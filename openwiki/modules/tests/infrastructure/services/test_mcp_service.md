---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_mcp_service"
source_path: "tests/infrastructure/services/test_mcp_service.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-28T06:32:33.199560+00:00"
---

# Module Specification: test_mcp_service

* **Source Reference:** `tests/infrastructure/services/test_mcp_service.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to test mcp service.

**Architecture Layer:**
- Services

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `pytest`
- `httpx`
- `unittest.mock.MagicMock`
- `unittest.mock.patch`
- `autogen_team.infrastructure.services.mcp_service.MCPService`

**Exported Classes:**
- None

**Exported Functions:**
- `mcp_service`
- `test_mcp_service_start`
- `test_mcp_service_load_prompts_not_found`
- `test_mcp_service_get_prompt_lazy_load`
- `test_mcp_service_stop`
- `test_mcp_service_r2r_client_property`
- `test_mcp_service_r2r_client_failure`

**Exported Interfaces:**
- Not explicitly defined.

**Public API:**
- Not explicitly defined.

## 3. Architecture & Execution
### Internal Architecture
Not explicitly defined.

### Execution Flow
Not explicitly defined.

### Sequence Explanation
Not explicitly defined.

### Examples
Not explicitly defined.

## 4. UML 2.0 Diagrams
### Class Diagram
```plantuml
@startuml
    ' No classes found in module
@enduml
```

### Package Diagram
```plantuml
@startuml
    package "tests" {
        package "infrastructure" {
            package "services" {
                [test_mcp_service.py]
            }
        }
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    mcp_service -> object : call
    mcp_service -> MCPService : call
    mcp_service -> MagicMock : call
    test_mcp_service_start -> isinstance : call
    test_mcp_service_start -> start : call
    test_mcp_service_start -> patch : call
    test_mcp_service_load_prompts_not_found -> MCPService : call
    test_mcp_service_load_prompts_not_found -> _load_prompts : call
    test_mcp_service_get_prompt_lazy_load -> get_prompt : call
    test_mcp_service_get_prompt_lazy_load -> assert_called_once : call
    test_mcp_service_get_prompt_lazy_load -> MCPService : call
    test_mcp_service_get_prompt_lazy_load -> patch : call
    test_mcp_service_stop -> stop : call
    test_mcp_service_stop -> start : call
    test_mcp_service_r2r_client_property -> raises : call
    test_mcp_service_r2r_client_property -> assert_called_once : call
    test_mcp_service_r2r_client_property -> MCPService : call
    test_mcp_service_r2r_client_property -> patch : call
    test_mcp_service_r2r_client_failure -> raises : call
    test_mcp_service_r2r_client_failure -> MCPService : call
    test_mcp_service_r2r_client_failure -> patch : call
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Services" {
        [test_mcp_service.py]
    }
    [test_mcp_service.py] --> [pytest]
    [test_mcp_service.py] --> [httpx]
    [test_mcp_service.py] --> [unittest.mock.MagicMock]
    [test_mcp_service.py] --> [unittest.mock.patch]
    [test_mcp_service.py] --> [autogen_team.infrastructure.services.mcp_service.MCPService]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [pytest] : imports
    [Module] --> [httpx] : imports
    [Module] --> [unittest.mock.MagicMock] : imports
    [Module] --> [unittest.mock.patch] : imports
    [Module] --> [autogen_team.infrastructure.services.mcp_service.MCPService] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `mcp_service() -> MCPService` (Public)
**Description:** Fixture to provide an MCPService instance with default config.

**Inputs:**
- None

**Output:**
- return type: `MCPService`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = mcp_service()
```

### `test_mcp_service_start(mcp_service: MCPService) -> None` (Public)
**Description:** Test MCPService.start initializes clients and config.

**Inputs:**
- `mcp_service`
  - type: MCPService
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_mcp_service_start(...)
```

### `test_mcp_service_load_prompts_not_found() -> None` (Public)
**Description:** Test _load_prompts when file doesn't exist (line 60).

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_mcp_service_load_prompts_not_found()
```

### `test_mcp_service_get_prompt_lazy_load(mcp_service: MCPService) -> None` (Public)
**Description:** Test get_prompt triggers lazy loading.

**Inputs:**
- `mcp_service`
  - type: MCPService
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_mcp_service_get_prompt_lazy_load(...)
```

### `test_mcp_service_stop(mcp_service: MCPService) -> None` (Public)
**Description:** Test MCPService.stop (lines 72-74).

**Inputs:**
- `mcp_service`
  - type: MCPService
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_mcp_service_stop(...)
```

### `test_mcp_service_r2r_client_property(mcp_service: MCPService) -> None` (Public)
**Description:** Test r2r_client property auto-starts (lines 79-83).

**Inputs:**
- `mcp_service`
  - type: MCPService
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_mcp_service_r2r_client_property(...)
```

### `test_mcp_service_r2r_client_failure() -> None` (Public)
**Description:** Test r2r_client property raises error if start fails (line 82).

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_mcp_service_r2r_client_failure()
```

## 7. Call Graph
```plantuml
@startuml
[test_mcp_service] --> [object] : calls
[test_mcp_service] --> [isinstance] : calls
[test_mcp_service] --> [assert_called_once] : calls
[test_mcp_service] --> [raises] : calls
[test_mcp_service] --> [MagicMock] : calls
[test_mcp_service] --> [patch] : calls
[test_mcp_service] --> [get_prompt] : calls
[test_mcp_service] --> [stop] : calls
[test_mcp_service] --> [_load_prompts] : calls
[test_mcp_service] --> [start] : calls
[test_mcp_service] --> [MCPService] : calls
@enduml
```

## 8. Cross References
- **Dependencies:** [Dependencies](../../../../dependencies/index.md)
- **Used by:** None
- **Calls:** object, isinstance, assert_called_once, raises, MagicMock, patch, get_prompt, stop, _load_prompts, start, MCPService
- **Called from:** None
- **Related classes:** [Classes](../../../../classes/index.md)
- **Related diagrams:** [Diagrams](../../../../diagrams/index.md)
