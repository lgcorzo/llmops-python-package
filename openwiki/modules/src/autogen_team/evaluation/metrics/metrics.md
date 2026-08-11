---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: metrics"
source_path: "src/autogen_team/evaluation/metrics/metrics.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.077597+00:00"
---

# Module Specification: metrics

* **Source Reference:** `src/autogen_team/evaluation/metrics/metrics.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to metrics.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `__future__.annotations`
- `abc`
- `typing`
- `difflib.SequenceMatcher`
- `typing.Optional`
- `typing.cast`
- `mlflow`
- `pandas`
- `pydantic`
- `mlflow.metrics.MetricValue`
- `autogen_team.core.schemas`
- `autogen_team.models.entities`

**Exported Classes:**
- `Metric`
- `AutogenMetric`
- `AutogenConversationMetric`
- `Threshold`

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
    class Metric {
        +score() : float
        +scorer() : float
        +to_mlflow() : MlflowMetric
    }
    class AutogenMetric {
        +score() : float
        +_exact_match_score() : float
        +_similarity_score() : float
        +_length_ratio() : float
    }
    class AutogenConversationMetric {
        +score() : float
    }
    class Threshold {
        +to_mlflow() : MlflowThreshold
    }
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [__future__.annotations] : imports
    [Module] --> [abc] : imports
    [Module] --> [typing] : imports
    [Module] --> [difflib.SequenceMatcher] : imports
    [Module] --> [typing.Optional] : imports
    [Module] --> [typing.cast] : imports
    [Module] --> [mlflow] : imports
    [Module] --> [pandas] : imports
    [Module] --> [pydantic] : imports
    [Module] --> [mlflow.metrics.MetricValue] : imports
    [Module] --> [autogen_team.core.schemas] : imports
    [Module] --> [autogen_team.models.entities] : imports
@enduml
```

## 5. Class & Method Specifications
### `Metric` ([`src/autogen_team/evaluation/metrics/metrics.py`](/src/autogen_team/evaluation/metrics/metrics.py))
#### Overview
Base class for a project metric.

Use metrics to evaluate model performance.
e.g., accuracy, precision, recall, MAE, F1, ...

Parameters:
    name (str): name of the metric for the reporting.
    greater_is_better (bool): maximize or minimize result.

#### Attributes
- None found.

#### Methods
##### `score(self, targets: pd.DataFrame, outputs: pd.DataFrame) -> float` (Public)
**Description:** Score the outputs against the targets.

Args:
    targets (pd.DataFrame): expected values.
    outputs (pd.DataFrame): predicted values.

Returns:
    float: single result from the metric computation.

**Inputs:**
- `targets`: pd.DataFrame
- `outputs`: pd.DataFrame

**Output:**
- Return Type: `float`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = Metric.score(..., ...)
```

##### `scorer(self, model: models.Model, inputs: schemas.Inputs, targets: pd.DataFrame) -> float` (Public)
**Description:** Score model outputs against targets.

Args:
    model (models.Model): model to evaluate.
    inputs (schemas.Inputs): model inputs values.
    targets (schemas.Targets): model expected values.

Returns:
    float: single result from the metric computation.

**Inputs:**
- `model`: models.Model
- `inputs`: schemas.Inputs
- `targets`: pd.DataFrame

**Output:**
- Return Type: `float`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = Metric.scorer(..., ..., ...)
```

##### `to_mlflow(self) -> MlflowMetric` (Public)
**Description:** Convert the metric to an Mlflow metric.

Returns:
    MlflowMetric: the Mlflow metric.

**Inputs:**
- None

**Output:**
- Return Type: `MlflowMetric`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = Metric.to_mlflow()
```

### `AutogenMetric` ([`src/autogen_team/evaluation/metrics/metrics.py`](/src/autogen_team/evaluation/metrics/metrics.py))
#### Overview
Evaluate text-based Autogen responses using conversation metrics.

Parameters:
    metric_type (str): Type of text metric (exact_match, similarity, length_ratio)
    similarity_threshold (float): Minimum similarity score for partial matches

#### Attributes
- None found.

#### Methods
##### `score(self, targets: pd.DataFrame, outputs: pd.DataFrame) -> float` (Public)
**Description:** No description provided.

**Inputs:**
- `targets`: pd.DataFrame
- `outputs`: pd.DataFrame

**Output:**
- Return Type: `float`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = AutogenMetric.score(..., ...)
```

##### `_exact_match_score(self, y_true: pd.Series[str], y_pred: pd.Series[str]) -> float` (Private)
**Purpose:** No description provided.

**Parameters:**
- `y_true`: pd.Series[str]
- `y_pred`: pd.Series[str]

**Return value:**
- `float`

##### `_similarity_score(self, y_true: pd.Series[str], y_pred: pd.Series[str]) -> float` (Private)
**Purpose:** No description provided.

**Parameters:**
- `y_true`: pd.Series[str]
- `y_pred`: pd.Series[str]

**Return value:**
- `float`

##### `_length_ratio(self, y_true: pd.Series[str], y_pred: pd.Series[str]) -> float` (Private)
**Purpose:** No description provided.

**Parameters:**
- `y_true`: pd.Series[str]
- `y_pred`: pd.Series[str]

**Return value:**
- `float`

### `AutogenConversationMetric` ([`src/autogen_team/evaluation/metrics/metrics.py`](/src/autogen_team/evaluation/metrics/metrics.py))
#### Overview
Evaluate conversation quality metrics for Autogen interactions.

Parameters:
    check_termination (bool): Verify if conversation reached termination
    check_error_messages (bool): Check for error messages in output

#### Attributes
- None found.

#### Methods
##### `score(self, targets: pd.DataFrame, outputs: pd.DataFrame) -> float` (Public)
**Description:** No description provided.

**Inputs:**
- `targets`: pd.DataFrame
- `outputs`: pd.DataFrame

**Output:**
- Return Type: `float`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = AutogenConversationMetric.score(..., ...)
```

### `Threshold` ([`src/autogen_team/evaluation/metrics/metrics.py`](/src/autogen_team/evaluation/metrics/metrics.py))
#### Overview
A project threshold for a metric.

Use thresholds to monitor model performances.
e.g., to trigger an alert when a threshold is met.

Parameters:
    threshold (int | float): absolute threshold value.
    greater_is_better (bool): maximize or minimize result.

#### Attributes
- None found.

#### Methods
##### `to_mlflow(self) -> MlflowThreshold` (Public)
**Description:** Convert the threshold to an mlflow threshold.

Returns:
    MlflowThreshold: the mlflow threshold.

**Inputs:**
- None

**Output:**
- Return Type: `MlflowThreshold`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = Threshold.to_mlflow()
```

## 6. Module Functions