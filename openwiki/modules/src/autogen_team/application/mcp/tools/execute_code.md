---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: execute_code"
source_path: "src/autogen_team/application/mcp/tools/execute_code.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.130063+00:00"
---

# Module Specification: execute_code

* **Source Reference:** `src/autogen_team/application/mcp/tools/execute_code.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to execute code.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `__future__.annotations`
- `json`
- `os`
- `py_compile`
- `shutil`
- `tempfile`
- `typing`
- `loguru.logger`
- `litellm`
- `autogen_team.core.security.safe_join`
- `autogen_team.infrastructure.services.mcp_service.MCPService`

**Exported Classes:**
- None

**Exported Functions:**
- `execute_code`

## 3. Architecture & Execution
### Internal Architecture
Not explicitly defined.

### Execution Flow
Not explicitly defined.

### Sequence Explanation
Not explicitly defined.

## 4. UML 2.0 Diagrams
### Class Diagram
```plantuml
@startuml
    ' No classes found in module
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [__future__.annotations] : imports
    [Module] --> [json] : imports
    [Module] --> [os] : imports
    [Module] --> [py_compile] : imports
    [Module] --> [shutil] : imports
    [Module] --> [tempfile] : imports
    [Module] --> [typing] : imports
    [Module] --> [loguru.logger] : imports
    [Module] --> [litellm] : imports
    [Module] --> [autogen_team.core.security.safe_join] : imports
    [Module] --> [autogen_team.infrastructure.services.mcp_service.MCPService] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `execute_code(task: T.Dict[str, T.Any], workspace_path: str)`
Generate code changes for a task and validate in sandbox.

Args:
    task: A task dict (from DAG) with id, name, description.
    workspace_path: Path to the workspace root.

Returns:
    A dict with files_changed list and status.

**Inputs:**
- `task`: T.Dict[str, T.Any]
- `workspace_path`: str

**Output:**
- Return Type: `T.Dict[str, T.Any]`
