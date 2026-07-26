import argparse
import ast
import os
import subprocess
import json


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


def generate_markdown(filepath, entity_type, entity_name, description, git_sha, node):
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
    args = parser.parse_args()

    os.makedirs(args.docs_dir, exist_ok=True)

    modified_files, deleted_files = get_modified_python_files(args.commit)
    print(f"Modified files to process: {modified_files}")
    print(f"Deleted files to process: {deleted_files}")

    git_sha = get_git_sha()

    if deleted_files:
        prune_deleted_files(args.docs_dir, deleted_files)

    for filepath in modified_files:
        entities = extract_classes_and_functions(filepath)
        for entity_type, entity_name, description, node in entities:
            filename, md_content = generate_markdown(
                filepath, entity_type, entity_name, description, git_sha, node
            )
            out_path = os.path.join(args.docs_dir, filename)

            with open(out_path, "w") as f:
                f.write(md_content)
            print(f"Generated/Updated: {out_path}")

    update_index(args.docs_dir)


if __name__ == "__main__":
    main()
