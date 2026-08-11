---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: send_kafka_test"
source_path: "Scripts/send_kafka_test.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.166652+00:00"
---

# Module Specification: send_kafka_test

* **Source Reference:** `Scripts/send_kafka_test.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to send kafka test.

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

## 3. Architecture & Execution
### Internal Architecture
Not explicitly defined.

### Execution Flow
Not explicitly defined.

### Sequence Explanation
Not explicitly defined.

## 4. UML 2.0 Diagrams
### Class Diagram
```plantuml
@startuml
    ' No classes found in module
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
No description provided.

**Inputs:**
- `err`: Any
- `msg`: Any

**Output:**
- Return Type: `None`

### `main()`
No description provided.

**Inputs:**
- None

**Output:**
- Return Type: `None`
