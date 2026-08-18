import os
import ast
import shutil
import argparse
import subprocess
from datetime import datetime, timezone

IGNORED_DIRS = {
    ".git",
    ".github",
    ".vscode",
    ".idea",
    "node_modules",
    "dist",
    "bin",
    "obj",
    "target",
    "coverage",
    "__pycache__",
    ".venv",
    "venv",
    "openwiki",
    ".agents",
    ".artifacts",
    ".jules",
}


def get_python_files(root_dir):
    py_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS and not d.startswith(".")]
        for f in filenames:
            if f.endswith(".py"):
                py_files.append(os.path.join(dirpath, f))
    return py_files


def get_changed_files():
    try:
        output = subprocess.check_output(
            ["git", "diff", "--name-only", "main...HEAD"], universal_newlines=True
        )
        return [f for f in output.splitlines() if f.endswith(".py") and os.path.exists(f)]
    except subprocess.CalledProcessError:
        try:
            output = subprocess.check_output(
                ["git", "diff", "--name-only", "HEAD"], universal_newlines=True
            )
            return [f for f in output.splitlines() if f.endswith(".py") and os.path.exists(f)]
        except subprocess.CalledProcessError:
            return []


def parse_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return ast.parse(content), content
    except Exception as e:
        print(f"Failed to parse {filepath}: {e}")
        return None, ""


def extract_classes(tree):
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]


def extract_functions(tree):
    return [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef)
    ]


def get_arg_type(arg, default_val=None):
    if hasattr(arg, "annotation") and arg.annotation is not None:
        try:
            return ast.unparse(arg.annotation)
        except Exception:
            pass
    return "Any"


def get_return_type(node):
    if hasattr(node, "returns") and node.returns is not None:
        try:
            return ast.unparse(node.returns)
        except Exception:
            pass
    return "Any"


GLOBAL_SYMBOLS = {"classes": {}, "functions": {}, "imports": {}, "calls": {}, "layer": {}}


def populate_globals(py_files):
    for f in py_files:
        tree, _ = parse_file(f)
        if not tree:
            continue

        GLOBAL_SYMBOLS["layer"][f] = analyze_architecture(f)
        GLOBAL_SYMBOLS["imports"][f] = []
        GLOBAL_SYMBOLS["calls"][f] = []

        for n in tree.body:
            if isinstance(n, ast.ClassDef):
                GLOBAL_SYMBOLS["classes"][n.name] = f
            elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                GLOBAL_SYMBOLS["functions"][n.name] = f
            elif isinstance(n, ast.Import):
                for alias in n.names:
                    GLOBAL_SYMBOLS["imports"][f].append(alias.name)
            elif isinstance(n, ast.ImportFrom):
                mod = n.module or ""
                for alias in n.names:
                    GLOBAL_SYMBOLS["imports"][f].append(f"{mod}.{alias.name}")

        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    GLOBAL_SYMBOLS["calls"][f].append(node.func.id)
                elif isinstance(node.func, ast.Attribute):
                    GLOBAL_SYMBOLS["calls"][f].append(node.func.attr)


def md_link(target_filepath, source_filepath=None):
    target_md = os.path.join("openwiki", "modules", os.path.relpath(target_filepath, ".")).replace(
        ".py", ".md"
    )
    if source_filepath:
        source_md_dir = os.path.dirname(
            os.path.join("openwiki", "modules", os.path.relpath(source_filepath, ".")).replace(
                ".py", ".md"
            )
        )
        return os.path.relpath(target_md, source_md_dir)
    else:
        # if no source, assume linking from a root index file (e.g., classes/index.md)
        return os.path.relpath(target_md, os.path.join("openwiki", "classes"))


def generate_uml_sequence(filepath, tree):
    uml = ["```plantuml", "@startuml"]
    funcs = extract_functions(tree)
    if not funcs:
        uml.append("    ' No functions for sequence")
    for f in funcs:
        calls = []
        for node in ast.walk(f):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    calls.append(node.func.id)
                elif isinstance(node.func, ast.Attribute):
                    calls.append(node.func.attr)
        for c in set(calls):
            uml.append(f"    {f.name} -> {c} : call")
    uml.extend(["@enduml", "```"])
    return uml


