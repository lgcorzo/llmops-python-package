---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Training"
source_path: "src/autogen_team/application/jobs/training.py"
description: "Exhaustive functional summary for Training."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Training

* **Source Reference:** `src/autogen_team/application/jobs/training.py`

## UML Diagrams

```mermaid
classDiagram
    class TrainingJob {
        +T.Literal['TrainingJob'] KIND
        +inputs
        +list metrics
        +model
        +registry
        +run_config
        +saver
        +signer
        +splitter
        +targets
        +run(): base.Locals
    }
    Job <|-- TrainingJob
    TrainingJob --> ParquetReader
    TrainingJob --> ParquetReader
    TrainingJob --> RunConfig
    TrainingJob --> InferSigner
    TrainingJob --> BaselineAutogenModel
    TrainingJob --> CustomSaver
    TrainingJob --> MlflowRegister
```
