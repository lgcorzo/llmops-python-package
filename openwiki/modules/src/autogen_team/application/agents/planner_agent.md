---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: planner_agent"
source_path: "src/autogen_team/application/agents/planner_agent.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.101392+00:00"
---

# Module Specification: planner_agent

* **Source Reference:** `src/autogen_team/application/agents/planner_agent.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to planner agent.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `typing.Any`
- `typing.Dict`
- `typing.cast`
- `autogen_team.infrastructure.client.mcp_client.MCPClient`

**Exported Classes:**
- `PlannerAgent`

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
    class PlannerAgent {
        +__init__() : None
        +create_plan() : Dict[str, Any]
    }
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [typing.Any] : imports
    [Module] --> [typing.Dict] : imports
    [Module] --> [typing.cast] : imports
    [Module] --> [autogen_team.infrastructure.client.mcp_client.MCPClient] : imports
@enduml
```

## 5. Class & Method Specifications
### `PlannerAgent` ([`src/autogen_team/application/agents/planner_agent.py`](/src/autogen_team/application/agents/planner_agent.py))
#### Overview
Agent responsible for decomposing a high-level goal into a detailed plan.
Uses the MCP 'plan_mission' tool.

#### Constructor
**Initialization:** Initializes `PlannerAgent` with required dependencies and sets up initial internal state.

#### Attributes
- `client`

#### Methods
##### `__init__(self) -> None` (Public)
**Description:** No description provided.

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
instance = PlannerAgent()
result = instance.__init__()
```

##### `create_plan(self, goal: str, repository_path: str) -> Dict[str, Any]` (Public)
**Description:** Calls the `plan_mission` tool via MCP.

**Inputs:**
- `goal`: str
- `repository_path`: str

**Output:**
- Return Type: `Dict[str, Any]`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
instance = PlannerAgent()
result = instance.create_plan(..., ...)
```

## 6. Module Functions