---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Schemas"
source_path: "src/autogen_team/core/schemas.py"
description: "Exhaustive functional summary for Schemas."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---
# Module Specification: Core Schemas

* **Source Reference:** `src/autogen_team/core/schemas.py` (Lines: L1-L114)
* **Downstream Consumers:** [[Modules/Models/Entities]], [[Modules/DataAccess/Datasets]], [[Modules/Evaluation/Metrics]], [[Modules/Registry/MlflowAdapter]], [[Modules/Infrastructure/Utils]]

## 1. Architectural Role & Responsibilities

The schemas module defines the shared data contracts for the entire system using **Pandera** `DataFrameModel` classes. All data flowing between layers (training inputs, prediction outputs, SHAP values, feature importances) is validated against these schemas, ensuring type safety and data integrity.

## 2. UML 2.0 Class Diagram


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

```mermaid
classDiagram
    class Config {
        +bool coerce
        +bool strict
    }
    class Config {
        +bool strict
    }
    class FeatureImportancesSchema {
        +papd.Series[padt.String] feature
        +papd.Series[padt.Float32] importance
    }
    class InputsSchema {
        +papd.Series[padt.String] input
    }
    class MetadataSchema {
        +papd.Series[padt.String] model_version
        +papd.Series[padt.String] timestamp
    }
    class OutputsSchema {
        +papd.Series[padt.Object] metadata
        +papd.Series[padt.String] response
    }
    class SHAPValuesSchema {
        +papd.Series[padt.String] explanation
        +papd.Series[padt.String] sample
        +papd.Series[padt.Float32] shap_value
    }
    class Schema {
        +check(data: pd.DataFrame): papd.DataFrame[TSchema]
    }
    class TargetsSchema {
        +papd.Series[padt.String] input_target
        +papd.Series[padt.String] response
    }
    Schema <|-- FeatureImportancesSchema
    Schema <|-- InputsSchema
    Schema <|-- MetadataSchema
    Schema <|-- OutputsSchema
    Schema <|-- SHAPValuesSchema
    Schema <|-- TargetsSchema
```
