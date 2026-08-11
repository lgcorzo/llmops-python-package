---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_mcp_service"
source_path: "tests/infrastructure/services/test_mcp_service.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.253796+00:00"
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
    [Module] --> [pytest] : imports
    [Module] --> [httpx] : imports
    [Module] --> [unittest.mock.MagicMock] : imports
    [Module] --> [unittest.mock.patch] : imports
    [Module] --> [autogen_team.infrastructure.services.mcp_service.MCPService] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `mcp_service()`
Fixture to provide an MCPService instance with default config.

**Inputs:**
- None

**Output:**
- Return Type: `MCPService`

### `test_mcp_service_start(mcp_service: MCPService)`
Test MCPService.start initializes clients and config.

**Inputs:**
- `mcp_service`: MCPService

**Output:**
- Return Type: `None`

### `test_mcp_service_load_prompts_not_found()`
Test _load_prompts when file doesn't exist (line 60).

**Inputs:**
- None

**Output:**
- Return Type: `None`

### `test_mcp_service_get_prompt_lazy_load(mcp_service: MCPService)`
Test get_prompt triggers lazy loading.

**Inputs:**
- `mcp_service`: MCPService

**Output:**
- Return Type: `None`

### `test_mcp_service_stop(mcp_service: MCPService)`
Test MCPService.stop (lines 72-74).

**Inputs:**
- `mcp_service`: MCPService

**Output:**
- Return Type: `None`

### `test_mcp_service_r2r_client_property(mcp_service: MCPService)`
Test r2r_client property auto-starts (lines 79-83).

**Inputs:**
- `mcp_service`: MCPService

**Output:**
- Return Type: `None`

### `test_mcp_service_r2r_client_failure()`
Test r2r_client property raises error if start fails (line 82).

**Inputs:**
- None

**Output:**
- Return Type: `None`
