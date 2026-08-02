---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Splitters"
source_path: "src/autogen_team/infrastructure/utils/splitters.py"
description: "Exhaustive functional summary for Splitters."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Splitters

* **Source Reference:** `src/autogen_team/infrastructure/utils/splitters.py`

## UML Diagrams

```mermaid
classDiagram
    class Splitter {
        +str KIND
        +get_n_splits(inputs: schemas.Inputs, targets: schemas.Targets, groups: Index \| None): int
        +split(inputs: schemas.Inputs, targets: schemas.Targets, groups: Index \| None): TrainTestSplits
    }
    class TimeSeriesSplitter {
        +T.Literal['TimeSeriesSplitter'] KIND
        +int gap
        +int n_splits
        +int \ test_size
        +float
        +|get_n_splits(inputs: schemas.Inputs, targets: schemas.Targets, groups: Index \| None): int
        +split(inputs: schemas.Inputs, targets: schemas.Targets, groups: Index \| None): TrainTestSplits
    }
    class TrainTestSplitter {
        +T.Literal['TrainTestSplitter'] KIND
        +int random_state
        +bool shuffle
        +int \ test_size
        +float
        +|get_n_splits(inputs: schemas.Inputs, targets: schemas.Targets, groups: Index \| None): int
        +split(inputs: schemas.Inputs, targets: schemas.Targets, groups: Index \| None): TrainTestSplits
    }
    Splitter <|-- TimeSeriesSplitter
    Splitter <|-- TrainTestSplitter
```
