---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Inference"
source_path: "src/autogen_team/application/jobs/inference.py"
description: "Exhaustive functional summary for Inference."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Inference

* **Source Reference:** `src/autogen_team/application/jobs/inference.py`

## UML Diagrams

```mermaid
classDiagram
    class InferenceJob {
        +T.Literal['InferenceJob'] KIND
        +str \ alias_or_version
        +int
        +inputs
        +loader
        +outputs
        +|run(): base.Locals
    }
    Job <|-- InferenceJob
    InferenceJob --> ParquetReader
    InferenceJob --> ParquetWriter
    InferenceJob --> CustomLoader
```
