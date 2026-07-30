---
type: "module-architecture"
title: "Core Architecture: src/autogen_team/core"
description: "Technical architecture and class hierarchy for core schemas and security utilities"
tags: ["architecture", "uml", "pyreverse", "openwiki", "core", "schemas"]
timestamp: "2026-07-30T00:00:00Z"
---

# Module Name: core

* **Source Directory Reference:** `src/autogen_team/core/`
* **Package Dependency:** Upstream: `pandera`, `pandas`, `pydantic`. Downstream: `src/autogen_team/models/`, `src/autogen_team/application/`, `src/autogen_team/data_access/`.

## 1. Executive Summary & Purpose

The `core` module establishes the strict type contracts, schema definitions, and file-system security utilities for the entire repository. It uses `pandera.DataFrameModel` to enforce runtime validation on inputs, targets, predictions, SHAP values, metadata, and feature importances. Additionally, it provides path-traversal prevention via `safe_join()`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)

The following class diagram derived from local AST analysis models the Pandera dataframe schema inheritance tree:

```mermaid
classDiagram
    direction BT
    class DataFrameModel {
        <<external: pandera>>
    }
    class Schema {
        <<abstract>>
        +check(data: DataFrame)* DataFrame
    }
    class MetadataSchema {
        +timestamp: Series[String]
        +model_version: Series[String]
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
    class SHAPValuesSchema {
        +sample: Series[String]
        +explanation: Series[String]
        +shap_value: Series[Float32]
    }
    class FeatureImportancesSchema {
        +feature: Series[String]
        +importance: Series[Float32]
    }

    DataFrameModel <|-- Schema : Inherits Pandera DataFrameModel
    Schema <|-- MetadataSchema
    Schema <|-- InputsSchema
    Schema <|-- OutputsSchema
    Schema <|-- TargetsSchema
    Schema <|-- SHAPValuesSchema
    Schema <|-- FeatureImportancesSchema
```

## 3. Package & Class Relations

* **Inheritance & Validation:** `Schema` inherits from `pandera.DataFrameModel`. All data schemas (`InputsSchema`, `OutputsSchema`, `TargetsSchema`, `SHAPValuesSchema`, `FeatureImportancesSchema`, `MetadataSchema`) specialize `Schema` with strict column definitions and coercions.
* **Security Layer:** `src/autogen_team/core/security.py` defines `safe_join(base: str, *paths: str) -> str`, which guards against directory traversal attacks by validating path commonalities.

## 4. Execution Flow & Runtime Behavior

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Model / Pipeline Component
    participant SchemaCls as InputsSchema / OutputsSchema
    participant Pandera as Pandera Validator
    participant Security as safe_join Security Guard

    Caller->>Security: safe_join("/base/dir", "target/file.txt")
    Note over Security: Verifies realpath prefix matches base
    Security-->>Caller: Returns safe path

    Caller->>SchemaCls: check(dataframe)
    SchemaCls->>Pandera: validate(data, coerce=True, strict=True)
    Pandera-->>SchemaCls: Validated DataFrame
    SchemaCls-->>Caller: Returns papd.DataFrame[TSchema]
```

---

* **Source Citations:**
  * Base Schema Class: `src/autogen_team/core/schemas.py:18-47`
  * Data Schemas (`InputsSchema`, `OutputsSchema`, etc.): `src/autogen_team/core/schemas.py:49-98`
  * Security `safe_join`: `src/autogen_team/core/security.py:6-26`
