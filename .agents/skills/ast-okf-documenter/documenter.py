import os
import ast
import shutil
import argparse
import subprocess
from datetime import datetime, timezone

IGNORED_DIRS = {
    ".git", ".github", ".vscode", ".idea", "node_modules",
    "dist", "bin", "obj", "target", "coverage", "__pycache__",
    ".venv", "venv", "openwiki", ".agents", ".artifacts", ".jules"
}

def get_python_files(root_dir):
    py_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS and not d.startswith('.')]
        for f in filenames:
            if f.endswith('.py'):
                py_files.append(os.path.join(dirpath, f))
    return py_files

def get_changed_files():
    try:
        output = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], universal_newlines=True)
        return [f for f in output.splitlines() if f.endswith('.py') and os.path.exists(f)]
    except subprocess.CalledProcessError:
        return []

def parse_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return ast.parse(content), content
    except Exception as e:
        print(f"Failed to parse {filepath}: {e}")
        return None, ""

def extract_classes(tree):
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]

def extract_functions(tree):
    return [node for node in tree.body if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef)]

def get_arg_type(arg, default_val=None):
    if hasattr(arg, 'annotation') and arg.annotation is not None:
        if isinstance(arg.annotation, ast.Name):
            return arg.annotation.id
        elif isinstance(arg.annotation, ast.Subscript):
            if isinstance(arg.annotation.value, ast.Name):
                return f"{arg.annotation.value.id}[...]"
    return "Any"

def get_return_type(node):
    if hasattr(node, 'returns') and node.returns is not None:
        if isinstance(node.returns, ast.Name):
            return node.returns.id
        elif isinstance(node.returns, ast.Constant) and node.returns.value is None:
            return "None"
    return "Any"

def analyze_architecture(filepath):
    lower_path = filepath.lower()
    if 'controller' in lower_path or 'api' in lower_path:
        return 'Controllers'
    elif 'service' in lower_path:
        return 'Services'
    elif 'repository' in lower_path or 'data' in lower_path:
        return 'Repositories'
    elif 'model' in lower_path or 'entity' in lower_path:
        return 'Entities/Domain Models'
    elif 'dto' in lower_path:
        return 'DTOs'
    else:
        return 'Infrastructure/Other'

def generate_uml_diagram(classes):
    uml = ["```plantuml", "@startuml"]
    if classes:
        for cls in classes:
            uml.append(f"    class {cls.name} {{")
            for node in cls.body:
                if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                    ret_type = get_return_type(node)
                    uml.append(f"        +{node.name}() : {ret_type}")
            uml.append("    }")
    else:
        uml.append("    ' No classes found in module")
    uml.extend(["@enduml", "```"])
    return uml

def generate_dependency_diagram(imports):
    uml = ["```plantuml", "@startuml"]
    if imports:
        for imp in imports:
            uml.append(f"    [Module] --> [{imp}] : imports")
    else:
        uml.append("    ' No imports found in module")
    uml.extend(["@enduml", "```"])
    return uml


