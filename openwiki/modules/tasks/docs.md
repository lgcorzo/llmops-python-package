---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: docs"
source_path: "tasks/docs.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.173916+00:00"
---

# Module Specification: docs

* **Source Reference:** `tasks/docs.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to docs.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `invoke.context.Context`
- `invoke.tasks.task`
- `.cleans`

**Exported Classes:**
- None

**Exported Functions:**
- `serve`
- `api`
- `all`

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
    [Module] --> [invoke.context.Context] : imports
    [Module] --> [invoke.tasks.task] : imports
    [Module] --> [.cleans] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `serve(ctx: Context, format: str, port: int)`
Serve the API docs with pdoc.

**Inputs:**
- `ctx`: Context
- `format`: str
- `port`: int

**Output:**
- Return Type: `None`

### `api(ctx: Context, format: str, output_dir: str)`
Generate the API docs with pdoc.

**Inputs:**
- `ctx`: Context
- `format`: str
- `output_dir`: str

**Output:**
- Return Type: `None`

### `all(_: Context)`
Run all docs tasks.

**Inputs:**
- `_`: Context

**Output:**
- Return Type: `None`
