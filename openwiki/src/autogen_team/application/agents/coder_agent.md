---
title: src/autogen_team/application/agents/coder_agent.py
source: src/autogen_team/application/agents/coder_agent.py
---

# Document: src/autogen_team/application/agents/coder_agent.py

## Module Overview

### Purpose
Provides functionality for `coder_agent`.

### Responsibilities
Handles operations and definitions related to `coder_agent`.

### Main Workflow
Execution flow defined by the functions and classes in the module.

### Dependencies
- `typing.Any`
- `typing.Dict`
- `typing.cast`
- `autogen_team.infrastructure.client.mcp_client.MCPClient`

## Public API

### Exported Classes
- `CoderAgent`

### Exported Functions
None

## Class `CoderAgent`

### Overview

Agent responsible for executing coding tasks.
Uses the MCP 'execute_code' tool.

### Constructor

No description provided.

**Parameters:**

### Public Method `execute_task`

#### Description
No description provided.

#### Inputs
- `task` (Dict[(str, Any)]): semantic meaning. Required.

#### Output
- Return type: `Dict[(str, Any)]`
- Semantic meaning: Result of the operation.

#### Side Effects
May update internal state or external services.

#### Complexity
- Time Complexity: O(1) mostly.
- Space Complexity: O(1) mostly.

#### Example
```python
# Example usage of execute_task
instance.execute_task()
```

## UML Diagram

```plantuml
@startuml
class CoderAgent {
  + __init__()
  + execute_task()
}
@enduml
```

