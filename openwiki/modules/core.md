---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: autogen_team.core"
source_path: "src/autogen_team/core/schemas.py"
description: "Pandera dataframe schema definitions, validation checks, and security primitives."
tags: ["core", "schemas", "pandera", "validation"]
last_verified_commit: "main"
timestamp: "2026-07-31T16:40:00Z"
---

# Module Specification: `autogen_team.core`

* **Source File Reference:** `src/autogen_team/core/schemas.py` (Lines: L1-L114)
* **Upstream Dependencies:** `pandas`, `pandera`
* **Downstream Consumers:** [[Modules/Application|autogen_team.application]]

---

## 1. Architectural Role & Responsibilities

The `autogen_team.core` module defines the data schema foundation for the application. Using Pandera DataFrame models, it validates inputs, outputs, targets, SHAP values, and feature importances.

---

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Schema {
        +Config: Config
        +check(data: DataFrame)$ DataFrame
    }
    class InputsSchema {
        +input: Series[String]
    }
    class OutputsSchema {
        +response: Series[String]
        +metadata: Series[Object]
    }
    class TargetsSchema {
        +input_target: Series[String]
        +response: Series[String]
    }
    Schema <|-- InputsSchema : Realization
    Schema <|-- OutputsSchema : Realization
    Schema <|-- TargetsSchema : Realization
```

---

## 3. Schema Class Contracts

### `Schema.check(data: pd.DataFrame)`
- **Source Line Citation:** `src/autogen_team/core/schemas.py:L36-L46`
- **Behavior**: Validates input pandas DataFrame against the declared schema model and returns typed `papd.DataFrame[TSchema]`.
