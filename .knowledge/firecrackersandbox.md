---
type: class
title: "FirecrackerSandbox"
source_path: "src/autogen_team/application/mcp/tools/run_tests.py"
description: "Firecracker-based sandbox using SandboxService."
tags: [class]
last_verified_commit: "dc137c3"
---

# FirecrackerSandbox

Source File: `src/autogen_team/application/mcp/tools/run_tests.py`

Firecracker-based sandbox using SandboxService.

## Architecture Visualization

```mermaid
classDiagram
    class FirecrackerSandbox {
        +service
        -__init__(sandbox_service)
        +run_tests(workspace_dir, timeout)
    }
```
