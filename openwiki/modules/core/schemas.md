---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Core Schemas"
source_path: "src/autogen_team/core/schemas.py"
description: "Pandera DataFrameModel hierarchy for type-safe data validation across the autogen_team system."
tags: ["core", "schemas", "pandera", "validation"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Module Specification: Core Schemas

* **Source Reference:** `src/autogen_team/core/schemas.py` (Lines: L1-L114)
* **Downstream Consumers:** [[Modules/Models/Entities]], [[Modules/DataAccess/Datasets]], [[Modules/Evaluation/Metrics]], [[Modules/Registry/MlflowAdapter]], [[Modules/Infrastructure/Utils]]

## 1. Architectural Role & Responsibilities

The schemas module defines the shared data contracts for the entire system using **Pandera** `DataFrameModel` classes. All data flowing between layers (training inputs, prediction outputs, SHAP values, feature importances) is validated against these schemas, ensuring type safety and data integrity.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Schema {
        <<abstract>>
        +check(data: DataFrame)$ DataFrame~TSchema~
    }
    class Config {
        +coerce: bool = True
        +strict: bool = True
    }
    class InputsSchema {
        +input: Series~String~
    }
    class OutputsSchema {
        +response: Series~String~
        +metadata: Series~Object~
    }
    class TargetsSchema {
        +input_target: Series~String~
        +response: Series~String~
    }
    class MetadataSchema {
        +timestamp: Series~String~
        +model_version: Series~String~
    }
    class SHAPValuesSchema {
        +sample: Series~String~
        +explanation: Series~String~
        +shap_value: Series~Float32~
    }
    class FeatureImportancesSchema {
        +feature: Series~String~
        +importance: Series~Float32~
    }

    Schema *-- Config
    Schema <|-- InputsSchema : Inheritance
    Schema <|-- OutputsSchema : Inheritance
    Schema <|-- TargetsSchema : Inheritance
    Schema <|-- MetadataSchema : Inheritance
    Schema <|-- SHAPValuesSchema : Inheritance
    Schema <|-- FeatureImportancesSchema : Inheritance
```

## 3. Class & Method Specifications

### `Schema` (`src/autogen_team/core/schemas.py:L18-L46`)

Base class for all dataframe schemas. Extends Pandera's `DataFrameModel` with strict validation and type coercion.

#### Methods

* **`check(cls: Type[TSchema], data: pd.DataFrame) -> papd.DataFrame[TSchema]`** (L36-L46)
  - **Purpose:** Validate a DataFrame against the schema, returning a typed DataFrame.
  - **Inputs:** `data` (`pd.DataFrame`): raw dataframe to validate.
  - **Outputs:** `papd.DataFrame[TSchema]`: validated, typed dataframe.

## 4. Type Aliases

| Alias | Definition | Line |
| :--- | :--- | :--- |
| `Inputs` | `papd.DataFrame[InputsSchema]` | L94 |
| `Targets` | `papd.DataFrame[TargetsSchema]` | L95 |
| `Outputs` | `papd.DataFrame[OutputsSchema]` | L96 |
| `SHAPValues` | `papd.DataFrame[SHAPValuesSchema]` | L97 |
| `FeatureImportances` | `papd.DataFrame[FeatureImportancesSchema]` | L98 |
