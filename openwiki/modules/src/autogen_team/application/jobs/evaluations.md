---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: evaluations"
source_path: "src/autogen_team/application/jobs/evaluations.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-28T06:32:33.112298+00:00"
---

# Module Specification: evaluations

* **Source Reference:** `src/autogen_team/application/jobs/evaluations.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to evaluations.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `typing`
- `typing.Dict`
- `typing.List`
- `mlflow`
- `pandas`
- `pydantic`
- `autogen_team.application.jobs.base`
- `autogen_team.core.schemas`
- `autogen_team.data_access.adapters.datasets`
- `autogen_team.evaluation.metrics`
- `autogen_team.infrastructure.services`
- `autogen_team.registry.adapters.mlflow_adapter`

**Exported Classes:**
- `EvaluationsJob`

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
    class EvaluationsJob {
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
                    [evaluations.py]
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
        [evaluations.py]
    }
    [evaluations.py] --> [typing]
    [evaluations.py] --> [typing.Dict]
    [evaluations.py] --> [typing.List]
    [evaluations.py] --> [mlflow]
    [evaluations.py] --> [pandas]
    [evaluations.py] --> [pydantic]
    [evaluations.py] --> [autogen_team.application.jobs.base]
    [evaluations.py] --> [autogen_team.core.schemas]
    [evaluations.py] --> [autogen_team.data_access.adapters.datasets]
    [evaluations.py] --> [autogen_team.evaluation.metrics]
    [evaluations.py] --> [autogen_team.infrastructure.services]
    [evaluations.py] --> [autogen_team.registry.adapters.mlflow_adapter]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [typing] : imports
    [Module] --> [typing.Dict] : imports
    [Module] --> [typing.List] : imports
    [Module] --> [mlflow] : imports
    [Module] --> [pandas] : imports
    [Module] --> [pydantic] : imports
    [Module] --> [autogen_team.application.jobs.base] : imports
    [Module] --> [autogen_team.core.schemas] : imports
    [Module] --> [autogen_team.data_access.adapters.datasets] : imports
    [Module] --> [autogen_team.evaluation.metrics] : imports
    [Module] --> [autogen_team.infrastructure.services] : imports
    [Module] --> [autogen_team.registry.adapters.mlflow_adapter] : imports
@enduml
```

## 5. Class & Method Specifications
### `EvaluationsJob` ([`src/autogen_team/application/jobs/evaluations.py`](/src/autogen_team/application/jobs/evaluations.py))
#### Overview
Generate evaluations from a registered model and a dataset.

Parameters:
    run_config (services.MlflowService.RunConfig): mlflow run config.
    inputs (datasets.ReaderKind): reader for the inputs data.
    targets (datasets.ReaderKind): reader for the targets data.
    model_type (str): model type (e.g., "regressor", "classifier").
    alias_or_version (str | int): alias or version for the model.
    metrics (metrics_.MetricKind): metrics for the reporting.
    evaluators (list[str]): list of evaluators to use.
    thresholds (dict[str, metrics_.Threshold] | None): metric thresholds.

#### Attributes
- None found.

#### Methods
##### `run(self) -> base.Locals` (Public)
**Description:** No description provided.

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
result = EvaluationsJob.run()
```

## 6. Module Functions
## 7. Call Graph
```plantuml
@startuml
[evaluations] --> [client] : calls
[evaluations] --> [Threshold] : calls
[evaluations] --> [info] : calls
[evaluations] --> [RunConfig] : calls
[evaluations] --> [notify] : calls
[evaluations] --> [debug] : calls
[evaluations] --> [AutogenMetric] : calls
[evaluations] --> [evaluate] : calls
[evaluations] --> [read] : calls
[evaluations] --> [check] : calls
[evaluations] --> [to_mlflow] : calls
[evaluations] --> [to_dict] : calls
[evaluations] --> [run_context] : calls
[evaluations] --> [from_pandas] : calls
[evaluations] --> [items] : calls
[evaluations] --> [lineage] : calls
[evaluations] --> [log_input] : calls
[evaluations] --> [logger] : calls
[evaluations] --> [locals] : calls
[evaluations] --> [uri_for_model_alias_or_version] : calls
[evaluations] --> [concat] : calls
[evaluations] --> [Field] : calls
@enduml
```

## 8. Cross References
- **Dependencies:** [Dependencies](../../../../../dependencies/index.md)
- **Used by:** ../../../../tests/application/jobs/test_evaluations.md
- **Calls:** client, Threshold, info, RunConfig, notify, debug, AutogenMetric, evaluate, read, check, to_mlflow, to_dict, run_context, from_pandas, items, lineage, log_input, logger, locals, uri_for_model_alias_or_version, concat, Field
- **Called from:** None
- **Related classes:** [Classes](../../../../../classes/index.md)
- **Related diagrams:** [Diagrams](../../../../../diagrams/index.md)
