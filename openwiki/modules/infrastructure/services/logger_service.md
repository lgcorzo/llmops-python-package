---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Logger Service"
source_path: "src/autogen_team/infrastructure/services/logger_service.py"
description: "Exhaustive functional summary for Logger Service."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Logger Service

* **Source Reference:** `src/autogen_team/infrastructure/services/logger_service.py`

## UML Diagrams

```mermaid
classDiagram
    class LoggerService {
        +bool backtrace
        +bool catch
        +bool colorize
        +bool diagnose
        +str format
        +str level
        +bool serialize
        +str sink
        +logger(): loguru.Logger
        +start(): None
    }
    class PropagateHandler {
        +emit(record: logging.LogRecord): None
    }
    class Service {
        +start(): None
        +stop(): None
    }
    Service <|-- AlertsService
    Service <|-- HatchetService
    Service <|-- LoggerService
    Service <|-- MCPService
    Service <|-- MlflowService
    Job --> LoggerService
```
