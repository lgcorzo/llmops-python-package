---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_kafka_app"
source_path: "tests/infrastructure/messaging/test_kafka_app.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-28T06:32:33.219686+00:00"
---

# Module Specification: test_kafka_app

* **Source Reference:** `tests/infrastructure/messaging/test_kafka_app.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to test kafka app.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `json`
- `os`
- `signal`
- `typing.Any`
- `typing.Dict`
- `typing.Generator`
- `unittest.mock.MagicMock`
- `unittest.mock.patch`
- `pytest`
- `autogen_team.infrastructure.messaging.kafka_app.DEFAULT_FASTAPI_HOST`
- `autogen_team.infrastructure.messaging.kafka_app.DEFAULT_FASTAPI_PORT`
- `autogen_team.infrastructure.messaging.kafka_app.FastAPIKafkaService`
- `autogen_team.infrastructure.messaging.kafka_app.PredictionResponse`
- `autogen_team.infrastructure.messaging.kafka_app.app`
- `confluent_kafka.KafkaError`

**Exported Classes:**
- None

**Exported Functions:**
- `mock_kafka_service`
- `test_initialization`
- `test_delivery_report`
- `test_start_producer_failure`
- `test_start_consumer_failure`
- `test_run_server`
- `test_run_server_failure`
- `test_consume_messages`
- `test_consume_messages_with_error`
- `test_poll_message`
- `test_poll_message_no_consumer`
- `test_handle_message_error_partition_eof`
- `test_handle_message_error_other_error`
- `test_process_message`
- `test_process_message_json_decode_error`
- `test_process_message_prediction_error`
- `test_close_consumer`
- `test_stop`
- `test_main_function`
- `test_process_message_producer_none`
- `test_process_message_exception_on_produce`
- `test_main_prediction_callback_numpy`
- `test_main_prediction_callback_error`

**Exported Interfaces:**
- Not explicitly defined.

**Public API:**
- Not explicitly defined.

## 3. Architecture & Execution
### Internal Architecture
Not explicitly defined.

### Execution Flow
Not explicitly defined.

### Sequence Explanation
Not explicitly defined.

### Examples
Not explicitly defined.

## 4. UML 2.0 Diagrams
### Class Diagram
```plantuml
@startuml
    ' No classes found in module
