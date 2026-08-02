---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Base"
source_path: "src/autogen_team/application/jobs/base.py"
description: "Exhaustive functional summary for Base."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Base

* **Source Reference:** `src/autogen_team/application/jobs/base.py`

## UML Diagrams

```mermaid
classDiagram
    class Job {
        +str KIND
        +alerts_service
        +logger_service
        +mlflow_service
        +run(): Locals
    }
    Job <|-- EvaluationsJob
    Job <|-- ExplanationsJob
    Job <|-- HatchetInferenceJob
    Job <|-- InferenceJob
    Job <|-- PromotionJob
    Job <|-- TrainingJob
    Job <|-- TuningJob
    Job --> AlertsService
    Job --> LoggerService
    Job --> MlflowService
```
