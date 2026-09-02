---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_agents"
source_path: "tests/application/agents/test_agents.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-09-02T05:14:17.192169+00:00"
---

# Module Specification: test_agents

* **Source Reference:** `tests/application/agents/test_agents.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to test agents.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `pytest`
- `typing`
- `typing.Any`
- `unittest.mock.MagicMock`
- `autogen_team.application.agents.coder_agent.CoderAgent`
- `autogen_team.application.agents.planner_agent.PlannerAgent`
- `autogen_team.application.agents.reviewer_agent.ReviewerAgent`
- `autogen_team.application.agents.tester_agent.TesterAgent`

**Exported Classes:**
- None

**Exported Functions:**
- `mock_mcp_client`
- `test_coder_agent_execute_task`
- `test_planner_agent_create_plan`
- `test_reviewer_agent_review_changes`
- `test_tester_agent_run_tests`

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
        package "application" {
            package "agents" {
                [test_agents.py]
            }
        }
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    mock_mcp_client -> cast : call
    mock_mcp_client -> MagicMock : call
    mock_mcp_client -> patch : call
    mock_mcp_client -> AsyncMock : call
    test_coder_agent_execute_task -> assert_called_once : call
    test_coder_agent_execute_task -> assert_called_with : call
    test_coder_agent_execute_task -> CoderAgent : call
    test_coder_agent_execute_task -> execute_task : call
    test_planner_agent_create_plan -> PlannerAgent : call
    test_planner_agent_create_plan -> assert_called_with : call
    test_planner_agent_create_plan -> create_plan : call
    test_reviewer_agent_review_changes -> assert_called_with : call
    test_reviewer_agent_review_changes -> ReviewerAgent : call
    test_reviewer_agent_review_changes -> review_changes : call
    test_tester_agent_run_tests -> run_tests : call
    test_tester_agent_run_tests -> assert_called_with : call
    test_tester_agent_run_tests -> TesterAgent : call
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Infrastructure/Other" {
        [test_agents.py]
    }
    [test_agents.py] --> [pytest]
    [test_agents.py] --> [typing]
    [test_agents.py] --> [typing.Any]
    [test_agents.py] --> [unittest.mock.MagicMock]
    [test_agents.py] --> [autogen_team.application.agents.coder_agent.CoderAgent]
    [test_agents.py] --> [autogen_team.application.agents.planner_agent.PlannerAgent]
    [test_agents.py] --> [autogen_team.application.agents.reviewer_agent.ReviewerAgent]
    [test_agents.py] --> [autogen_team.application.agents.tester_agent.TesterAgent]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [pytest] : imports
    [Module] --> [typing] : imports
    [Module] --> [typing.Any] : imports
    [Module] --> [unittest.mock.MagicMock] : imports
    [Module] --> [autogen_team.application.agents.coder_agent.CoderAgent] : imports
    [Module] --> [autogen_team.application.agents.planner_agent.PlannerAgent] : imports
    [Module] --> [autogen_team.application.agents.reviewer_agent.ReviewerAgent] : imports
    [Module] --> [autogen_team.application.agents.tester_agent.TesterAgent] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `mock_mcp_client(mocker: Any) -> MagicMock` (Public)
**Description:** Executes the mock mcp client operation.

**Inputs:**
- `mocker`
  - type: Any
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `MagicMock`
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
result = mock_mcp_client(...)
```

### `test_coder_agent_execute_task(mock_mcp_client: MagicMock) -> None` (Public)
**Description:** Executes the test coder agent execute task operation.

**Inputs:**
- `mock_mcp_client`
  - type: MagicMock
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
result = test_coder_agent_execute_task(...)
```

### `test_planner_agent_create_plan(mock_mcp_client: MagicMock) -> None` (Public)
**Description:** Executes the test planner agent create plan operation.

**Inputs:**
- `mock_mcp_client`
  - type: MagicMock
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
result = test_planner_agent_create_plan(...)
```

### `test_reviewer_agent_review_changes(mock_mcp_client: MagicMock) -> None` (Public)
**Description:** Executes the test reviewer agent review changes operation.

**Inputs:**
- `mock_mcp_client`
  - type: MagicMock
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
result = test_reviewer_agent_review_changes(...)
```

### `test_tester_agent_run_tests(mock_mcp_client: MagicMock) -> None` (Public)
**Description:** Executes the test tester agent run tests operation.

**Inputs:**
- `mock_mcp_client`
  - type: MagicMock
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
result = test_tester_agent_run_tests(...)
```

## 7. Call Graph
```plantuml
@startuml
[test_agents] --> [PlannerAgent] : calls
[test_agents] --> [AsyncMock] : calls
[test_agents] --> [TesterAgent] : calls
[test_agents] --> [cast] : calls
[test_agents] --> [patch] : calls
[test_agents] --> [review_changes] : calls
[test_agents] --> [execute_task] : calls
[test_agents] --> [MagicMock] : calls
[test_agents] --> [assert_called_once] : calls
[test_agents] --> [CoderAgent] : calls
[test_agents] --> [ReviewerAgent] : calls
[test_agents] --> [run_tests] : calls
[test_agents] --> [assert_called_with] : calls
[test_agents] --> [create_plan] : calls
@enduml
```

## 8. Cross References
- **Dependencies:** [Dependencies](../../../../dependencies/index.md)
- **Used by:** None
- **Calls:** PlannerAgent, AsyncMock, TesterAgent, cast, patch, review_changes, execute_task, MagicMock, assert_called_once, CoderAgent, ReviewerAgent, run_tests, assert_called_with, create_plan
- **Called from:** None
- **Related classes:** [Classes](../../../../classes/index.md)
- **Related diagrams:** [Diagrams](../../../../diagrams/index.md)
