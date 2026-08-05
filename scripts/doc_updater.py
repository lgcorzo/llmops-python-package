import ast
import os
import shutil
import sys
import subprocess
from pathlib import Path

IGNORED_FOLDERS = {
    '.git', '.github', '.vscode', '.idea', 'node_modules',
    'dist', 'bin', 'obj', 'target', 'coverage', '__pycache__',
    'openwiki', '.agents', '.pytest_cache', '.venv', 'venv', 'env'
}

def get_changed_files():
    try:
        # Get changed files from PR or local diff
        output = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD']).decode('utf-8')
        files = output.strip().split('\n')
        if not any(files):
            # Try to get diff between main and HEAD
            output = subprocess.check_output(['git', 'diff', '--name-only', 'main']).decode('utf-8')
            files = output.strip().split('\n')
        return [f for f in files if f.endswith('.py') and Path(f).exists()]
    except Exception as e:
        print(f"Warning: Could not get changed files via git: {e}")
        return []

def get_ast(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return ast.parse(f.read(), filename=filepath)
    except Exception as e:
        print(f"Failed to parse {filepath}: {e}")
        return None

def extract_info(filepath):
    tree = get_ast(filepath)
    if not tree:
        return None

    imports = []
    classes = []
    functions = []

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ''
            for alias in node.names:
                imports.append(f"{module}.{alias.name}")
        elif isinstance(node, ast.ClassDef):
            classes.append(node)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(node)

    return {
        'imports': imports,
        'classes': classes,
        'functions': functions,
        'docstring': ast.get_docstring(tree)
    }

def format_type(node):
    if node is None:
        return "Any"
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{format_type(node.value)}.{node.attr}"
    if isinstance(node, ast.Subscript):
        return f"{format_type(node.value)}[{format_type(node.slice)}]"
    if isinstance(node, ast.Constant):
        return str(node.value)
    if isinstance(node, ast.List):
        return f"[{', '.join(format_type(elt) for elt in node.elts)}]"
    if isinstance(node, ast.Tuple):
        return f"({', '.join(format_type(elt) for elt in node.elts)})"
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.BitOr):
            return f"{format_type(node.left)} | {format_type(node.right)}"
    return "Any"

def format_args(args):
    arg_list = []
    defaults = [None] * (len(args.args) - len(args.defaults)) + args.defaults
    for arg, default_node in zip(args.args, defaults):
        arg_type = format_type(arg.annotation)
        default = ast.unparse(default_node) if default_node else None
        arg_list.append((arg.arg, arg_type, default))

    # Handle kwonlyargs
    kw_defaults = args.kw_defaults if hasattr(args, 'kw_defaults') else []
    for arg, default_node in zip(getattr(args, 'kwonlyargs', []), kw_defaults):
        arg_type = format_type(arg.annotation)
        default = ast.unparse(default_node) if default_node else None
        arg_list.append((arg.arg, arg_type, default))

    return arg_list

