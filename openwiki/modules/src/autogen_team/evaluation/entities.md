---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: entities"
source_path: "src/autogen_team/evaluation/entities.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-28T06:32:33.064773+00:00"
---

# Module Specification: entities

* **Source Reference:** `src/autogen_team/evaluation/entities.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to entities.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `dataclasses.dataclass`

**Exported Classes:**
- `MetricResult`

**Exported Functions:**
- None

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
    class MetricResult {
    }
@enduml
```

### Package Diagram
```plantuml
@startuml
    package "src" {
        package "autogen_team" {
            package "evaluation" {
                [entities.py]
            }
        }
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    ' No functions for sequence
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Infrastructure/Other" {
        [entities.py]
    }
    [entities.py] --> [dataclasses.dataclass]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [dataclasses.dataclass] : imports
@enduml
```

## 5. Class & Method Specifications
### `MetricResult` ([`src/autogen_team/evaluation/entities.py`](/src/autogen_team/evaluation/entities.py))
#### Overview
Represents a metric evaluation result.

#### Attributes
- None found.

#### Methods
## 6. Module Functions
## 7. Call Graph
- No public API calls detected.

## 8. Cross References
- **Dependencies:** [Dependencies](../../../../dependencies/index.md)
- **Used by:** None
- **Calls:** None
- **Called from:** None
- **Related classes:** [Classes](../../../../classes/index.md)
- **Related diagrams:** [Diagrams](../../../../diagrams/index.md)