def generate_doc_for_file(filepath, tree):
    classes = extract_classes(tree)
    functions = extract_functions(tree)

    lines = []

    lines.append("---")
    lines.append('iso_doc_type: "Specification"')
    lines.append('iso_viewpoint: "ComponentView"')
    lines.append('type: "module"')
    title = os.path.basename(filepath).replace(".py", "")
    lines.append(f'title: "Module: {title}"')
    lines.append(f'source_path: "{filepath.lstrip("./")}"')
    lines.append('description: "AST-generated documentation for the module."')
    lines.append('tags: ["generated", "ast"]')
    lines.append(f'timestamp: "{datetime.now(timezone.utc).isoformat()}"')
    lines.append("---")
    lines.append("")
    lines.append(f"# Module Specification: {title}")
    lines.append("")
    lines.append(f"* **Source Reference:** `{filepath.lstrip('./')}`")
    lines.append("")
    lines.append("## 1. Architectural Role & Responsibilities")
    lines.append("**Purpose:**")
    lines.append(f"Provides functionality related to {title.replace('_', ' ')}.")
    lines.append("")
    lines.append("**Architecture Layer:**")
    lines.append(f"- {analyze_architecture(filepath)}")
    lines.append("")
    lines.append("**Responsibilities:**")
    lines.append(f"- Manage and execute operations for {title}.")
    lines.append("")
    lines.append("**Main Workflow:**")
    lines.append(f"- Initialize components and process requests for {title}.")
    lines.append("")
    lines.append("## 2. Dependencies")

    imports = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            for alias in node.names:
                imports.append(f"{module}.{alias.name}")

    lines.append("**Imports:**")
    for imp in imports:
        lines.append(f"- `{imp}`")
    if not imports:
        lines.append("- None")
    lines.append("")

    lines.append("**Exported Classes:**")
    for cls in classes:
        lines.append(f"- `{cls.name}`")
    if not classes:
        lines.append("- None")
    lines.append("")

    lines.append("**Exported Functions:**")
    for func in functions:
        lines.append(f"- `{func.name}`")
    if not functions:
        lines.append("- None")
    lines.append("")

    lines.append("## 3. Architecture & Execution")
    lines.append("### Internal Architecture")
    lines.append("Follows standard modular design, encapsulating state and behavior within defined classes and functions.")
    lines.append("")
    lines.append("### Execution Flow")
    lines.append("Sequential execution of defined functions and class methods.")
    lines.append("")
    lines.append("### Sequence Explanation")
    lines.append("Clients instantiate classes or call functions, which execute business logic and return results.")
    lines.append("")

    lines.append("## 4. UML 2.0 Diagrams")
    lines.append("### Class Diagram")
    lines.extend(generate_uml_diagram(classes))
    lines.append("")
    lines.append("### Dependency Graph")
    lines.extend(generate_dependency_diagram(imports))
    lines.append("")

    lines.append("## 5. Class & Method Specifications")
    for cls in classes:
        lines.append(f"### `{cls.name}` ([`{filepath.lstrip('./')}`](/{filepath.lstrip('./')}))")
        lines.append("#### Overview")
        cls_doc = ast.get_docstring(cls)
        if cls_doc:
            lines.append(cls_doc)
        else:
            lines.append(f"Provides state and behavior management for {cls.name.replace('Agent', ' Agent')}.")
        lines.append("")

        has_init = any(isinstance(node, ast.FunctionDef) and node.name == '__init__' for node in cls.body)
        if has_init:
            lines.append("#### Constructor")
            lines.append(f"**Initialization:** Initializes `{cls.name}` with required dependencies and sets up initial internal state.")
            lines.append("")

        lines.append("#### Attributes")

        # Extract attributes from assignments in __init__
        attributes = []
        for node in cls.body:
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                for stmt in node.body:
                    if isinstance(stmt, ast.Assign):
                        for target in stmt.targets:
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == 'self':
                                attributes.append(target.attr)
                    elif isinstance(stmt, ast.AnnAssign):
                        if isinstance(stmt.target, ast.Attribute) and isinstance(stmt.target.value, ast.Name) and stmt.target.value.id == 'self':
                            attributes.append(stmt.target.attr)

        if attributes:
            for attr in attributes:
                lines.append(f"- `{attr}`")
        else:
            lines.append("- None found.")
        lines.append("")

        lines.append("#### Methods")
        for node in cls.body:
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                ret_type = get_return_type(node)

                # Determine inputs string for method signature
                input_args = []
                for arg in node.args.args:
                    if arg.arg == 'self':
                        input_args.append('self')
                    else:
                        input_args.append(f"{arg.arg}: {get_arg_type(arg)}")
                inputs_str = ", ".join(input_args)

                lines.append(f"##### `{node.name}({inputs_str}) -> {ret_type}` (Public)")
                func_doc = ast.get_docstring(node)
                if func_doc:
                    lines.append(f"**Description:** {func_doc}")
                else:
                    lines.append(f"**Description:** Executes the {node.name} operation, mutating state or calculating derived values as necessary.")
                lines.append("")
                lines.append("**Inputs:**")
                for arg in node.args.args:
                    if arg.arg == 'self':
                        continue
                    arg_type = get_arg_type(arg)
                    lines.append(f"- `{arg.arg}`: {arg_type}")
                if len(node.args.args) <= 1 and any(arg.arg == 'self' for arg in node.args.args):
                    lines.append("- None")
                elif not node.args.args:
                    lines.append("- None")
                lines.append("")
                lines.append("**Output:**")
                lines.append(f"- Return Type: `{ret_type}`")
                lines.append(f"- Semantic Meaning: The resulting value after processing the {node.name} action.")
                lines.append("")
                lines.append("**Side Effects:**")
                lines.append("- Modifies internal instance state if applicable; performs operations constrained to its domain boundaries.")
                lines.append("")
                lines.append("**Complexity:**")
                lines.append("- Time Complexity: O(1) or O(N) depending on implementation details.")
                lines.append("- Space Complexity: O(1) auxiliary space expected.")
                lines.append("")
                lines.append("**Example:**")
                lines.append("```python")
                if has_init:
                    lines.append(f"instance = {cls.name}()")

                    ex_args = []
                    for arg in node.args.args:
                        if arg.arg != 'self':
                            ex_args.append('...')
                    ex_args_str = ", ".join(ex_args)

                    lines.append(f"result = instance.{node.name}({ex_args_str})")
                else:
                    ex_args = []
                    for arg in node.args.args:
                        if arg.arg != 'self':
                            ex_args.append('...')
                    ex_args_str = ", ".join(ex_args)
                    lines.append(f"result = {cls.name}.{node.name}({ex_args_str})")
                lines.append("```")
                lines.append("")

    lines.append("## 6. Module Functions")
    for func in functions:
        input_args = []
        for arg in func.args.args:
            input_args.append(f"{arg.arg}: {get_arg_type(arg)}")
        inputs_str = ", ".join(input_args)

        lines.append(f"### `{func.name}({inputs_str})`")
        func_doc = ast.get_docstring(func)
        if func_doc:
            lines.append(func_doc)
        else:
            lines.append(f"Executes the {func.name} operation.")
        lines.append("")
        lines.append("**Inputs:**")
        for arg in func.args.args:
            arg_type = get_arg_type(arg)
            lines.append(f"- `{arg.arg}`: {arg_type}")
        if not func.args.args:
            lines.append("- None")
        lines.append("")
        lines.append("**Output:**")
        ret_type = get_return_type(func)
        lines.append(f"- Return Type: `{ret_type}`")
        lines.append("")

    return "\n".join(lines)


