---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Run Tests"
source_path: "src/autogen_team/application/mcp/tools/run_tests.py"
description: "Exhaustive functional summary for Run Tests."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Run Tests

* **Source Reference:** `src/autogen_team/application/mcp/tools/run_tests.py`

## UML Diagrams

```mermaid
classDiagram
    class FirecrackerSandbox {
        +service
        +run_tests(workspace_dir: str, timeout: int): T.Dict[str, T.Any]
    }
    class SandboxBackend {
        +run_tests(workspace_dir: str, timeout: int): T.Dict[str, T.Any]
    }
    class SubprocessSandbox {
        +run_tests(workspace_dir: str, timeout: int): T.Dict[str, T.Any]
    }
    SandboxBackend <|-- FirecrackerSandbox
    SandboxBackend <|-- SubprocessSandbox
    FirecrackerSandbox --> SandboxService
```
