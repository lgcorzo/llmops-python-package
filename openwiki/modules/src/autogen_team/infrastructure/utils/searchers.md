---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: searchers"
source_path: "src/autogen_team/infrastructure/utils/searchers.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.037378+00:00"
---

# Module Specification: searchers

* **Source Reference:** `src/autogen_team/infrastructure/utils/searchers.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to searchers.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `abc`
- `typing`
- `pandas`
- `pydantic`
- `sklearn.model_selection`
- `autogen_team.core.schemas`
- `autogen_team.evaluation.metrics`
- `autogen_team.infrastructure.utils.splitters`
- `autogen_team.models.entities`

**Exported Classes:**
- `Searcher`
- `GridCVSearcher`

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
    class Searcher {
        +search() : Results
    }
    class GridCVSearcher {
        +search() : Results
    }
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [abc] : imports
    [Module] --> [typing] : imports
    [Module] --> [pandas] : imports
    [Module] --> [pydantic] : imports
    [Module] --> [sklearn.model_selection] : imports
    [Module] --> [autogen_team.core.schemas] : imports
    [Module] --> [autogen_team.evaluation.metrics] : imports
    [Module] --> [autogen_team.infrastructure.utils.splitters] : imports
    [Module] --> [autogen_team.models.entities] : imports
@enduml
```

## 5. Class & Method Specifications
### `Searcher` ([`src/autogen_team/infrastructure/utils/searchers.py`](/src/autogen_team/infrastructure/utils/searchers.py))
#### Overview
Base class for a searcher.

Use searcher to fine-tune models.
i.e., to find the best model params.

Parameters:
    param_grid (Grid): mapping of param key -> values.

#### Attributes
- None found.

#### Methods
##### `search(self, model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation) -> Results` (Public)
**Description:** Search the best model for the given inputs and targets.

Args:
    model (models.Model): AI/ML model to fine-tune.
    metric (metrics.Metric): main metric to optimize.
    inputs (schemas.Inputs): model inputs for tuning.
    targets (schemas.Targets): model targets for tuning.
    cv (CrossValidation): choice for cross-fold validation.

Returns:
    Results: all the results of the searcher execution process.

**Inputs:**
- `model`: models.Model
- `metric`: metrics.Metric
- `inputs`: schemas.Inputs
- `targets`: schemas.Targets
- `cv`: CrossValidation

**Output:**
- Return Type: `Results`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = Searcher.search(..., ..., ..., ..., ...)
```

### `GridCVSearcher` ([`src/autogen_team/infrastructure/utils/searchers.py`](/src/autogen_team/infrastructure/utils/searchers.py))
#### Overview
Grid searcher with cross-fold validation.

Convention: metric returns higher values for better models.

Parameters:
    n_jobs (int, optional): number of jobs to run in parallel.
    refit (bool): refit the model after the tuning.
    verbose (int): set the searcher verbosity level.
    error_score (str | float): strategy or value on error.
    return_train_score (bool): include train scores if True.

#### Attributes
- None found.

#### Methods
##### `search(self, model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation) -> Results` (Public)
**Description:** No description provided.

**Inputs:**
- `model`: models.Model
- `metric`: metrics.Metric
- `inputs`: schemas.Inputs
- `targets`: schemas.Targets
- `cv`: CrossValidation

**Output:**
- Return Type: `Results`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = GridCVSearcher.search(..., ..., ..., ..., ...)
```

## 6. Module Functions