def update_indexes(py_files):
    summary_lines = ["# Summary", ""]
    index_lines = ["# Project Documentation Index", "", "Welcome to the fully AST-generated project documentation.", "", "## Modules"]

    docs_created = []
    for filepath in py_files:
        rel_path = os.path.relpath(filepath, '.')
        out_path = os.path.join('openwiki', 'modules', rel_path).replace('.py', '.md')
        if os.path.exists(out_path):
            docs_created.append((rel_path, out_path))

    for rel_path, out_path in sorted(docs_created):
        name = os.path.basename(rel_path).replace(".py", "")
        rel_link = out_path.replace('openwiki/', './')
        summary_lines.append(f"- [{name}]({rel_link})")
        index_lines.append(f"- [{rel_path}]({rel_link})")

    with open('openwiki/SUMMARY.md', 'w') as f:
        f.write("\n".join(summary_lines))

    with open('openwiki/index.md', 'w') as f:
        f.write("\n".join(index_lines))

def build_okf_folders():
    folders = [
        "architecture",
        "modules",
        "api",
        "classes",
        "diagrams",
        "dependencies",
        "glossary",
        "decisions",
        "generated"
    ]
    for folder in folders:
        os.makedirs(os.path.join('openwiki', folder), exist_ok=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['full', 'diff'], required=True)
    args = parser.parse_args()

    if args.mode == 'full':
        if os.path.exists('openwiki'):
            shutil.rmtree('openwiki')
        build_okf_folders()
        py_files = get_python_files('.')
    else:
        build_okf_folders()
        py_files = get_changed_files()

    if not py_files:
        return

    for filepath in py_files:
        tree, content = parse_file(filepath)
        if not tree:
            continue

        doc_content = generate_doc_for_file(filepath, tree)

        rel_path = os.path.relpath(filepath, '.')
        out_path = os.path.join('openwiki', 'modules', rel_path).replace('.py', '.md')

        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

    if args.mode == 'full':
        update_indexes(py_files)
    else:
        update_indexes(get_python_files('.'))

if __name__ == "__main__":
    main()
