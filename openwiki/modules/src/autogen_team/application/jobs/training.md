---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: training"
source_path: "src/autogen_team/application/jobs/training.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-09-02T05:14:17.056805+00:00"
---

# Module Specification: training

* **Source Reference:** `src/autogen_team/application/jobs/training.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to training.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

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

### Package Diagram
```plantuml
@startuml
    package "src" {
        package "autogen_team" {
            package "application" {
                package "jobs" {
                    [training.py]
                }
            }
        }
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
result = TrainingJob.run()
```

## 6. Module Functions
## 7. Call Graph
```plantuml
@startuml
[training] --> [notify] : calls
[training] --> [read] : calls
[training] --> [register] : calls
[training] --> [Field] : calls
[training] --> [RunConfig] : calls
[training] --> [cast] : calls
[training] --> [info] : calls
[training] --> [log_input] : calls
[training] --> [sign] : calls
[training] --> [logger] : calls
[training] --> [client] : calls
[training] --> [InferSigner] : calls
[training] --> [BaselineAutogenModel] : calls
[training] --> [fit] : calls
[training] --> [log_metric] : calls
[training] --> [predict] : calls
[training] --> [AutogenMetric] : calls
[training] --> [to_dict] : calls
[training] --> [split] : calls
[training] --> [score] : calls
[training] --> [MlflowRegister] : calls
[training] --> [len] : calls
[training] --> [locals] : calls
[training] --> [TrainTestSplitter] : calls
[training] --> [run_context] : calls
[training] --> [check] : calls
[training] --> [lineage] : calls
[training] --> [enumerate] : calls
[training] --> [next] : calls
[training] --> [debug] : calls
[training] --> [save] : calls
[training] --> [CustomSaver] : calls
[training] --> [load_context_path] : calls
@enduml
```

## 8. Cross References
- **Dependencies:** [Dependencies](../../../../../dependencies/index.md)
- **Used by:** ../../../../tests/application/jobs/test_training.md
- **Calls:** notify, read, register, Field, RunConfig, cast, info, log_input, sign, logger, client, InferSigner, BaselineAutogenModel, fit, log_metric, predict, AutogenMetric, to_dict, split, score, MlflowRegister, len, locals, TrainTestSplitter, run_context, check, lineage, enumerate, next, debug, save, CustomSaver, load_context_path
- **Called from:** None
- **Related classes:** [Classes](../../../../../classes/index.md)
- **Related diagrams:** [Diagrams](../../../../../diagrams/index.md)
