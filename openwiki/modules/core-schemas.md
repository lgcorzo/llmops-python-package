---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Core-Schemas"
source_path: "src/autogen_team/"
description: "Documentation for Core-Schemas."
tags: ["core", "okf"]
timestamp: "2024-05-22T12:00:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: ""
---

# Core Schemas
The core schema module defines the fundamental data structures used throughout the application. It utilizes `pandera` to ensure strict typing and validation for DataFrames, which are central to the machine learning pipeline.

## Schema Overview
The following mermaid diagram shows the inheritance hierarchy of the schemas:

```mermaid
classDiagram
    Schema <|-- MetadataSchema
    Schema <|-- InputsSchema
    Schema <|-- OutputsSchema
    Schema <|-- TargetsSchema
    Schema <|-- SHAPValuesSchema
    Schema <|-- FeatureImportancesSchema

    class Schema {
        <<Abstract>>
        +classmethod check(data: pd.DataFrame)
    }
    class MetadataSchema {
        +timestamp: String
        +model_version: String
    }
    class InputsSchema {
        +input: String
    }
    class OutputsSchema {
        +response: String
        +metadata: Object
    }
    class TargetsSchema {
        +input_target: String
        +response: String
    }
    class SHAPValuesSchema {
        +sample: String
        +explanation: String
        +shap_value: Float32
    }
    class FeatureImportancesSchema {
        +feature: String
        +importance: Float32
    }
```

## Detailed Explanations
- **`Schema`**: The base class for all data validations. It uses `pandera.DataFrameModel` to enforce consistency during the ingestion of raw model outputs.
- **`Inputs` / `Targets`**: These are specific types (wrapped in `pandera.DataFrame`) that represent the training data and desired results respectively.
- **`SHAPValuesSchema` & `FeatureImportancesSchema`**: These schemas are specifically designed to hold explainability data, ensuring that model "interpretability" results are structured correctly for downstream analysis.

*Refer to: `src/autogen_team/core/schemas.py`*
