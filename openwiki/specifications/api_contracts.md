---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "api_contracts"
title: "ISO 15289 Specification: Complete API & Schema Specifications"
description: "Specification of Pandera DataFrame models, Pydantic settings, and CLI script parameters."
tags: ["iso15289", "api", "contracts", "schemas", "pandera"]
timestamp: "2026-07-31T16:40:00Z"
---

# ISO 15289 Specification: Complete API & Schema Specifications

## 1. Pandera DataFrame Schemas (`autogen_team.core.schemas`)

### 1. `Schema` (Base Model)
- **Source Citation**: `src/autogen_team/core/schemas.py:L18-L47`
- **Method**: `check(cls: Type[TSchema], data: pd.DataFrame) -> papd.DataFrame[TSchema]`

### 2. `InputsSchema`
- **Source Citation**: `src/autogen_team/core/schemas.py:L56-L60`
- **Fields**: `input: Series[String]`

### 3. `OutputsSchema`
- **Source Citation**: `src/autogen_team/core/schemas.py:L62-L67`
- **Fields**: `response: Series[String]`, `metadata: Series[Object]`

### 4. `TargetsSchema`
- **Source Citation**: `src/autogen_team/core/schemas.py:L69-L74`
- **Fields**: `input_target: Series[String]`, `response: Series[String]`

### 5. `SHAPValuesSchema`
- **Source Citation**: `src/autogen_team/core/schemas.py:L76-L85`
- **Fields**: `sample: Series[String]`, `explanation: Series[String]`, `shap_value: Series[Float32]`

---

## 2. Application Settings (`autogen_team.settings`)

### `MainSettings` Struct
- **Source Citation**: `src/autogen_team/settings.py:L21-L29`
- **Field**: `job: JobKind` (discriminator `"KIND"`)
