---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: send_kafka_test"
source_path: "Scripts/send_kafka_test.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-27T07:00:19.422330+00:00"
---

# Module Specification: send_kafka_test

* **Source Reference:** `Scripts/send_kafka_test.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to send kafka test.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Manages operations and logic for send kafka test.

**Main Workflow:**
- Executes the primary flow defined by send kafka test functions and classes.

## 2. Dependencies
**Imports:**
- `json`
- `os`
- `time`
- `typing.Any`
- `typing.Dict`
- `typing.cast`
- `uuid`
- `confluent_kafka.Consumer`
- `confluent_kafka.Producer`

**Exported Classes:**
- None

**Exported Functions:**
- `delivery_report`
- `main`

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

### Sequence Diagram
```plantuml
@startuml
    delivery_report -> print : call
    delivery_report -> topic : call
    delivery_report -> partition : call
    main -> format : call
    main -> value : call
    main -> close : call
    main -> print : call
    main -> Producer : call
    main -> flush : call
    main -> error : call
    main -> produce : call
    main -> cast : call
    main -> dumps : call
    main -> subscribe : call
    main -> poll : call
    main -> decode : call
    main -> uuid4 : call
    main -> encode : call
    main -> time : call
    main -> Consumer : call
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Infrastructure/Other" {
        [send_kafka_test.py]
    }
    [send_kafka_test.py] --> [json]
    [send_kafka_test.py] --> [os]
    [send_kafka_test.py] --> [time]
    [send_kafka_test.py] --> [typing.Any]
    [send_kafka_test.py] --> [typing.Dict]
    [send_kafka_test.py] --> [typing.cast]
    [send_kafka_test.py] --> [uuid]
    [send_kafka_test.py] --> [confluent_kafka.Consumer]
    [send_kafka_test.py] --> [confluent_kafka.Producer]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [json] : imports
    [Module] --> [os] : imports
    [Module] --> [time] : imports
    [Module] --> [typing.Any] : imports
    [Module] --> [typing.Dict] : imports
    [Module] --> [typing.cast] : imports
    [Module] --> [uuid] : imports
    [Module] --> [confluent_kafka.Consumer] : imports
    [Module] --> [confluent_kafka.Producer] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `delivery_report(err: Any, msg: Any)`
Executes the delivery report operation.

**Inputs:**
- `err`
  - type: Any
  - meaning: Represents the err parameter.
  - valid values: Any valid Any.
  - optional?: False
  - default value: None
- `msg`
  - type: Any
  - meaning: Represents the msg parameter.
  - valid values: Any valid Any.
  - optional?: False
  - default value: None

**Output:**
- return type: `None`
- semantic meaning: Returns the result of delivery report.
- possible null values: Yes, if None allows it.
- exceptions: Standard execution exceptions.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

### `main()`
Executes the main operation.

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Returns the result of main.
- possible null values: Yes, if None allows it.
- exceptions: Standard execution exceptions.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

## 7. Call Graph
```plantuml
@startuml
[send_kafka_test] --> [getenv] : calls
[send_kafka_test] --> [print] : calls
[send_kafka_test] --> [flush] : calls
[send_kafka_test] --> [error] : calls
[send_kafka_test] --> [partition] : calls
[send_kafka_test] --> [topic] : calls
[send_kafka_test] --> [subscribe] : calls
[send_kafka_test] --> [poll] : calls
[send_kafka_test] --> [time] : calls
[send_kafka_test] --> [produce] : calls
[send_kafka_test] --> [main] : calls
[send_kafka_test] --> [decode] : calls
[send_kafka_test] --> [uuid4] : calls
[send_kafka_test] --> [value] : calls
[send_kafka_test] --> [cast] : calls
[send_kafka_test] --> [format] : calls
[send_kafka_test] --> [close] : calls
[send_kafka_test] --> [Producer] : calls
[send_kafka_test] --> [dumps] : calls
[send_kafka_test] --> [encode] : calls
[send_kafka_test] --> [Consumer] : calls
@enduml
```

## 8. Cross References
- **Parent module:** None
- **Child modules:** None
- **Dependencies:** `confluent_kafka.Consumer`, `os`, `typing.cast`, `typing.Dict`, `uuid`, `typing.Any`, `json`, `confluent_kafka.Producer`, `time`
- **Used by:** None
- **Calls:** getenv, print, flush, error, partition, topic, subscribe, poll, time, produce, main, decode, uuid4, value, cast, format, close, Producer, dumps, encode, Consumer
- **Called from:** verify_agent_mcp.md, ../src/autogen_team/__main__.md, ../tests/infrastructure/messaging/test_kafka_app.md, ../tests/evaluation/metrics/test_metrics.md, ../skills/validate/scripts/convert_links.md, ../src/autogen_team/infrastructure/messaging/kafka_app.md, ../tests/test_scripts.md, ../tests/registry/adapters/test_security_mlflow_adapter.md, test_mcp_client_simple.md, run_hatchet_worker.md, trigger_mission.md, ../tests/repro_kafka_log.md, ../skills/validate/scripts/okf_validate.md
- **Related classes:** [Classes](../../classes/index.md)
- **Related interfaces:** Not explicitly defined.
- **Related diagrams:** [Diagrams](../../diagrams/index.md)
