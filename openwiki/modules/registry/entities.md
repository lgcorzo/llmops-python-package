---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Entities"
source_path: "src/autogen_team/registry/entities.py"
description: "Exhaustive functional summary for Entities."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Entities

* **Source Reference:** `src/autogen_team/registry/entities.py`

## UML Diagrams

```mermaid
classDiagram
    class ModelInfo {
        +str model_uri
        +Optional[str] run_id
    }
    class ModelVersion {
        +str model_uri
        +str name
        +str stage
        +str version
    }
```
