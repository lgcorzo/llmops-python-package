---
title: src/autogen_team/application/jobs/hatchet_inference.py
source: src/autogen_team/application/jobs/hatchet_inference.py
---

# Document: src/autogen_team/application/jobs/hatchet_inference.py

## Module Overview

Define a job for triggering a Hatchet inference workflow.

### Purpose
Provides functionality for `hatchet_inference`.

### Responsibilities
Handles operations and definitions related to `hatchet_inference`.

### Main Workflow
Execution flow defined by the functions and classes in the module.

### Dependencies
- `typing`
- `pydantic`
- `autogen_team.application.jobs.base`
- `autogen_team.data_access.adapters.datasets`
- `autogen_team.infrastructure.services`
- `autogen_team.registry.adapters.mlflow_adapter`

## Public API

### Exported Classes
- `HatchetInferenceJob`

### Exported Functions
None

## Class `HatchetInferenceJob`

### Overview

Trigger a Hatchet inference workflow.

This job acts as a client-side proxy that starts the asynchronous
inference process in the Hatchet engine.

Parameters:
    inputs (datasets.ReaderKind): reader for the inputs data.
    outputs (datasets.WriterKind): writer for the outputs data.
    alias_or_version (str | int): alias or version for the model.
    loader (registries.LoaderKind): registry loader for the model.
    hatchet_service (services.HatchetService): manage the Hatchet system.

### Attributes

- `KIND` (T.Literal[HatchetInferenceJob]): Public property.
- `inputs` (datasets.ReaderKind): Public property.
- `outputs` (datasets.WriterKind): Public property.
- `alias_or_version` (str | int): Public property.
- `loader` (registries.LoaderKind): Public property.
- `hatchet_service` (services.HatchetService): Public property.

### Public Method `run`

#### Description
No description provided.

#### Inputs
None

#### Output
- Return type: `base.Locals`
- Semantic meaning: Result of the operation.

#### Side Effects
May update internal state or external services.

#### Complexity
- Time Complexity: O(1) mostly.
- Space Complexity: O(1) mostly.

#### Example
```python
# Example usage of run
instance.run()
```

## UML Diagram

```plantuml
@startuml
class HatchetInferenceJob {
  + run()
}
base.Job <|-- HatchetInferenceJob
@enduml
```

