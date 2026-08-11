---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: projects"
source_path: "tasks/projects.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.190770+00:00"
---

# Module Specification: projects

* **Source Reference:** `tasks/projects.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to projects.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `json`
- `invoke.context.Context`
- `invoke.tasks.call`
- `invoke.tasks.task`

**Exported Classes:**
- None

**Exported Functions:**
- `requirements`
- `environment`
- `run`
- `mcp`
- `kafka`
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
    [Module] --> [json] : imports
    [Module] --> [invoke.context.Context] : imports
    [Module] --> [invoke.tasks.call] : imports
    [Module] --> [invoke.tasks.task] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `requirements(ctx: Context)`
Export the project requirements file.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `environment(ctx: Context)`
Export the project environment file.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `run(ctx: Context, job: str)`
Run an mlflow project from the MLproject file.

**Inputs:**
- `ctx`: Context
- `job`: str

**Output:**
- Return Type: `None`

### `mcp(ctx: Context, prompts: str | None)`
Run the MCP server.

Args:
    prompts (str, optional): Path to the prompts YAML config.

**Inputs:**
- `ctx`: Context
- `prompts`: str | None

**Output:**
- Return Type: `None`

### `kafka(ctx: Context)`
Run the Kafka inference service.

**Inputs:**
- `ctx`: Context

**Output:**
- Return Type: `None`

### `all(_: Context)`
Run all project tasks.

**Inputs:**
- `_`: Context

**Output:**
- Return Type: `None`
