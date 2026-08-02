---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Hatchet Inference"
source_path: "src/autogen_team/application/jobs/hatchet_inference.py"
description: "Exhaustive functional summary for Hatchet Inference."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Hatchet Inference

* **Source Reference:** `src/autogen_team/application/jobs/hatchet_inference.py`

## UML Diagrams

```mermaid
classDiagram
    class HatchetInferenceJob {
        +T.Literal['HatchetInferenceJob'] KIND
        +str \ alias_or_version
        +int
        +hatchet_service
        +inputs
        +loader
        +outputs
        +|run(): base.Locals
    }
    Job <|-- HatchetInferenceJob
    HatchetInferenceJob --> ParquetReader
    HatchetInferenceJob --> ParquetWriter
    HatchetInferenceJob --> HatchetService
    HatchetInferenceJob --> CustomLoader
```
