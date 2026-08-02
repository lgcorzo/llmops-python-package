---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Tuning"
source_path: "src/autogen_team/application/jobs/tuning.py"
description: "Exhaustive functional summary for Tuning."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Tuning

* **Source Reference:** `src/autogen_team/application/jobs/tuning.py`

## UML Diagrams

```mermaid
classDiagram
    class TuningJob {
        +T.Literal['TuningJob'] KIND
        +inputs
        +metric
        +model
        +run_config
        +searcher
        +splitter
        +targets
        +run(): base.Locals
    }
    Job <|-- TuningJob
    TuningJob --> ParquetReader
    TuningJob --> ParquetReader
    TuningJob --> RunConfig
    TuningJob --> GridCVSearcher
    TuningJob --> BaselineAutogenModel
```
