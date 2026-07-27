import argparse
import ast
import os
import re
import subprocess


def get_all_python_files():
    all_files = []
    for root_dir in ["src", "code"]:
        if os.path.exists(root_dir):
            for dirpath, _, filenames in os.walk(root_dir):
                for filename in filenames:
                    if filename.endswith(".py"):
                        all_files.append(os.path.join(dirpath, filename))
    return all_files, []


def get_modified_python_files(commit_range="HEAD~1"):
    try:
        if not commit_range:
            commit_range = "HEAD~1"

        # Get added and modified files
        output = subprocess.check_output(
            ["git", "diff", "--diff-filter=AM", "--name-only", commit_range]
        )
        files = output.decode("utf-8").splitlines()
        modified = [
            f
            for f in files
            if (f.startswith("src/") or f.startswith("code/"))
            and f.endswith(".py")
            and os.path.exists(f)
        ]

        # Get deleted files
        del_output = subprocess.check_output(
            ["git", "diff", "--diff-filter=D", "--name-only", commit_range]
        )
        del_files = del_output.decode("utf-8").splitlines()
        deleted = [
            f
            for f in del_files
            if (f.startswith("src/") or f.startswith("code/")) and f.endswith(".py")
        ]

        return modified, deleted
    except subprocess.CalledProcessError:
        print("git diff failed")
        return [], []


def extract_classes_and_functions(filepath):
    try:
        with open(filepath, "r") as f:
            tree = ast.parse(f.read())

        entities = []
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                entities.append(("class", node.name, ast.get_docstring(node), node))
            elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                entities.append(("api", node.name, ast.get_docstring(node), node))

        if not entities:
            return [
                (
                    "script",
                    os.path.basename(filepath).replace(".py", ""),
                    ast.get_docstring(tree),
                    None,
                )
            ]

        return entities
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return []


def get_git_sha():
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("utf-8").strip()
        )
    except subprocess.CalledProcessError:
        return "unknown"


def _generate_class_diagram(node, entity_name):
    if not node:
        return f"class {entity_name} {{\n    }}"

    methods = []
    attributes = []
    for item in node.body:
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = ", ".join([a.arg for a in item.args.args if a.arg != "self"])
            prefix = "+"
            if item.name.startswith("__"):
                prefix = "-"
            elif item.name.startswith("_"):
                prefix = "#"
            methods.append(f"        {prefix}{item.name}({args})")

            if item.name == "__init__":
                for stmt in item.body:
                    if isinstance(stmt, ast.Assign):
                        for target in stmt.targets:
                            if (
                                isinstance(target, ast.Attribute)
                                and isinstance(target.value, ast.Name)
                                and target.value.id == "self"
                            ):
                                attributes.append(f"        +{target.attr}")

    content = f"class {entity_name} {{\n"
    if attributes:
        content += "\n".join(attributes) + "\n"
    if methods:
        content += "\n".join(methods) + "\n"
    content += "    }"
    return content


def _generate_flowchart(node, entity_name):
    if not node:
        return f"Start --> {entity_name}_Execution\n    {entity_name}_Execution --> End"

    flow = ["Start --> Init"]
    calls = []
    for item in ast.walk(node):
        if isinstance(item, ast.Call):
            if isinstance(item.func, ast.Name):
                calls.append(item.func.id)
            elif isinstance(item.func, ast.Attribute):
                calls.append(item.func.attr)

    if calls:
        prev = "Init"
        for i, call in enumerate(calls):
            flow.append(f"{prev} --> call_{i}[{call}]")
            prev = f"call_{i}"
        flow.append(f"{prev} --> End")
    else:
        flow.append("Init --> End")

    return "\n    ".join(flow)