def generate_markdown(filepath, info, outdir, rel_path):
    outpath = outdir / rel_path.with_suffix('.md')
    outpath.parent.mkdir(parents=True, exist_ok=True)

    with open(outpath, 'w', encoding='utf-8') as f:
        # YAML Frontmatter
        f.write("---\n")
        f.write(f"title: {rel_path}\n")
        f.write(f"source: {rel_path}\n")
        f.write("---\n\n")

        f.write(f"# Document: {rel_path}\n\n")

        f.write("## Module Overview\n\n")
        if info['docstring']:
            f.write(f"{info['docstring']}\n\n")

        f.write("### Purpose\n")
        f.write(f"Provides functionality for `{rel_path.stem}`.\n\n")
        f.write("### Responsibilities\n")
        f.write(f"Handles operations and definitions related to `{rel_path.stem}`.\n\n")
        f.write("### Main Workflow\n")
        f.write("Execution flow defined by the functions and classes in the module.\n\n")
        f.write("### Dependencies\n")
        for imp in info['imports']:
            f.write(f"- `{imp}`\n")
        if not info['imports']:
            f.write("None\n")
        f.write("\n")

        # Public API
        f.write("## Public API\n\n")
        f.write("### Exported Classes\n")
        for c in info['classes']:
            if not c.name.startswith('_'):
                f.write(f"- `{c.name}`\n")
        if not any(not c.name.startswith('_') for c in info['classes']):
            f.write("None\n")

        f.write("\n### Exported Functions\n")
        for func in info['functions']:
            if not func.name.startswith('_'):
                f.write(f"- `{func.name}`\n")
        if not any(not f.name.startswith('_') for f in info['functions']):
            f.write("None\n")
        f.write("\n")

        # Classes
        if info['classes']:
            for c in info['classes']:
                is_public = not c.name.startswith('_')
                if not is_public:
                    continue
                f.write(f"## Class `{c.name}`\n\n")
                f.write("### Overview\n\n")
                cdoc = ast.get_docstring(c)
                if cdoc:
                    f.write(f"{cdoc}\n\n")
                else:
                    f.write(f"Represents `{c.name}` and provides business capabilities.\n\n")

                # Constructor and Methods
                methods = [n for n in c.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]

                # Attributes (heuristic: look at assignments in __init__ or class level)
                attributes = []
                for n in c.body:
                    if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
                        attributes.append((n.target.id, format_type(n.annotation)))

                if attributes:
                    f.write("### Attributes\n\n")
                    for attr_name, attr_type in attributes:
                        if not attr_name.startswith('_'):
                            f.write(f"- `{attr_name}` ({attr_type}): Public property.\n")
                    f.write("\n")

                for m in methods:
                    mdoc = ast.get_docstring(m) or "No description provided."
                    args = format_args(m.args)
                    returns = format_type(m.returns) if m.returns else "None"

                    if m.name == '__init__':
                        f.write("### Constructor\n\n")
                        f.write(f"{mdoc}\n\n")
                        f.write("**Parameters:**\n")
                        for a_name, a_type, a_default in args:
                            if a_name == 'self':
                                continue
                            f.write(f"- `{a_name}` ({a_type})")
                            if a_default:
                                f.write(f" = `{a_default}`")
                            f.write("\n")
                        f.write("\n")
                    elif not m.name.startswith('_'):
                        f.write(f"### Public Method `{m.name}`\n\n")
                        f.write(f"#### Description\n{mdoc}\n\n")
                        f.write("#### Inputs\n")
                        for a_name, a_type, a_default in args:
                            if a_name == 'self' or a_name == 'cls':
                                continue
                            f.write(f"- `{a_name}` ({a_type}): semantic meaning. ")
                            if a_default:
                                f.write(f"Optional (default: `{a_default}`).")
                            else:
                                f.write("Required.")
                            f.write("\n")
                        if len(args) <= 1 and args[0][0] in ('self', 'cls'):
                            f.write("None\n")
                        f.write("\n#### Output\n")
                        f.write(f"- Return type: `{returns}`\n")
                        f.write("- Semantic meaning: Result of the operation.\n\n")
                        f.write("#### Side Effects\n")
                        f.write("May update internal state or external services.\n\n")
                        f.write("#### Complexity\n")
                        f.write("- Time Complexity: O(1) mostly.\n")
                        f.write("- Space Complexity: O(1) mostly.\n\n")
                        f.write("#### Example\n")
                        f.write("```python\n")
                        f.write(f"# Example usage of {m.name}\n")
                        f.write(f"instance.{m.name}()\n")
                        f.write("```\n\n")
                    else:
                        f.write(f"### Private Method `{m.name}`\n\n")
                        f.write(f"**Purpose:** {mdoc}\n\n")
                        f.write("**Parameters:**\n")
                        for a_name, a_type, _ in args:
                            if a_name == 'self' or a_name == 'cls':
                                continue
                            f.write(f"- `{a_name}`: {a_type}\n")
                        f.write("\n**Return value:**\n")
                        f.write(f"- `{returns}`\n\n")

        # Functions
        if info['functions']:
            for func in info['functions']:
                fdoc = ast.get_docstring(func) or "No description provided."
                args = format_args(func.args)
                returns = format_type(func.returns) if func.returns else "None"

                if not func.name.startswith('_'):
                    f.write(f"## Public Function `{func.name}`\n\n")
                    f.write(f"### Description\n{fdoc}\n\n")
                    f.write("### Inputs\n")
                    for a_name, a_type, a_default in args:
                        f.write(f"- `{a_name}` ({a_type}): semantic meaning. ")
                        if a_default:
                            f.write(f"Optional (default: `{a_default}`).")
                        else:
                            f.write("Required.")
                        f.write("\n")
                    if not args:
                        f.write("None\n")
                    f.write("\n### Output\n")
                    f.write(f"- Return type: `{returns}`\n")
                    f.write("- Semantic meaning: Result of the operation.\n\n")
                    f.write("### Side Effects\n")
                    f.write("May update state or affect global resources.\n\n")
                    f.write("### Complexity\n")
                    f.write("- Time Complexity: O(1) mostly.\n")
                    f.write("- Space Complexity: O(1) mostly.\n\n")
                    f.write("### Example\n")
                    f.write("```python\n")
                    f.write(f"# Example usage of {func.name}\n")
                    f.write(f"{func.name}()\n")
                    f.write("```\n\n")
                else:
                    f.write(f"## Private Function `{func.name}`\n\n")
                    f.write(f"**Purpose:** {fdoc}\n\n")
                    f.write("**Parameters:**\n")
                    for a_name, a_type, _ in args:
                        f.write(f"- `{a_name}`: {a_type}\n")
                    f.write("\n**Return value:**\n")
                    f.write(f"- `{returns}`\n\n")

        # PlantUML
        f.write("## UML Diagram\n\n")
        f.write("```plantuml\n")
        f.write("@startuml\n")
        if info['classes']:
            for c in info['classes']:
                f.write(f"class {c.name} {{\n")
                methods = [n for n in c.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
                for m in methods:
                    if m.name.startswith('_') and m.name != '__init__':
                        f.write(f"  - {m.name}()\n")
                    else:
                        f.write(f"  + {m.name}()\n")
                f.write("}\n")

                # Inheritance
                for base in c.bases:
                    base_name = format_type(base)
                    f.write(f"{base_name} <|-- {c.name}\n")
        else:
            f.write("note \"No classes in module\" as N1\n")
        f.write("@enduml\n")
        f.write("```\n\n")

def generate_indexes(outdir, all_files):
    with open(outdir / 'index.md', 'w') as f:
        f.write("# Project Documentation\n\n")
        f.write("Welcome to the OKF Documentation.\n\n")
        f.write("## Modules\n\n")
        for fpath in sorted(all_files):
            f.write(f"- [{fpath}]({fpath.with_suffix('.md')})\n")

    with open(outdir / 'SUMMARY.md', 'w') as f:
        f.write("# Table of contents\n\n")
        f.write("* [Introduction](index.md)\n")
        for fpath in sorted(all_files):
            f.write(f"* [{fpath}]({fpath.with_suffix('.md')})\n")

def get_all_python_files(root_dir='.'):
    all_files = []
    for root, dirs, files in os.walk(root_dir):
        # Exclude ignored folders
        dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS and not d.startswith('.')]
        for file in files:
            if file.endswith('.py'):
                filepath = Path(root) / file
                all_files.append(filepath)
    return all_files

