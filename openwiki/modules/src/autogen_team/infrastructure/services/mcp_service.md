---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: mcp_service"
source_path: "src/autogen_team/infrastructure/services/mcp_service.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-27T07:00:19.308195+00:00"
---

# Module Specification: mcp_service

* **Source Reference:** `src/autogen_team/infrastructure/services/mcp_service.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to mcp service.

**Architecture Layer:**
- Services

**Responsibilities:**
- Manages operations and logic for mcp service.

**Main Workflow:**
- Executes the primary flow defined by mcp service functions and classes.

## 2. Dependencies
**Imports:**
- `__future__.annotations`
- `typing`
- `typing.ClassVar`
- `httpx`
- `litellm`
- `pydantic.Field`
- `autogen_team.infrastructure.io.osvariables.Env`
- `logger_service.Service`

**Exported Classes:**
- `MCPService`

**Exported Functions:**
- None

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
    class MCPService {
        +start() : None
        +_load_prompts() : None
        +get_prompt() : str
        +stop() : None
        +r2r_client() : httpx.AsyncClient
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    ' No functions for sequence
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Services" {
        [mcp_service.py]
    }
    [mcp_service.py] --> [__future__.annotations]
    [mcp_service.py] --> [typing]
    [mcp_service.py] --> [typing.ClassVar]
    [mcp_service.py] --> [httpx]
    [mcp_service.py] --> [litellm]
    [mcp_service.py] --> [pydantic.Field]
    [mcp_service.py] --> [autogen_team.infrastructure.io.osvariables.Env]
    [mcp_service.py] --> [logger_service.Service]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [__future__.annotations] : imports
    [Module] --> [typing] : imports
    [Module] --> [typing.ClassVar] : imports
    [Module] --> [httpx] : imports
    [Module] --> [litellm] : imports
    [Module] --> [pydantic.Field] : imports
    [Module] --> [autogen_team.infrastructure.io.osvariables.Env] : imports
    [Module] --> [logger_service.Service] : imports
@enduml
```

## 5. Class & Method Specifications
### `MCPService` ([`src/autogen_team/infrastructure/services/mcp_service.py`](/src/autogen_team/infrastructure/services/mcp_service.py))
#### Overview
Service for MCP server lifecycle and backend clients.

Manages LiteLLM and R2R HTTP client initialization, providing
a single point of access for all MCP tool backends.

Parameters:
    litellm_api_base (str): LiteLLM API base URL.
    litellm_api_key (str): LiteLLM API key.
    litellm_model (str): Default LiteLLM model identifier.
    r2r_base_url (str): R2R RAG API base URL.

#### Attributes
- None found.

#### Methods
##### `start(self) -> None` (Public)
**Description:** Initialize LiteLLM configuration and R2R HTTP client.

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Returns the result of start.
- possible null values: Yes, if None allows it.
- exceptions: Standard execution exceptions.

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
result = MCPService.start()
```

##### `_load_prompts(self) -> None` (Private)
**Purpose:** Load prompts from YAML file.

**Parameters:**
- None

**Return value:**
- `None`

##### `get_prompt(self, tool_name: str, key: str) -> str` (Public)
**Description:** Get a specific prompt for a tool and key.

**Inputs:**
- `tool_name`
  - type: str
  - meaning: Represents the tool name parameter.
  - valid values: Any valid str.
  - optional?: False
  - default value: None
- `key`
  - type: str
  - meaning: Represents the key parameter.
  - valid values: Any valid str.
  - optional?: True
  - default value: 'system'

**Output:**
- return type: `str`
- semantic meaning: Returns the result of get prompt.
- possible null values: Yes, if str allows it.
- exceptions: Standard execution exceptions.

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
result = MCPService.get_prompt(..., ...)
```

##### `stop(self) -> None` (Public)
**Description:** Stop the MCP service and close HTTP clients.

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Returns the result of stop.
- possible null values: Yes, if None allows it.
- exceptions: Standard execution exceptions.

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
result = MCPService.stop()
```

##### `r2r_client(self) -> httpx.AsyncClient` (Public)
**Description:** Return the R2R async HTTP client.

**Inputs:**
- None

**Output:**
- return type: `httpx.AsyncClient`
- semantic meaning: Returns the result of r2r client.
- possible null values: Yes, if httpx.AsyncClient allows it.
- exceptions: Standard execution exceptions.

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
result = MCPService.r2r_client()
```

## 6. Module Functions
## 7. Call Graph
```plantuml
@startuml
[mcp_service] --> [str] : calls
[mcp_service] --> [_load_prompts] : calls
[mcp_service] --> [Env] : calls
[mcp_service] --> [Field] : calls
[mcp_service] --> [parse_file] : calls
[mcp_service] --> [cast] : calls
[mcp_service] --> [get] : calls
[mcp_service] --> [start] : calls
[mcp_service] --> [to_object] : calls
[mcp_service] --> [RuntimeError] : calls
[mcp_service] --> [AsyncClient] : calls
[mcp_service] --> [Timeout] : calls
[mcp_service] --> [exists] : calls
@enduml
```

## 8. Cross References
- **Parent module:** __init__.md
- **Child modules:** None
- **Dependencies:** `typing.ClassVar`, `autogen_team.infrastructure.io.osvariables.Env`, `__future__.annotations`, `typing`, `pydantic.Field`, `logger_service.Service`, `litellm`, `httpx`
- **Used by:** ../../application/mcp/tools/generate_mission_docs.md, ../../../../tests/infrastructure/services/test_mcp_service.md, ../../application/mcp/tools/plan_mission.md, ../../application/mcp/tools/execute_code.md, ../../application/mcp/tools/security_review.md
- **Calls:** str, _load_prompts, Env, Field, parse_file, cast, get, start, to_object, RuntimeError, AsyncClient, Timeout, exists
- **Called from:** None
- **Related classes:** [Classes](../../../../../classes/index.md)
- **Related interfaces:** Not explicitly defined.
- **Related diagrams:** [Diagrams](../../../../../diagrams/index.md)
