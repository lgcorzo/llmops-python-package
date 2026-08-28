---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: autonomous_mission"
source_path: "src/autogen_team/application/workflows/autonomous_mission.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-28T06:32:33.103489+00:00"
---

# Module Specification: autonomous_mission

* **Source Reference:** `src/autogen_team/application/workflows/autonomous_mission.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to autonomous mission.

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
- `typing.List`
- `autogen_team.application.agents.coder_agent.CoderAgent`
- `autogen_team.application.agents.documentation_agent.DocumentationAgent`
- `autogen_team.application.agents.planner_agent.PlannerAgent`
- `autogen_team.application.agents.reviewer_agent.ReviewerAgent`
- `autogen_team.application.agents.tester_agent.TesterAgent`
- `autogen_team.infrastructure.services.hatchet_service.HatchetService`
- `hatchet_sdk.Context`
- `pydantic.BaseModel`

**Exported Classes:**
- `MissionInput`
- `TaskInput`
- `MissionOutput`

**Exported Functions:**
- `execute_coding_task`
- `plan`
- `fan_out_tasks`
- `aggregate_and_review`
- `document_mission`

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
    class MissionInput {
    }
    class TaskInput {
    }
    class MissionOutput {
    }
@enduml
```

### Package Diagram
```plantuml
@startuml
    package "src" {
        package "autogen_team" {
            package "application" {
                package "workflows" {
                    [autonomous_mission.py]
                }
            }
        }
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    execute_coding_task -> CoderAgent : call
    execute_coding_task -> execute_task : call
    execute_coding_task -> task : call
    execute_coding_task -> log : call
    plan -> PlannerAgent : call
    plan -> create_plan : call
    plan -> task : call
    plan -> log : call
    fan_out_tasks -> aio_run_many : call
    fan_out_tasks -> len : call
    fan_out_tasks -> get : call
    fan_out_tasks -> TaskInput : call
    fan_out_tasks -> task : call
    fan_out_tasks -> log : call
    fan_out_tasks -> task_output : call
    fan_out_tasks -> create_bulk_run_item : call
    aggregate_and_review -> get : call
    aggregate_and_review -> task : call
    aggregate_and_review -> extend : call
    aggregate_and_review -> review_changes : call
    aggregate_and_review -> MissionOutput : call
    aggregate_and_review -> join : call
    aggregate_and_review -> log : call
    aggregate_and_review -> task_output : call
    aggregate_and_review -> run_tests : call
    aggregate_and_review -> TesterAgent : call
    aggregate_and_review -> ReviewerAgent : call
    document_mission -> log : call
    document_mission -> get : call
    document_mission -> task : call
    document_mission -> extend : call
    document_mission -> MissionOutput : call
    document_mission -> generate_docs : call
    document_mission -> DocumentationAgent : call
    document_mission -> task_output : call
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Infrastructure/Other" {
        [autonomous_mission.py]
    }
    [autonomous_mission.py] --> [typing.Any]
    [autonomous_mission.py] --> [typing.Dict]
    [autonomous_mission.py] --> [typing.List]
    [autonomous_mission.py] --> [autogen_team.application.agents.coder_agent.CoderAgent]
    [autonomous_mission.py] --> [autogen_team.application.agents.documentation_agent.DocumentationAgent]
    [autonomous_mission.py] --> [autogen_team.application.agents.planner_agent.PlannerAgent]
    [autonomous_mission.py] --> [autogen_team.application.agents.reviewer_agent.ReviewerAgent]
    [autonomous_mission.py] --> [autogen_team.application.agents.tester_agent.TesterAgent]
    [autonomous_mission.py] --> [autogen_team.infrastructure.services.hatchet_service.HatchetService]
    [autonomous_mission.py] --> [hatchet_sdk.Context]
    [autonomous_mission.py] --> [pydantic.BaseModel]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [typing.Any] : imports
    [Module] --> [typing.Dict] : imports
    [Module] --> [typing.List] : imports
    [Module] --> [autogen_team.application.agents.coder_agent.CoderAgent] : imports
    [Module] --> [autogen_team.application.agents.documentation_agent.DocumentationAgent] : imports
    [Module] --> [autogen_team.application.agents.planner_agent.PlannerAgent] : imports
    [Module] --> [autogen_team.application.agents.reviewer_agent.ReviewerAgent] : imports
    [Module] --> [autogen_team.application.agents.tester_agent.TesterAgent] : imports
    [Module] --> [autogen_team.infrastructure.services.hatchet_service.HatchetService] : imports
    [Module] --> [hatchet_sdk.Context] : imports
    [Module] --> [pydantic.BaseModel] : imports
@enduml
```