@enduml
```

### Package Diagram
```plantuml
@startuml
    package "tests" {
        package "infrastructure" {
            package "messaging" {
                [test_kafka_app.py]
            }
        }
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    mock_kafka_service -> PredictionResponse : call
    mock_kafka_service -> patch : call
    mock_kafka_service -> MagicMock : call
    mock_kafka_service -> FastAPIKafkaService : call
    mock_kafka_service -> fixture : call
    test_delivery_report -> patch : call
    test_delivery_report -> assert_called_once : call
    test_delivery_report -> MagicMock : call
    test_delivery_report -> delivery_report : call
    test_start_producer_failure -> start : call
    test_start_producer_failure -> raises : call
    test_start_producer_failure -> Exception : call
    test_start_consumer_failure -> start : call
    test_start_consumer_failure -> raises : call
    test_start_consumer_failure -> Exception : call
    test_run_server -> assert_called_once_with : call
    test_run_server -> patch : call
    test_run_server -> _run_server : call
    test_run_server_failure -> Exception : call
    test_run_server_failure -> patch : call
    test_run_server_failure -> _run_server : call
    test_consume_messages -> assert_called_once : call
    test_consume_messages -> _consume_messages : call
    test_consume_messages -> MagicMock : call
    test_consume_messages_with_error -> assert_not_called : call
    test_consume_messages_with_error -> assert_called_once : call
    test_consume_messages_with_error -> _consume_messages : call
    test_consume_messages_with_error -> MagicMock : call
    test_poll_message -> _poll_message : call
    test_poll_message -> assert_called_once_with : call
    test_poll_message -> MagicMock : call
    test_poll_message_no_consumer -> _poll_message : call
    test_poll_message_no_consumer -> assert_called_once : call
    test_poll_message_no_consumer -> patch : call
    test_handle_message_error_partition_eof -> patch : call
    test_handle_message_error_partition_eof -> _handle_message_error : call
    test_handle_message_error_partition_eof -> assert_called_once : call
    test_handle_message_error_partition_eof -> MagicMock : call
    test_handle_message_error_other_error -> patch : call
    test_handle_message_error_other_error -> _handle_message_error : call
    test_handle_message_error_other_error -> assert_called_once : call
    test_handle_message_error_other_error -> MagicMock : call
    test_process_message -> PredictionResponse : call
    test_process_message -> assert_called_once : call
    test_process_message -> assert_called_once_with : call
    test_process_message -> patch : call
    test_process_message -> MagicMock : call
    test_process_message -> _process_message : call
    test_process_message_json_decode_error -> assert_called_once : call
    test_process_message_json_decode_error -> patch : call
    test_process_message_json_decode_error -> MagicMock : call
    test_process_message_json_decode_error -> assert_called : call
    test_process_message_json_decode_error -> JSONDecodeError : call
    test_process_message_json_decode_error -> assert_not_called : call
    test_process_message_json_decode_error -> _process_message : call
    test_process_message_prediction_error -> assert_called_once : call
    test_process_message_prediction_error -> Exception : call
    test_process_message_prediction_error -> patch : call
    test_process_message_prediction_error -> MagicMock : call
    test_process_message_prediction_error -> assert_called : call
    test_process_message_prediction_error -> _process_message : call
    test_close_consumer -> assert_called_once : call
    test_close_consumer -> patch : call
    test_close_consumer -> MagicMock : call
    test_close_consumer -> assert_called : call
    test_close_consumer -> _close_consumer : call
    test_stop -> assert_called_once : call
    test_stop -> assert_called_once_with : call
    test_stop -> patch : call
    test_stop -> MagicMock : call
    test_stop -> stop : call
    test_stop -> is_set : call
    test_stop -> getpid : call
    test_main_function -> main : call
    test_main_function -> assert_called_once : call
    test_main_function -> assert_called_once_with : call
    test_main_function -> patch : call
    test_main_function -> MagicMock : call
    test_main_function -> assert_called : call
    test_process_message_producer_none -> patch : call
    test_process_message_producer_none -> _process_message : call
    test_process_message_producer_none -> assert_any_call : call
    test_process_message_producer_none -> MagicMock : call
    test_process_message_exception_on_produce -> patch : call
    test_process_message_exception_on_produce -> Exception : call
    test_process_message_exception_on_produce -> MagicMock : call
    test_process_message_exception_on_produce -> assert_any_call : call
    test_process_message_exception_on_produce -> _process_message : call
    test_main_prediction_callback_numpy -> object : call
    test_main_prediction_callback_numpy -> main : call
    test_main_prediction_callback_numpy -> patch : call
    test_main_prediction_callback_numpy -> MagicMock : call
    test_main_prediction_callback_numpy -> get : call
    test_main_prediction_callback_numpy -> callback : call
    test_main_prediction_callback_numpy -> PredictionRequest : call
    test_main_prediction_callback_error -> main : call
    test_main_prediction_callback_error -> Exception : call
    test_main_prediction_callback_error -> patch : call
    test_main_prediction_callback_error -> MagicMock : call
    test_main_prediction_callback_error -> get : call
    test_main_prediction_callback_error -> callback : call
    test_main_prediction_callback_error -> PredictionRequest : call
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Infrastructure/Other" {
        [test_kafka_app.py]
    }
    [test_kafka_app.py] --> [json]
    [test_kafka_app.py] --> [os]
    [test_kafka_app.py] --> [signal]
    [test_kafka_app.py] --> [typing.Any]
    [test_kafka_app.py] --> [typing.Dict]
    [test_kafka_app.py] --> [typing.Generator]
    [test_kafka_app.py] --> [unittest.mock.MagicMock]
    [test_kafka_app.py] --> [unittest.mock.patch]
    [test_kafka_app.py] --> [pytest]
    [test_kafka_app.py] --> [autogen_team.infrastructure.messaging.kafka_app.DEFAULT_FASTAPI_HOST]
    [test_kafka_app.py] --> [autogen_team.infrastructure.messaging.kafka_app.DEFAULT_FASTAPI_PORT]
    [test_kafka_app.py] --> [autogen_team.infrastructure.messaging.kafka_app.FastAPIKafkaService]
    [test_kafka_app.py] --> [autogen_team.infrastructure.messaging.kafka_app.PredictionResponse]
    [test_kafka_app.py] --> [autogen_team.infrastructure.messaging.kafka_app.app]
    [test_kafka_app.py] --> [confluent_kafka.KafkaError]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [json] : imports
    [Module] --> [os] : imports
    [Module] --> [signal] : imports
    [Module] --> [typing.Any] : imports
    [Module] --> [typing.Dict] : imports
    [Module] --> [typing.Generator] : imports
    [Module] --> [unittest.mock.MagicMock] : imports
    [Module] --> [unittest.mock.patch] : imports
    [Module] --> [pytest] : imports
    [Module] --> [autogen_team.infrastructure.messaging.kafka_app.DEFAULT_FASTAPI_HOST] : imports
    [Module] --> [autogen_team.infrastructure.messaging.kafka_app.DEFAULT_FASTAPI_PORT] : imports
    [Module] --> [autogen_team.infrastructure.messaging.kafka_app.FastAPIKafkaService] : imports
    [Module] --> [autogen_team.infrastructure.messaging.kafka_app.PredictionResponse] : imports
    [Module] --> [autogen_team.infrastructure.messaging.kafka_app.app] : imports
    [Module] --> [confluent_kafka.KafkaError] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `mock_kafka_service() -> Generator[tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock], None, None]` (Public)