def build_docs(mode='full'):
    out_dir = Path('openwiki')

    if mode == 'full':
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)

        for folder in ['architecture', 'modules', 'api', 'classes', 'diagrams', 'dependencies', 'glossary', 'decisions', 'generated']:
            (out_dir / folder).mkdir(exist_ok=True)

        files_to_process = get_all_python_files()
    else:
        if not out_dir.exists():
            print("openwiki directory does not exist. Running full mode instead.")
            return build_docs('full')

        changed = get_changed_files()
        files_to_process = [Path(f) for f in changed if Path(f).exists()]
        if not files_to_process:
            print("No Python files modified.")
            return

    processed_rel_paths = set()

    # Process files
    for filepath in files_to_process:
        # Avoid generating for scripts/doc_updater.py or root setup.py if we just want src?
        # The instruction says: "The skill shall recursively inspect every source folder. Ignored folders... Everything else is documented."
        # We process everything not ignored.
        rel_path = filepath
        info = extract_info(filepath)
        if info is not None:
            generate_markdown(filepath, info, out_dir, rel_path)
            processed_rel_paths.add(rel_path)

    # Now regenerate index if we need to. For diff mode, we might need all existing .md files
    # to rebuild SUMMARY.md and index.md.
    if mode == 'full':
        all_md_files = list(processed_rel_paths)
    else:
        # Find all .md files in openwiki that correspond to .py files (excluding special ones)
        all_md_files = []
        for root, dirs, files in os.walk(out_dir):
            if Path(root) == out_dir and set(dirs).intersection({'architecture', 'modules', 'api', 'classes', 'diagrams', 'dependencies', 'glossary', 'decisions', 'generated'}):
                pass
            for file in files:
                if file.endswith('.md') and file not in ('index.md', 'SUMMARY.md'):
                    md_path = Path(root) / file
                    rel_py = md_path.relative_to(out_dir).with_suffix('.py')
                    all_md_files.append(rel_py)

        # Add newly processed if they were somehow not there (e.g. new files)
        for rp in processed_rel_paths:
            if rp not in all_md_files:
                all_md_files.append(rp)

    generate_indexes(out_dir, all_md_files)
    print(f"Documentation generated successfully in {mode} mode.")

def main():
    mode = 'full'
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode not in ('full', 'diff'):
            print(f"Unknown mode: {mode}. Use 'full' or 'diff'.")
            sys.exit(1)

    build_docs(mode)

if __name__ == '__main__':
    main()
