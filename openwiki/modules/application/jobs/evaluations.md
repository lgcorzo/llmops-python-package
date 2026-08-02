---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Evaluations"
source_path: "src/autogen_team/application/jobs/evaluations.py"
description: "Exhaustive functional summary for Evaluations."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Evaluations

* **Source Reference:** `src/autogen_team/application/jobs/evaluations.py`

## UML Diagrams

```mermaid
classDiagram
    class EvaluationsJob {
        +T.Literal['EvaluationsJob'] KIND
        +T.Union[str, int] alias_or_version
        +List[str] evaluators
        +inputs
        +List[metrics_.AutogenMetric] metrics
        +str model_type
        +run_config
        +targets
        +Dict[str, metrics_.Threshold] thresholds
        +run(): base.Locals
    }
    Job <|-- EvaluationsJob
    EvaluationsJob --> ParquetReader
    EvaluationsJob --> ParquetReader
    EvaluationsJob --> RunConfig
```