def generate_markdown(
    filepath, entity_type, entity_name, description, git_sha, node, existing_content=None
):
    filename = f"{entity_name}.md".lower().replace("_", "-")
    desc = (description or "Concise functional summary.").replace("\n", " ").strip()
    if not desc:
        desc = "Concise functional summary."

    mermaid_diagram = ""
    if entity_type == "class":
        mermaid_diagram = (
            f"```mermaid\nclassDiagram\n    {_generate_class_diagram(node, entity_name)}\n```"
        )
    elif entity_type in ("script", "module", "api"):
        mermaid_diagram = (
            f"```mermaid\nflowchart TD\n    {_generate_flowchart(node, entity_name)}\n```"
        )

    if existing_content:
        content = existing_content
        match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        if match:
            fm = match.group(1)
            lines = fm.split("\n")
            new_lines = []
            has_source = False
            has_commit = False
            for line in lines:
                if line.startswith("source_path:"):
                    new_lines.append(f'source_path: "{filepath}"')
                    has_source = True
                elif line.startswith("last_verified_commit:"):
                    new_lines.append(f'last_verified_commit: "{git_sha}"')
                    has_commit = True
                else:
                    new_lines.append(line)
            if not has_source:
                new_lines.append(f'source_path: "{filepath}"')
            if not has_commit:
                new_lines.append(f'last_verified_commit: "{git_sha}"')
            content = (
                content[: match.start()]
                + "---\n"
                + "\n".join(new_lines)
                + "\n---"
                + content[match.end() :]
            )

        source_file_pattern = re.compile(r"^Source File: `.*?`", re.MULTILINE)
        if source_file_pattern.search(content):
            content = source_file_pattern.sub(f"Source File: `{filepath}`", content)
        else:
            title_pattern = re.compile(r"^# " + re.escape(entity_name), re.MULTILINE)
            title_match = title_pattern.search(content)
            if title_match:
                content = (
                    content[: title_match.end()]
                    + f"\n\nSource File: `{filepath}`"
                    + content[title_match.end() :]
                )
            else:
                content += f"\n\nSource File: `{filepath}`"

        new_arch = f"## Architecture Visualization\n\n{mermaid_diagram}"
        arch_pattern = re.compile(
            r"## Architecture Visualization\s*\n```mermaid.*?```\n*", re.DOTALL
        )
        if arch_pattern.search(content):
            content = arch_pattern.sub(new_arch + "\n\n", content)
        else:
            arch_pattern_fallback = re.compile(
                r"## Architecture Visualization\s*\n.*?(?=\n# |\Z)", re.DOTALL
            )
            if arch_pattern_fallback.search(content):
                content = arch_pattern_fallback.sub(new_arch + "\n\n", content)
            else:
                content += f"\n\n{new_arch}\n"

        md_content = content
    else:
        md_content = f"""---
type: {entity_type}
title: "{entity_name}"
source_path: "{filepath}"
description: "{desc}"
tags: [{entity_type}]
last_verified_commit: "{git_sha}"
---

# {entity_name}

Source File: `{filepath}`

{desc}

## Architecture Visualization

{mermaid_diagram}
"""
    return filename, md_content


def prune_deleted_files(docs_dir, deleted_files):
    for f in deleted_files:
        # Need to find markdown files that have this source_path
        # Since we don't have a direct map from file -> md names easily without reading,
        # let's scan all md files.
        if not os.path.exists(docs_dir):
            continue
        for md_file in os.listdir(docs_dir):
            if not md_file.endswith(".md") or md_file == "index.md":
                continue

            md_path = os.path.join(docs_dir, md_file)
            with open(md_path, "r") as fp:
                content = fp.read()

            if f'source_path: "{f}"' in content:
                os.remove(md_path)
                print(f"Pruned deleted file doc: {md_path}")


def update_index(docs_dir):
    index_path = os.path.join(docs_dir, "index.md")

    if not os.path.exists(docs_dir):
        return

    md_files = [f for f in os.listdir(docs_dir) if f.endswith(".md") and f != "index.md"]
    md_files.sort()

    links = [f"- [[{f.replace('.md', '')}]]" for f in md_files]

    with open(index_path, "w") as f:
        f.write("# Knowledge Base Index\n\n")
        f.write("\n".join(links) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Update OKF Documentation")
    parser.add_argument("--commit", default="HEAD~1", help="Git commit range")
    parser.add_argument("--docs-dir", default=".knowledge", help="Output directory")
    parser.add_argument(
        "--full", action="store_true", help="Rebuild entire documentation from scratch"
    )
    args = parser.parse_args()

    os.makedirs(args.docs_dir, exist_ok=True)

    if args.full:
        modified_files, deleted_files = get_all_python_files()
    else:
        modified_files, deleted_files = get_modified_python_files(args.commit)

    print(f"Modified files to process: {modified_files}")
    print(f"Deleted files to process: {deleted_files}")

    git_sha = get_git_sha()

    if deleted_files:
        prune_deleted_files(args.docs_dir, deleted_files)

    for filepath in modified_files:
        entities = extract_classes_and_functions(filepath)
        for entity_type, entity_name, description, node in entities:
            filename = f"{entity_name}.md".lower().replace("_", "-")
            out_path = os.path.join(args.docs_dir, filename)

            existing_content = None
            if os.path.exists(out_path):
                with open(out_path, "r") as f:
                    existing_content = f.read()

            filename, md_content = generate_markdown(
                filepath, entity_type, entity_name, description, git_sha, node, existing_content
            )

            with open(out_path, "w") as f:
                f.write(md_content)
            print(f"Generated/Updated: {out_path}")

    update_index(args.docs_dir)


if __name__ == "__main__":
    main()
