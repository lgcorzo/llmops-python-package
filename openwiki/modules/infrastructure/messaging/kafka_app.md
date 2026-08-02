---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Kafka App"
source_path: "src/autogen_team/infrastructure/messaging/kafka_app.py"
description: "Exhaustive functional summary for Kafka App."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Kafka App

* **Source Reference:** `src/autogen_team/infrastructure/messaging/kafka_app.py`

## UML Diagrams

```mermaid
classDiagram
    class FastAPIKafkaService {
        +Consumer \ consumer
        +None
        +consumer_config : Dict[str, Any]
        +input_topic : str
        +output_topic : str
        +prediction_callback : Callable[[PredictionRequest], PredictionResponse]
        +producer : Producer \| None
        +producer_config : Dict[str, Any]
        +server_thread : threading.Thread \| None
        +stop_event : Event
        +|delivery_report(err: Optional[KafkaError], msg: Any): None
        +start(): None
        +stop(): None
    }
    class PredictionRequest {
        +Dict[str, Any] input_data
        +validate_model(): DataFrameBase[InputsSchema]
    }
    class PredictionResponse {
        +Dict[str, Any] result
    }
    PredictionResponse --> FastAPIKafkaService
```
