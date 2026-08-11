---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: mcp_service"
source_path: "src/autogen_team/infrastructure/services/mcp_service.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.022951+00:00"
---

# Module Specification: mcp_service

* **Source Reference:** `src/autogen_team/infrastructure/services/mcp_service.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to mcp service.

**Architecture Layer:**
- Services

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

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
    class MCPService {
        +start() : None
        +_load_prompts() : None
        +get_prompt() : str
        +stop() : None
        +r2r_client() : httpx.AsyncClient
    }
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
- Return Type: `None`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

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
- `tool_name`: str
- `key`: str

**Output:**
- Return Type: `str`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

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
- Return Type: `None`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

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
- Return Type: `httpx.AsyncClient`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = MCPService.r2r_client()
```

## 6. Module Functions