def generate_uml_component(filepath):
    uml = ["```plantuml", "@startuml"]
    layer = GLOBAL_SYMBOLS["layer"].get(filepath, "Unknown")
    uml.append(f'    package "{layer}" {{')
    uml.append(f"        [{os.path.basename(filepath)}]")
    uml.append("    }")
    for imp in GLOBAL_SYMBOLS["imports"].get(filepath, []):
        uml.append(f"    [{os.path.basename(filepath)}] --> [{imp}]")
    uml.extend(["@enduml", "```"])
    return uml


def analyze_architecture(filepath):
    lower_path = filepath.lower()
    if "controller" in lower_path or "api" in lower_path:
        return "Controllers"
    elif "service" in lower_path:
        return "Services"
    elif "repository" in lower_path or "data" in lower_path:
        return "Repositories"
    elif "model" in lower_path or "entity" in lower_path:
        return "Entities/Domain Models"
    elif "dto" in lower_path:
        return "DTOs"
    else:
        return "Infrastructure/Other"


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
    lines.append("- Not explicitly defined.")
    lines.append("")
    lines.append("**Main Workflow:**")
    lines.append("- Not explicitly defined.")
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

    lines.append("**Exported Interfaces:**")
    lines.append("- Not explicitly defined.")
    lines.append("")

    lines.append("**Public API:**")
    lines.append("- Not explicitly defined.")
    lines.append("")

    lines.append("## 3. Architecture & Execution")
    lines.append("### Internal Architecture")
    lines.append("Not explicitly defined.")
    lines.append("")
    lines.append("### Execution Flow")
    lines.append("Not explicitly defined.")
    lines.append("")
    lines.append("### Sequence Explanation")
    lines.append("Not explicitly defined.")
    lines.append("")

    lines.append("### Examples")
    lines.append("Not explicitly defined.")
    lines.append("")

    lines.append("## 4. UML 2.0 Diagrams")
    lines.append("### Class Diagram")
    lines.extend(generate_uml_diagram(classes))
    lines.append("")
    lines.append("### Sequence Diagram")
    lines.extend(generate_uml_sequence(filepath, tree))
    lines.append("")
    lines.append("### Component Diagram")
    lines.extend(generate_uml_component(filepath))
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
            lines.append(
                f"Provides state and behavior management for {cls.name.replace('Agent', ' Agent')}."
            )
        lines.append("")

        has_init = any(
            isinstance(node, ast.FunctionDef) and node.name == "__init__" for node in cls.body
        )
        if has_init:
            lines.append("#### Constructor")
            lines.append(
                f"**Initialization:** Initializes `{cls.name}` with required dependencies and sets up initial internal state."
            )
            lines.append("")

        lines.append("#### Attributes")

        # Extract attributes from assignments in __init__
        attributes = []
        for node in cls.body:
            if isinstance(node, ast.FunctionDef) and node.name == "__init__":
                for stmt in node.body:
                    if isinstance(stmt, ast.Assign):
                        for target in stmt.targets:
                            if (
                                isinstance(target, ast.Attribute)
                                and isinstance(target.value, ast.Name)
                                and target.value.id == "self"
                            ):
                                attributes.append(target.attr)
                    elif isinstance(stmt, ast.AnnAssign):
                        if (
                            isinstance(stmt.target, ast.Attribute)
                            and isinstance(stmt.target.value, ast.Name)
                            and stmt.target.value.id == "self"
                        ):
                            attributes.append(stmt.target.attr)

        if attributes:
            for attr in attributes:
                lines.append(f"- `{attr}`")
                lines.append("  - Type: Any")
                lines.append("  - Purpose: Not explicitly defined.")
                lines.append("  - Constraints: Not explicitly defined.")
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
                    if arg.arg == "self":
                        input_args.append("self")
                    else:
                        input_args.append(f"{arg.arg}: {get_arg_type(arg)}")
                inputs_str = ", ".join(input_args)

                is_private = node.name.startswith("_") and node.name != "__init__"
                visibility = "Private" if is_private else "Public"

                lines.append(f"##### `{node.name}({inputs_str}) -> {ret_type}` ({visibility})")
                func_doc = ast.get_docstring(node)

                if is_private:
                    if func_doc:
                        lines.append(f"**Purpose:** {func_doc}")
                    else:
                        lines.append("**Purpose:** No description provided.")
                    lines.append("")
                    lines.append("**Parameters:**")
                    has_params = False
                    for arg in node.args.args:
                        if arg.arg == "self":
                            continue
                        has_params = True
                        arg_type = get_arg_type(arg)
                        lines.append(f"- `{arg.arg}`: {arg_type}")
                    if not has_params:
                        lines.append("- None")
                    lines.append("")
                    lines.append("**Return value:**")
                    lines.append(f"- `{ret_type}`")
                    lines.append("")
                else:
                    if func_doc:
                        lines.append(f"**Description:** {func_doc}")
                    else:
                        lines.append("**Description:** No description provided.")
                    lines.append("")
                    lines.append("**Inputs:**")
                    has_params = False
                    num_defaults = len(node.args.defaults) if node.args.defaults else 0
                    num_args = len(node.args.args)
                    default_offset = num_args - num_defaults
                    for i, arg in enumerate(node.args.args):
                        if arg.arg == "self":
                            continue
                        has_params = True
                        arg_type = get_arg_type(arg)
                        default_val = "None"
                        is_optional = "False"
                        if i >= default_offset:
                            try:
                                default_val = ast.unparse(node.args.defaults[i - default_offset])
                                is_optional = "True"
                            except Exception:
                                default_val = "Unknown"

                        lines.append(f"- `{arg.arg}`")
                        lines.append(f"  - type: {arg_type}")
                        lines.append("  - meaning: Not explicitly defined.")
                        lines.append("  - valid values: Not explicitly defined.")
                        lines.append(f"  - optional?: {is_optional}")
                        lines.append(f"  - default value: {default_val}")

                    if not has_params:
                        lines.append("- None")
                    lines.append("")
                    lines.append("**Output:**")
                    lines.append(f"- return type: `{ret_type}`")
                    lines.append("- semantic meaning: Not explicitly defined.")
                    lines.append("- possible null values: Not explicitly defined.")
                    lines.append("- exceptions: Not explicitly defined.")
                    lines.append("")
                    lines.append("**Side Effects:**")
                    lines.append("- Database updates: Not explicitly defined.")
                    lines.append("- File operations: Not explicitly defined.")
                    lines.append("- Network calls: Not explicitly defined.")
                    lines.append("- Cache: Not explicitly defined.")
                    lines.append("- State changes: Not explicitly defined.")
                    lines.append("")
                    lines.append("**Complexity:**")
                    lines.append("- Time Complexity: Not explicitly defined.")
                    lines.append("- Space Complexity: Not explicitly defined.")
                    lines.append("")
                    lines.append("**Example:**")
                    lines.append("```python")
                    if has_init:
                        lines.append(f"instance = {cls.name}()")

                        ex_args = []
                        for arg in node.args.args:
                            if arg.arg != "self":
                                ex_args.append("...")
                        ex_args_str = ", ".join(ex_args)

                        lines.append(f"result = instance.{node.name}({ex_args_str})")
                    else:
                        ex_args = []
                        for arg in node.args.args:
                            if arg.arg != "self":
                                ex_args.append("...")
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
            lines.append("No description provided.")
        lines.append("")
        lines.append("**Inputs:**")

        has_params = False
        num_defaults = len(func.args.defaults) if func.args.defaults else 0
        num_args = len(func.args.args)
        default_offset = num_args - num_defaults
        for i, arg in enumerate(func.args.args):
            has_params = True
            arg_type = get_arg_type(arg)
            default_val = "None"
            is_optional = "False"
            if i >= default_offset:
                try:
                    default_val = ast.unparse(func.args.defaults[i - default_offset])
                    is_optional = "True"
                except Exception:
                    default_val = "Unknown"

            lines.append(f"- `{arg.arg}`")
            lines.append(f"  - type: {arg_type}")
            lines.append("  - meaning: Not explicitly defined.")
            lines.append("  - valid values: Not explicitly defined.")
            lines.append(f"  - optional?: {is_optional}")
            lines.append(f"  - default value: {default_val}")

        if not has_params:
            lines.append("- None")
        lines.append("")
        lines.append("**Output:**")
        ret_type = get_return_type(func)
        lines.append(f"- return type: `{ret_type}`")
        lines.append("- semantic meaning: Not explicitly defined.")
        lines.append("- possible null values: Not explicitly defined.")
        lines.append("- exceptions: Not explicitly defined.")
        lines.append("")
        lines.append("**Side Effects:**")
        lines.append("- Database updates: Not explicitly defined.")
        lines.append("- File operations: Not explicitly defined.")
        lines.append("- Network calls: Not explicitly defined.")
        lines.append("- Cache: Not explicitly defined.")
        lines.append("- State changes: Not explicitly defined.")
        lines.append("")

    called_from = []
    used_by = []
    calls = set(GLOBAL_SYMBOLS["calls"].get(filepath, []))
    for other_file, other_calls in GLOBAL_SYMBOLS["calls"].items():
        if other_file == filepath:
            continue
        for c in classes:
            if c.name in other_calls:
                used_by.append(md_link(other_file, filepath))
        for f in functions:
            if f.name in other_calls:
                called_from.append(md_link(other_file, filepath))

    lines.append("## 7. Call Graph")
    if calls:
        lines.append("```plantuml")
        lines.append("@startuml")
        title = os.path.basename(filepath).replace(".py", "")
        for c in calls:
            lines.append(f"[{title}] --> [{c}] : calls")
        lines.append("@enduml")
        lines.append("```")
    else:
        lines.append("- No public API calls detected.")
    lines.append("")

    # Calculate depth to openwiki root
    rel_source_dir = os.path.dirname(
        os.path.join("openwiki", "modules", os.path.relpath(filepath, ".")).replace(".py", ".md")
    )
    depth = rel_source_dir.count(os.sep)
    up_path = "../" * depth if depth > 0 else "./"

    lines.append("## 8. Cross References")
    lines.append(f"- **Dependencies:** [Dependencies]({up_path}dependencies/index.md)")
    lines.append(f"- **Used by:** {', '.join(set(used_by)) if used_by else 'None'}")
    lines.append(f"- **Calls:** {', '.join(calls) if calls else 'None'}")
    lines.append(f"- **Called from:** {', '.join(set(called_from)) if called_from else 'None'}")
    lines.append(f"- **Related classes:** [Classes]({up_path}classes/index.md)")
    lines.append(f"- **Related diagrams:** [Diagrams]({up_path}diagrams/index.md)\n")

    return "\n".join(lines)


