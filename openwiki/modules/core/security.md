---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Core Security"
source_path: "src/autogen_team/core/security.py"
description: "Path traversal prevention utility for the autogen_team system."
tags: ["core", "security", "path-traversal", "safe-join"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Module Specification: Core Security

* **Source Reference:** `src/autogen_team/core/security.py` (Lines: L1-L27)
* **Downstream Consumers:** [[Modules/Infrastructure/Services]] (`SandboxService.upload_artifact`), MCP `run_tests` tool

## 1. Architectural Role & Responsibilities

The security module provides critical path traversal prevention for the shared kernel. The `safe_join()` function is used wherever user-controlled or sandbox-controlled file paths interact with the host filesystem.

## 2. Function Specification

### `safe_join(base: str, *paths: str) -> str` (`src/autogen_team/core/security.py:L6-L27`)

Safely join paths, ensuring the result is within the base directory. Resolves symlinks via `os.path.realpath()` before validation.

- **Inputs:**
  - `base` (`str`): The base directory.
  - `*paths` (`str`): Paths to join.
- **Outputs:** `str`: The joined path.
- **Raises:** `ValueError`: If the resolved path is outside the base directory.

### Security Algorithm

```mermaid
flowchart TD
    A["Input: base, *paths"] --> B["os.path.realpath(base)"]
    B --> C["os.path.realpath(os.path.join(base_dir, *paths))"]
    C --> D{"os.path.commonpath == base_dir?"}
    D -->|Yes| E["Return final_path ✅"]
    D -->|No| F["Raise ValueError ❌ Path traversal detected"]
```
