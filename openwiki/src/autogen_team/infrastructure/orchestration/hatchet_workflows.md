---
title: src/autogen_team/infrastructure/orchestration/hatchet_workflows.py
source: src/autogen_team/infrastructure/orchestration/hatchet_workflows.py
---

# Document: src/autogen_team/infrastructure/orchestration/hatchet_workflows.py

## Module Overview

### Purpose
Provides functionality for `hatchet_workflows`.

### Responsibilities
Handles operations and definitions related to `hatchet_workflows`.

### Main Workflow
Execution flow defined by the functions and classes in the module.

### Dependencies
- `typing.Any`
- `autogen_team.application.jobs.inference`
- `autogen_team.infrastructure.services.HatchetService`
- `hatchet_sdk.Context`

## Public API

### Exported Classes
None

### Exported Functions
- `run_inference`

## Public Function `run_inference`

### Description
Run the inference job.

### Inputs
- `input` (Any): semantic meaning. Required.
- `context` (Context): semantic meaning. Required.

### Output
- Return type: `dict[(str, Any)]`
- Semantic meaning: Result of the operation.

### Side Effects
May update state or affect global resources.

### Complexity
- Time Complexity: O(1) mostly.
- Space Complexity: O(1) mostly.

### Example
```python
# Example usage of run_inference
run_inference()
```

## UML Diagram

```plantuml
@startuml
note "No classes in module" as N1
@enduml
```

