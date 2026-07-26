---
type: class
title: "SandboxBackend"
source_path: "src/autogen_team/application/mcp/tools/run_tests.py"
description: "Abstract sandbox backend for running tests.  Provides an interface for future Firecracker MicroVM integration."
tags: [class]
last_verified_commit: "dc137c3"
---

# SandboxBackend

Source File: `src/autogen_team/application/mcp/tools/run_tests.py`

Abstract sandbox backend for running tests.  Provides an interface for future Firecracker MicroVM integration.

## Architecture Visualization

```mermaid
classDiagram
    class SandboxBackend {
        +run_tests(workspace_dir, timeout)
    }
```