## 5. Class & Method Specifications
### `MissionInput` ([`src/autogen_team/application/workflows/autonomous_mission.py`](/src/autogen_team/application/workflows/autonomous_mission.py))
#### Overview
Input for the top-level autonomous-mission workflow.

#### Attributes
- None found.

#### Methods
### `TaskInput` ([`src/autogen_team/application/workflows/autonomous_mission.py`](/src/autogen_team/application/workflows/autonomous_mission.py))
#### Overview
Input for a single child coding-task workflow.

#### Attributes
- None found.

#### Methods
### `MissionOutput` ([`src/autogen_team/application/workflows/autonomous_mission.py`](/src/autogen_team/application/workflows/autonomous_mission.py))
#### Overview
Final output of the autonomous-mission workflow.

#### Attributes
- None found.

#### Methods
## 6. Module Functions
### `execute_coding_task(task_input: TaskInput, context: Context) -> Dict[str, Any]` (Public)
**Description:** Run the Coder Agent on a single task inside a child workflow.

**Inputs:**
- `task_input`
  - type: TaskInput
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `context`
  - type: Context
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `Dict[str, Any]`
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
result = execute_coding_task(..., ...)
```

### `plan(mission_input: MissionInput, context: Context) -> Dict[str, Any]` (Public)
**Description:** Step 1: Planner Agent analyses the goal and creates a task DAG.

**Inputs:**
- `mission_input`
  - type: MissionInput
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `context`
  - type: Context
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `Dict[str, Any]`
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
result = plan(..., ...)
```

### `fan_out_tasks(mission_input: MissionInput, context: Context) -> Dict[str, Any]` (Public)
**Description:** Step 2: Spawn parallel child workflows for each coding task.

Uses ``develop_task_workflow.aio_run_many`` for true parallel
fan-out execution across the Hatchet worker pool.

**Inputs:**
- `mission_input`
  - type: MissionInput
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `context`
  - type: Context
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `Dict[str, Any]`
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
result = fan_out_tasks(..., ...)
```

### `aggregate_and_review(mission_input: MissionInput, context: Context) -> MissionOutput` (Public)
**Description:** Step 3: Aggregate child results, run tests, and perform security review.

**Inputs:**
- `mission_input`
  - type: MissionInput
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `context`
  - type: Context
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `MissionOutput`
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
result = aggregate_and_review(..., ...)
```

### `document_mission(mission_input: MissionInput, context: Context) -> MissionOutput` (Public)
**Description:** Step 4: Generate documentation and diagrams for the mission.

**Inputs:**
- `mission_input`
  - type: MissionInput
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `context`
  - type: Context
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `MissionOutput`
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
result = document_mission(..., ...)
```

## 7. Call Graph
```plantuml
@startuml
[autonomous_mission] --> [HatchetService] : calls
[autonomous_mission] --> [execute_task] : calls
[autonomous_mission] --> [workflow] : calls
[autonomous_mission] --> [ReviewerAgent] : calls
[autonomous_mission] --> [aio_run_many] : calls
[autonomous_mission] --> [len] : calls
[autonomous_mission] --> [log] : calls
[autonomous_mission] --> [get] : calls
[autonomous_mission] --> [task] : calls
[autonomous_mission] --> [create_plan] : calls
[autonomous_mission] --> [join] : calls
[autonomous_mission] --> [create_bulk_run_item] : calls
[autonomous_mission] --> [TesterAgent] : calls
[autonomous_mission] --> [CoderAgent] : calls
[autonomous_mission] --> [TaskInput] : calls
[autonomous_mission] --> [review_changes] : calls
[autonomous_mission] --> [MissionOutput] : calls
[autonomous_mission] --> [DocumentationAgent] : calls
[autonomous_mission] --> [task_output] : calls
[autonomous_mission] --> [run_tests] : calls
[autonomous_mission] --> [PlannerAgent] : calls
[autonomous_mission] --> [generate_docs] : calls
[autonomous_mission] --> [extend] : calls
@enduml
```

## 8. Cross References
- **Dependencies:** [Dependencies](../../../../../dependencies/index.md)
- **Used by:** ../../../../tests/application/workflows/test_autonomous_mission.md
- **Calls:** HatchetService, execute_task, workflow, ReviewerAgent, aio_run_many, len, log, get, task, create_plan, join, create_bulk_run_item, TesterAgent, CoderAgent, TaskInput, review_changes, MissionOutput, DocumentationAgent, task_output, run_tests, PlannerAgent, generate_docs, extend
- **Called from:** None
- **Related classes:** [Classes](../../../../../classes/index.md)
- **Related diagrams:** [Diagrams](../../../../../diagrams/index.md)
