---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Infrastructure Utils"
source_path: "src/autogen_team/infrastructure/utils/"
description: "Utility classes for hyperparameter search, model signing, and data splitting."
tags: ["infrastructure", "utils", "searcher", "signer", "splitter"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Module Specification: Infrastructure Utils

* **Source Reference:** `src/autogen_team/infrastructure/utils/` (3 files)
* **Downstream Consumers:** [[Modules/Application/Jobs]] (TuningJob, TrainingJob, EvaluationsJob)

## 1. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT

    class Searcher {
        <<abstract>>
        +KIND: str
        +param_grid: Grid
        +search(model, metric, inputs, targets, cv)* Results
    }
    class GridCVSearcher {
        +KIND: "GridCVSearcher"
        +n_jobs: int?
        +refit: bool = True
        +verbose: int = 3
        +search(model, metric, inputs, targets, cv) Results
    }

    class Signer {
        <<abstract>>
        +KIND: str
        +sign(inputs, outputs)* Signature
    }
    class InferSigner {
        +KIND: "InferSigner"
        +sign(inputs, outputs) Signature
    }

    class Splitter {
        <<abstract>>
        +KIND: str
        +split(inputs, targets, groups?)* TrainTestSplits
        +get_n_splits(inputs, targets, groups?)* int
    }
    class TrainTestSplitter {
        +KIND: "TrainTestSplitter"
        +shuffle: bool = False
        +test_size: int | float = 2
        +random_state: int = 42
        +split(inputs, targets, groups?) TrainTestSplits
        +get_n_splits(inputs, targets, groups?) int
    }
    class TimeSeriesSplitter {
        +KIND: "TimeSeriesSplitter"
        +gap: int = 0
        +n_splits: int = 4
        +test_size: int | float = 1440
        +split(inputs, targets, groups?) TrainTestSplits
        +get_n_splits(inputs, targets, groups?) int
    }

    Searcher <|-- GridCVSearcher : Inheritance
    Signer <|-- InferSigner : Inheritance
    Splitter <|-- TrainTestSplitter : Inheritance
    Splitter <|-- TimeSeriesSplitter : Inheritance
```

## 2. Searchers (`searchers.py:L1-L118`)

Hyperparameter search using scikit-learn `GridSearchCV`:

- `Searcher` (abstract): Defines `search(model, metric, inputs, targets, cv)` interface
- `GridCVSearcher`: Exhaustive grid search with cross-fold validation

**Type Aliases:**
- `Grid = dict[ParamKey, list[ParamValue]]`
- `Results = tuple[DataFrame, float, Params]`
- `CrossValidation = int | TrainTestSplits | Splitter`

## 3. Signers (`signers.py:L1-L55`)

Model signature generation using MLflow's `infer_signature`:

- `Signer` (abstract): Defines `sign(inputs, outputs)` interface
- `InferSigner`: Automatic signature inference from data

## 4. Splitters (`splitters.py:L1-L124`)

Data splitting for cross-validation:

- `Splitter` (abstract): Defines `split(inputs, targets, groups?)` and `get_n_splits()` interface
- `TrainTestSplitter`: Simple train/test split with optional shuffle
- `TimeSeriesSplitter`: Fixed time series splits using `TimeSeriesSplit` (default: 2-month test window)