def update_indexes(py_files):
    summary_lines = [
        "# Summary",
        "",
        "## Navigation",
        "- [Home](index.md)",
        "- [Glossary](glossary/index.md)",
        "- [Decisions](decisions/index.md)",
        "",
        "## Table of contents",
        "",
        "## Architecture overview",
        "- [Architecture](architecture/index.md)",
        "",
        "## Module list",
    ]

    index_lines = [
        "# Project Documentation Index",
        "",
        "Welcome to the fully AST-generated project documentation.",
        "",
        "## Navigation",
        "- [Summary](SUMMARY.md)",
        "",
        "## Architecture overview",
        "- [Architecture](architecture/index.md)",
        "",
        "## Module list",
    ]

    docs_created = []
    global_classes = []
    global_functions = []

    for filepath in py_files:
        rel_path = os.path.relpath(filepath, ".")
        out_path = os.path.join("openwiki", "modules", rel_path).replace(".py", ".md")
        if os.path.exists(out_path):
            docs_created.append((rel_path, out_path))

            tree, _ = parse_file(filepath)
            if tree:
                classes = extract_classes(tree)
                functions = extract_functions(tree)
                rel_link = out_path.replace("openwiki/", "./")
                for cls in classes:
                    global_classes.append((cls.name, rel_link))
                for func in functions:
                    global_functions.append((func.name, rel_link))

    for rel_path, out_path in sorted(docs_created):
        name = os.path.basename(rel_path).replace(".py", "")
        rel_link = out_path.replace("openwiki/", "./")
        summary_lines.append(f"- [{name}]({rel_link})")
        index_lines.append(f"- [{rel_path}]({rel_link})")

    summary_lines.append("")
    summary_lines.append("## Alphabetical class index")
    index_lines.append("")
    index_lines.append("## Alphabetical class index")
    for cls_name, link in sorted(global_classes, key=lambda x: x[0].lower()):
        summary_lines.append(f"- [{cls_name}]({link})")
        index_lines.append(f"- [{cls_name}]({link})")

    summary_lines.append("")
    summary_lines.append("## Public API index")
    index_lines.append("")
    index_lines.append("## Public API index")
    for func_name, link in sorted(global_functions, key=lambda x: x[0].lower()):
        # Filter out private methods loosely if wanted, but instructions just say public api index
        if not func_name.startswith("_"):
            summary_lines.append(f"- [{func_name}]({link})")
            index_lines.append(f"- [{func_name}]({link})")

    with open("openwiki/SUMMARY.md", "w") as f:
        f.write("\n".join(summary_lines))

    with open("openwiki/index.md", "w") as f:
        f.write("\n".join(index_lines))

    folders_to_init = [
        "architecture",
        "api",
        "classes",
        "diagrams",
        "dependencies",
        "glossary",
        "decisions",
        "generated",
    ]
    for folder in folders_to_init:
        idx_path = os.path.join("openwiki", folder, "index.md")
        lines = [f"# {folder.capitalize()} Index\n"]
        if folder == "classes":
            for cls_name, fp in sorted(GLOBAL_SYMBOLS["classes"].items()):
                target_md = os.path.join("openwiki", "modules", os.path.relpath(fp, ".")).replace(
                    ".py", ".md"
                )
                lines.append(
                    f"- [{cls_name}]({os.path.relpath(target_md, os.path.join('openwiki', folder))})"
                )
        elif folder == "api":
            for fn_name, fp in sorted(GLOBAL_SYMBOLS["functions"].items()):
                target_md = os.path.join("openwiki", "modules", os.path.relpath(fp, ".")).replace(
                    ".py", ".md"
                )
                lines.append(
                    f"- [{fn_name}]({os.path.relpath(target_md, os.path.join('openwiki', folder))})"
                )
        elif folder == "dependencies":
            for fp, imps in sorted(GLOBAL_SYMBOLS["imports"].items()):
                if imps:
                    lines.append(f"- `{os.path.basename(fp)}` depends on: {', '.join(imps[:5])}...")
        else:
            lines.append(f"Index for {folder}.")

        with open(idx_path, "w") as f:
            f.write("\n".join(lines))


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
        "generated",
    ]
    for folder in folders:
        os.makedirs(os.path.join("openwiki", folder), exist_ok=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["full", "diff"], required=True)
    args = parser.parse_args()

    all_py = get_python_files(".")
    populate_globals(all_py)

    if args.mode == "full":
        if os.path.exists("openwiki"):
            shutil.rmtree("openwiki")
        build_okf_folders()
        py_files = get_python_files(".")
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

        rel_path = os.path.relpath(filepath, ".")
        out_path = os.path.join("openwiki", "modules", rel_path).replace(".py", ".md")

        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(doc_content)

    if args.mode == "full":
        update_indexes(py_files)
    else:
        update_indexes(get_python_files("."))


if __name__ == "__main__":
    main()
