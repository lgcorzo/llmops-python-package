---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: retrieve_context"
source_path: "src/autogen_team/application/mcp/tools/retrieve_context.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.119995+00:00"
---

# Module Specification: retrieve_context

* **Source Reference:** `src/autogen_team/application/mcp/tools/retrieve_context.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to retrieve context.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `__future__.annotations`
- `typing`
- `loguru.logger`
- `httpx`
- `autogen_team.infrastructure.io.osvariables.Env`

**Exported Classes:**
- None

**Exported Functions:**
- `retrieve_context`

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
    [Module] --> [typing] : imports
    [Module] --> [loguru.logger] : imports
    [Module] --> [httpx] : imports
    [Module] --> [autogen_team.infrastructure.io.osvariables.Env] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `retrieve_context(query: str, collection_name: str)`
Query R2R RAG system for relevant codebase patterns via semantic search.

Args:
    query: Search query string.
    collection_name: Name of the R2R collection to search.

Returns:
    Dict with matching documents and graph context.

**Inputs:**
- `query`: str
- `collection_name`: str

**Output:**
- Return Type: `T.Dict[str, T.Any]`
