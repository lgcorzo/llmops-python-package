import os
import ast

def generate_cross_refs(filepath, imports, classes):
    lines = []
    lines.append("## 7. Cross References")

    # Parent module
    dirname = os.path.dirname(filepath)
    if dirname and dirname != ".":
        parent = os.path.basename(dirname)
        lines.append(f"- Parent module: `{parent}`")
    else:
        lines.append("- Parent module: Not explicitly defined.")

    lines.append("- Child modules: Not explicitly defined.")

    if imports:
        lines.append("- Dependencies:")
        for imp in imports:
            lines.append(f"  - `{imp}`")
    else:
        lines.append("- Dependencies: Not explicitly defined.")

    lines.append("- Used by: Not explicitly defined.")
    lines.append("- Calls: Not explicitly defined.")
    lines.append("- Called from: Not explicitly defined.")

    if classes:
        lines.append("- Related classes:")
        for cls in classes:
            lines.append(f"  - `{cls.name}`")
    else:
        lines.append("- Related classes: Not explicitly defined.")

    lines.append("- Related interfaces: Not explicitly defined.")
    lines.append("- Related diagrams:")
    lines.append("  - [Class Diagram](#class-diagram)")
    lines.append("  - [Dependency Graph](#dependency-graph)")
    lines.append("  - [Call Graph](#call-graph)")
    lines.append("")
    return "\n".join(lines)

class MockClass:
    def __init__(self, name):
        self.name = name

print(generate_cross_refs("src/models.py", ["os", "sys"], [MockClass("User"), MockClass("Product")]))
