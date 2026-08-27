---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: training"
source_path: "src/autogen_team/application/jobs/training.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-27T07:00:19.410282+00:00"
---

# Module Specification: training

* **Source Reference:** `src/autogen_team/application/jobs/training.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to training.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Manages operations and logic for training.

**Main Workflow:**
- Executes the primary flow defined by training functions and classes.

## 2. Dependencies
**Imports:**
- `typing`
- `mlflow`
- `pydantic`
- `autogen_team.application.jobs.base`
- `autogen_team.core.schemas`
- `autogen_team.data_access.adapters.datasets`
- `autogen_team.evaluation.metrics.metrics`
- `autogen_team.infrastructure.services`
- `autogen_team.infrastructure.utils.signers`
- `autogen_team.infrastructure.utils.splitters`
- `autogen_team.models.entities`
- `autogen_team.registry.adapters.mlflow_adapter`

**Exported Classes:**
- `TrainingJob`

**Exported Functions:**
- None

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
    class TrainingJob {
        +run() : base.Locals
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    ' No functions for sequence
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Infrastructure/Other" {
        [training.py]
    }
    [training.py] --> [typing]
    [training.py] --> [mlflow]
    [training.py] --> [pydantic]
    [training.py] --> [autogen_team.application.jobs.base]
    [training.py] --> [autogen_team.core.schemas]
    [training.py] --> [autogen_team.data_access.adapters.datasets]
    [training.py] --> [autogen_team.evaluation.metrics.metrics]
    [training.py] --> [autogen_team.infrastructure.services]
    [training.py] --> [autogen_team.infrastructure.utils.signers]
    [training.py] --> [autogen_team.infrastructure.utils.splitters]
    [training.py] --> [autogen_team.models.entities]
    [training.py] --> [autogen_team.registry.adapters.mlflow_adapter]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [typing] : imports
    [Module] --> [mlflow] : imports
    [Module] --> [pydantic] : imports
    [Module] --> [autogen_team.application.jobs.base] : imports
    [Module] --> [autogen_team.core.schemas] : imports
    [Module] --> [autogen_team.data_access.adapters.datasets] : imports
    [Module] --> [autogen_team.evaluation.metrics.metrics] : imports
    [Module] --> [autogen_team.infrastructure.services] : imports
    [Module] --> [autogen_team.infrastructure.utils.signers] : imports
    [Module] --> [autogen_team.infrastructure.utils.splitters] : imports
    [Module] --> [autogen_team.models.entities] : imports
    [Module] --> [autogen_team.registry.adapters.mlflow_adapter] : imports
@enduml
```

## 5. Class & Method Specifications
### `TrainingJob` ([`src/autogen_team/application/jobs/training.py`](/src/autogen_team/application/jobs/training.py))
#### Overview
Train and register a single AI/ML model.

Parameters:
    run_config (services.MlflowService.RunConfig): mlflow run config.
    inputs (datasets.ReaderKind): reader for the inputs data.
    targets (datasets.ReaderKind): reader for the targets data.
    model (models.ModelKind): machine learning model to train.
    metrics (metrics_.MetricKind): metrics for the reporting.
    splitter (splitters.SplitterKind): data sets splitter.
    saver (registries.SaverKind): model saver.
    signer (signers.SignerKind): model signer.
    registry (registries.RegisterKind): model register.

#### Attributes
- None found.

#### Methods
##### `run(self) -> base.Locals` (Public)
**Description:** Executes the run operation.

**Inputs:**
- None

**Output:**
- return type: `base.Locals`
- semantic meaning: Returns the result of run.
- possible null values: Yes, if base.Locals allows it.
- exceptions: Standard execution exceptions.

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
result = TrainingJob.run()
```

## 6. Module Functions
## 7. Call Graph
```plantuml
@startuml
[training] --> [RunConfig] : calls
[training] --> [len] : calls
[training] --> [predict] : calls
[training] --> [AutogenMetric] : calls
[training] --> [Field] : calls
[training] --> [next] : calls
[training] --> [save] : calls
[training] --> [load_context_path] : calls
[training] --> [locals] : calls
[training] --> [run_context] : calls
[training] --> [notify] : calls
[training] --> [logger] : calls
[training] --> [read] : calls
[training] --> [enumerate] : calls
[training] --> [fit] : calls
[training] --> [sign] : calls
[training] --> [debug] : calls
[training] --> [score] : calls
[training] --> [check] : calls
[training] --> [TrainTestSplitter] : calls
[training] --> [info] : calls
[training] --> [to_dict] : calls
[training] --> [cast] : calls
[training] --> [split] : calls
[training] --> [log_metric] : calls
[training] --> [lineage] : calls
[training] --> [BaselineAutogenModel] : calls
[training] --> [register] : calls
[training] --> [CustomSaver] : calls
[training] --> [log_input] : calls
[training] --> [client] : calls
[training] --> [MlflowRegister] : calls
[training] --> [InferSigner] : calls
@enduml
```

## 8. Cross References
- **Parent module:** __init__.md
- **Child modules:** None
- **Dependencies:** `autogen_team.evaluation.metrics.metrics`, `autogen_team.application.jobs.base`, `typing`, `autogen_team.infrastructure.utils.signers`, `autogen_team.models.entities`, `mlflow`, `autogen_team.core.schemas`, `autogen_team.registry.adapters.mlflow_adapter`, `autogen_team.data_access.adapters.datasets`, `autogen_team.infrastructure.services`, `pydantic`, `autogen_team.infrastructure.utils.splitters`
- **Used by:** ../../../../tests/application/jobs/test_training.md
- **Calls:** RunConfig, len, predict, AutogenMetric, Field, next, save, load_context_path, locals, run_context, notify, logger, read, enumerate, fit, sign, debug, score, check, TrainTestSplitter, info, to_dict, cast, split, log_metric, lineage, BaselineAutogenModel, register, CustomSaver, log_input, client, MlflowRegister, InferSigner
- **Called from:** None
- **Related classes:** [Classes](../../../../../classes/index.md)
- **Related interfaces:** Not explicitly defined.
- **Related diagrams:** [Diagrams](../../../../../diagrams/index.md)
