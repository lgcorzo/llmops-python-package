---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Searchers"
source_path: "src/autogen_team/infrastructure/utils/searchers.py"
description: "Exhaustive functional summary for Searchers."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Searchers

* **Source Reference:** `src/autogen_team/infrastructure/utils/searchers.py`

## UML Diagrams

```mermaid
classDiagram
    class GridCVSearcher {
        +T.Literal['GridCVSearcher'] KIND
        +str \ error_score
        +float
        +n_jobs : int \| None
        +refit : bool
        +return_train_score : bool
        +verbose : int
        +|search(model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation): Results
    }
    class Searcher {
        +str KIND
        +dict param_grid
        +search(model: models.Model, metric: metrics.Metric, inputs: schemas.Inputs, targets: schemas.Targets, cv: CrossValidation): Results
    }
    Searcher <|-- GridCVSearcher
    TuningJob --> GridCVSearcher
```
