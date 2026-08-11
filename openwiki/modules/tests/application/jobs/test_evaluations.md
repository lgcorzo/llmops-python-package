---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_evaluations"
source_path: "tests/application/jobs/test_evaluations.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.370065+00:00"
---

# Module Specification: test_evaluations

* **Source Reference:** `tests/application/jobs/test_evaluations.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to test evaluations.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `_pytest.capture`
- `pytest`
- `autogen_team.application.jobs`
- `autogen_team.core.schemas`
- `autogen_team.data_access.adapters.datasets`
- `autogen_team.evaluation.metrics`
- `autogen_team.infrastructure.services`
- `autogen_team.registry.adapters.mlflow_adapter`
- `mlflow.entities.Experiment`

**Exported Classes:**
- None

**Exported Functions:**
- `test_evaluations_job`

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
    [Module] --> [_pytest.capture] : imports
    [Module] --> [pytest] : imports
    [Module] --> [autogen_team.application.jobs] : imports
    [Module] --> [autogen_team.core.schemas] : imports
    [Module] --> [autogen_team.data_access.adapters.datasets] : imports
    [Module] --> [autogen_team.evaluation.metrics] : imports
    [Module] --> [autogen_team.infrastructure.services] : imports
    [Module] --> [autogen_team.registry.adapters.mlflow_adapter] : imports
    [Module] --> [mlflow.entities.Experiment] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `test_evaluations_job(alias_or_version: str | int, thresholds: dict[str, metrics.Threshold], mlflow_service: services.MlflowService, alerts_service: services.AlertsService, logger_service: services.LoggerService, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader, model_alias: registries.Version, metric: metrics.AutogenMetric, capsys: pc.CaptureFixture[str])`
No description provided.

**Inputs:**
- `alias_or_version`: str | int
- `thresholds`: dict[str, metrics.Threshold]
- `mlflow_service`: services.MlflowService
- `alerts_service`: services.AlertsService
- `logger_service`: services.LoggerService
- `inputs_reader`: datasets.ParquetReader
- `targets_reader`: datasets.ParquetReader
- `model_alias`: registries.Version
- `metric`: metrics.AutogenMetric
- `capsys`: pc.CaptureFixture[str]

**Output:**
- Return Type: `None`
