---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: checks"
source_path: "tasks/checks.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-06T06:46:33.020927+00:00"
---

# Module Specification: checks

* **Source Reference:** `tasks/checks.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to checks.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Manage and execute operations for checks.

**Main Workflow:**
- Initialize components and process requests for checks.

## 2. Dependencies
**Imports:**
- `invoke.context.Context`
- `invoke.tasks.task`

**Exported Classes:**
- None

**Exported Functions:**
- `poetry`
- `format`
- `type`
- `code`
- `test`
- `security`
- `coverage`
- `all`

## 3. Architecture & Execution
### Internal Architecture
Follows standard modular design, encapsulating state and behavior within defined classes and functions.

### Execution Flow
Sequential execution of defined functions and class methods.

### Sequence Explanation
Clients instantiate classes or call functions, which execute business logic and return results.

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
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `poetry(ctx: Context)`
Check poetry config files.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `format(ctx: Context)`
Check the formats with ruff.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `type(ctx: Context)`
Check the types with mypy.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `code(ctx: Context)`
Check the codes with ruff.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `test(ctx: Context)`
Check the tests with pytest.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `security(ctx: Context)`
Check the security with bandit.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `coverage(ctx: Context)`
Check the coverage with coverage.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `all(_: Context)`
Run all check tasks.

**Inputs:**
- `_`: Context

**Output:**
- Return Type: `None`
