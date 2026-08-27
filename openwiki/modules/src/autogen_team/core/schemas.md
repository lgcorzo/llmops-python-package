---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: schemas"
source_path: "src/autogen_team/core/schemas.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-27T07:00:19.348998+00:00"
---

# Module Specification: schemas

* **Source Reference:** `src/autogen_team/core/schemas.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to schemas.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Manages operations and logic for schemas.

**Main Workflow:**
- Executes the primary flow defined by schemas functions and classes.

## 2. Dependencies
**Imports:**
- `typing`
- `pandas`
- `pandera`
- `pandera.typing`
- `pandera.typing.common`

**Exported Classes:**
- `Schema`
- `MetadataSchema`
- `InputsSchema`
- `OutputsSchema`
- `TargetsSchema`
- `SHAPValuesSchema`
- `FeatureImportancesSchema`

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
    class Schema {
        +check() : papd.DataFrame[TSchema]
    }
    class MetadataSchema {
    }
    class InputsSchema {
    }
    class OutputsSchema {
    }
    class TargetsSchema {
    }
    class SHAPValuesSchema {
    }
    class FeatureImportancesSchema {
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
        [schemas.py]
    }
    [schemas.py] --> [typing]
    [schemas.py] --> [pandas]
    [schemas.py] --> [pandera]
    [schemas.py] --> [pandera.typing]
    [schemas.py] --> [pandera.typing.common]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [typing] : imports
    [Module] --> [pandas] : imports
    [Module] --> [pandera] : imports
    [Module] --> [pandera.typing] : imports
    [Module] --> [pandera.typing.common] : imports
@enduml
```

## 5. Class & Method Specifications
### `Schema` ([`src/autogen_team/core/schemas.py`](/src/autogen_team/core/schemas.py))
#### Overview
Base class for a dataframe schema.

Use a schema to type your dataframe object.
e.g., to communicate and validate its fields.

#### Attributes
- None found.

#### Methods
##### `check(cls: T.Type[TSchema], data: pd.DataFrame) -> papd.DataFrame[TSchema]` (Public)
**Description:** Check the dataframe with this schema.

Args:
    data (pd.DataFrame): dataframe to check.

Returns:
    papd.DataFrame[TSchema]: validated dataframe.

**Inputs:**
- `cls`
  - type: T.Type[TSchema]
  - meaning: Represents the cls parameter.
  - valid values: Any valid T.Type[TSchema].
  - optional?: False
  - default value: None
- `data`
  - type: pd.DataFrame
  - meaning: Represents the data parameter.
  - valid values: Any valid pd.DataFrame.
  - optional?: False
  - default value: None

**Output:**
- return type: `papd.DataFrame[TSchema]`
- semantic meaning: Returns the result of check.
- possible null values: Yes, if papd.DataFrame[TSchema] allows it.
- exceptions: Standard execution exceptions.

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
result = Schema.check(..., ...)
```

### `MetadataSchema` ([`src/autogen_team/core/schemas.py`](/src/autogen_team/core/schemas.py))
#### Overview
Schema for metadata in outputs.

#### Attributes
- None found.

#### Methods
### `InputsSchema` ([`src/autogen_team/core/schemas.py`](/src/autogen_team/core/schemas.py))
#### Overview
Schema for validating large string inputs.

#### Attributes
- None found.

#### Methods
### `OutputsSchema` ([`src/autogen_team/core/schemas.py`](/src/autogen_team/core/schemas.py))
#### Overview
Schema for structured JSON outputs.

#### Attributes
- None found.

#### Methods
### `TargetsSchema` ([`src/autogen_team/core/schemas.py`](/src/autogen_team/core/schemas.py))
#### Overview
Schema for the project target.

#### Attributes
- None found.

#### Methods
### `SHAPValuesSchema` ([`src/autogen_team/core/schemas.py`](/src/autogen_team/core/schemas.py))
#### Overview
Schema for SHAP values.

#### Attributes
- None found.

#### Methods
### `FeatureImportancesSchema` ([`src/autogen_team/core/schemas.py`](/src/autogen_team/core/schemas.py))
#### Overview
Schema for feature importances.

#### Attributes
- None found.

#### Methods
## 6. Module Functions
## 7. Call Graph
```plantuml
@startuml
[schemas] --> [check] : calls
[schemas] --> [print] : calls
[schemas] --> [validate] : calls
[schemas] --> [Field] : calls
[schemas] --> [cast] : calls
[schemas] --> [TypeVar] : calls
[schemas] --> [DataFrame] : calls
@enduml
```

## 8. Cross References
- **Parent module:** __init__.md
- **Child modules:** None
- **Dependencies:** `pandas`, `pandera`, `typing`, `pandera.typing.common`, `pandera.typing`
- **Used by:** None
- **Calls:** check, print, validate, Field, cast, TypeVar, DataFrame
- **Called from:** None
- **Related classes:** [Classes](../../../../classes/index.md)
- **Related interfaces:** Not explicitly defined.
- **Related diagrams:** [Diagrams](../../../../diagrams/index.md)