**Description:** Fixture to create a mocked FastAPIKafkaService.

**Inputs:**
- None

**Output:**
- return type: `Generator[tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock], None, None]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = mock_kafka_service()
```

### `test_initialization(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock, Dict[str, Any]]) -> None` (Public)
**Description:** Test FastAPIKafkaService initialization.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock, Dict[str, Any]]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_initialization(...)
```

### `test_delivery_report(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test delivery report logging.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_delivery_report(...)
```

### `test_start_producer_failure(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test start method when producer initialization fails.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_start_producer_failure(...)
```

### `test_start_consumer_failure(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test start method when consumer initialization fails.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_start_consumer_failure(...)
```

### `test_run_server(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test the _run_server method.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_run_server(...)
```

### `test_run_server_failure(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test the _run_server method when uvicorn fails.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_run_server_failure(...)
```

### `test_consume_messages(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test the _consume_messages method.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_consume_messages(...)
```

### `test_consume_messages_with_error(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test _consume_messages handles message errors.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_consume_messages_with_error(...)
```

### `test_poll_message(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test the _poll_message method.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_poll_message(...)
```

### `test_poll_message_no_consumer(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test _poll_message handles missing consumer.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_poll_message_no_consumer(...)
```

### `test_handle_message_error_partition_eof(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test _handle_message_error handles partition EOF.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_handle_message_error_partition_eof(...)
```

### `test_handle_message_error_other_error(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test _handle_message_error handles other Kafka errors.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_handle_message_error_other_error(...)
```

### `test_process_message(mock_json_loads: MagicMock, mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test the _process_message method.

**Inputs:**
- `mock_json_loads`
  - type: MagicMock
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_process_message(..., ...)
```

### `test_process_message_json_decode_error(mock_json_loads: MagicMock, mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test _process_message handles JSON decoding errors.

**Inputs:**
- `mock_json_loads`
  - type: MagicMock
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_process_message_json_decode_error(..., ...)
```

### `test_process_message_prediction_error(mock_json_loads: MagicMock, mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test _process_message handles prediction callback errors.

**Inputs:**
- `mock_json_loads`
  - type: MagicMock
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_process_message_prediction_error(..., ...)
```

### `test_close_consumer(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test the _close_consumer method.

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_close_consumer(...)
```

### `test_stop(mock_os_kill: MagicMock, mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test the stop method.

**Inputs:**
- `mock_os_kill`
  - type: MagicMock
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_stop(..., ...)
```

### `test_main_function() -> None` (Public)
**Description:** Test the main function.

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_main_function()
```

### `test_process_message_producer_none(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test _process_message when producer is None (line 215).

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_process_message_producer_none(...)
```

### `test_process_message_exception_on_produce(mock_kafka_service: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]) -> None` (Public)
**Description:** Test _process_message when produce raises exception (line 219).

**Inputs:**
- `mock_kafka_service`
  - type: tuple[FastAPIKafkaService, MagicMock, MagicMock, MagicMock, MagicMock]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_process_message_exception_on_produce(...)
```

### `test_main_prediction_callback_numpy() -> None` (Public)
**Description:** Test the prediction callback inside main with numpy output.

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_main_prediction_callback_numpy()
```

### `test_main_prediction_callback_error() -> None` (Public)
**Description:** Test the prediction callback inside main when predict fails.

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = test_main_prediction_callback_error()
```

## 7. Call Graph
```plantuml
@startuml
[test_kafka_app] --> [main] : calls
[test_kafka_app] --> [assert_called_once] : calls
[test_kafka_app] --> [assert_called_once_with] : calls
[test_kafka_app] --> [raises] : calls
[test_kafka_app] --> [MagicMock] : calls
[test_kafka_app] --> [_run_server] : calls
[test_kafka_app] --> [is_set] : calls
[test_kafka_app] --> [start] : calls
[test_kafka_app] --> [assert_not_called] : calls
[test_kafka_app] --> [delivery_report] : calls
[test_kafka_app] --> [object] : calls
[test_kafka_app] --> [patch] : calls
[test_kafka_app] --> [_handle_message_error] : calls
[test_kafka_app] --> [stop] : calls
[test_kafka_app] --> [get] : calls
[test_kafka_app] --> [fixture] : calls
[test_kafka_app] --> [_process_message] : calls
[test_kafka_app] --> [PredictionResponse] : calls
[test_kafka_app] --> [callback] : calls
[test_kafka_app] --> [JSONDecodeError] : calls
[test_kafka_app] --> [PredictionRequest] : calls
[test_kafka_app] --> [_close_consumer] : calls
[test_kafka_app] --> [_consume_messages] : calls
[test_kafka_app] --> [Exception] : calls
[test_kafka_app] --> [assert_called] : calls
[test_kafka_app] --> [FastAPIKafkaService] : calls
[test_kafka_app] --> [getpid] : calls
[test_kafka_app] --> [assert_any_call] : calls
[test_kafka_app] --> [_poll_message] : calls
@enduml
```

## 8. Cross References
- **Dependencies:** [Dependencies](../../../../dependencies/index.md)
- **Used by:** None
- **Calls:** main, assert_called_once, assert_called_once_with, raises, MagicMock, _run_server, is_set, start, assert_not_called, delivery_report, object, patch, _handle_message_error, stop, get, fixture, _process_message, PredictionResponse, callback, JSONDecodeError, PredictionRequest, _close_consumer, _consume_messages, Exception, assert_called, FastAPIKafkaService, getpid, assert_any_call, _poll_message
- **Called from:** None
- **Related classes:** [Classes](../../../../classes/index.md)
- **Related diagrams:** [Diagrams](../../../../diagrams/index.md)
