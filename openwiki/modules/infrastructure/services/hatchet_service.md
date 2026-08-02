---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Hatchet Service"
source_path: "src/autogen_team/infrastructure/services/hatchet_service.py"
description: "Exhaustive functional summary for Hatchet Service."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Hatchet Service

* **Source Reference:** `src/autogen_team/infrastructure/services/hatchet_service.py`

## UML Diagrams

```mermaid
classDiagram
    class HatchetService {
        +Hatchet client
        +ClassVar[Env] env
        +Optional[str] namespace
        +Optional[str] token
        +start(): None
        +stop(): None
    }
    Service <|-- HatchetService
    HatchetInferenceJob --> HatchetService
```
