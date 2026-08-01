---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Infrastructure Messaging"
source_path: "src/autogen_team/infrastructure/messaging/"
description: "FastAPIKafkaService real-time prediction pipeline and A2A Protocol Pydantic message schemas."
tags: ["infrastructure", "messaging", "kafka", "fastapi", "a2a"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Module Specification: Infrastructure Messaging

* **Source Reference:** `src/autogen_team/infrastructure/messaging/` (2 files)
* **Upstream Dependencies:** [[Modules/Core/Schemas]], [[Modules/Models/Entities]]

## 1. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class PredictionRequest {
        +input_data: Dict
    }
    class PredictionResponse {
        +result: Dict
    }
    class FastAPIKafkaService {
        -producer: Producer
        -consumer: Consumer
        -app: FastAPI
        -model: PyFuncModel
        -consumer_thread: Thread
        +kafka_server: str
        +group_id: str
        +input_topic: str
        +output_topic: str
        +model_uri: str
        +start() void
        +stop() void
        -_consume_messages() void
        -_poll_message() Message?
        -_process_message(msg: Message) void
        -prediction_callback(request: PredictionRequest) PredictionResponse
    }

    class MissionStart {
        +mission_id: str
        +goal: str
        +repository_path: str
        +context: Dict?
    }
    class TaskAssignment {
        +task_id: str
        +mission_id: str
        +description: str
        +relevant_files: List~str~
        +constraints: str?
    }
    class TaskResult {
        +task_id: str
        +mission_id: str
        +status: str
        +diff: str?
        +file_changes: List~str~
        +error_message: str?
    }
    class ReviewResult {
        +mission_id: str
        +approved: bool
        +comments: List~str~
        +suggested_changes: str?
    }

    FastAPIKafkaService --> PredictionRequest : consumes
    FastAPIKafkaService --> PredictionResponse : produces
```

## 2. FastAPIKafkaService

**Source:** `src/autogen_team/infrastructure/messaging/kafka_app.py:L86-L234`

### Lifecycle

1. **`start()`** (L120-L158): Initializes Kafka producer/consumer, loads PyFunc model from MLflow, starts FastAPI with `/health` endpoint, spawns consumer daemon thread.
2. **`_consume_messages()`** (L160-L175): Background loop polling Kafka topic.
3. **`_process_message(msg)`** (L177-L219): Deserializes JSON, calls `prediction_callback`, produces result to output topic, commits offset.
4. **`stop()`** (L221-L238): Closes consumer, flushes producer.

### Configuration

| Parameter | Default | Source |
| :--- | :--- | :--- |
| `kafka_server` | `DEFAULT_KAFKA_SERVER` (env var) | `kafka_app.py:L60-L66` |
| `group_id` | `DEFAULT_GROUP_ID` (env var) | `kafka_app.py:L60-L66` |
| `input_topic` | `DEFAULT_INPUT_TOPIC` (env var) | `kafka_app.py:L60-L66` |
| `output_topic` | `DEFAULT_OUTPUT_TOPIC` (env var) | `kafka_app.py:L60-L66` |

### Error Handling

- Consumer uses manual commit (`enable.auto.commit: false`)
- Auto offset reset: `latest`
- Delivery report callback for producer acknowledgment

## 3. A2A Protocol

**Source:** `src/autogen_team/infrastructure/messaging/a2a_protocol.py:L1-L45`

Pydantic models for inter-agent communication:

| Model | Purpose | Key Field |
| :--- | :--- | :--- |
| `MissionStart` | Event to start a new autonomous mission | `mission_id`, `goal` |
| `TaskAssignment` | Assign a coding task to a Coder Agent | `task_id`, `relevant_files` |
| `TaskResult` | Return from a Coder Agent execution | `status` (completed\|failed), `diff` |
| `ReviewResult` | Return from a Reviewer Agent | `approved`, `comments` |
