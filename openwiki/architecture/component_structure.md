---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "architecture"
title: "ISO 42010 Component View: Subsystems & UML 2.0 Class Diagrams"
description: "Component View detailing Python package layout, class structures, Pandera schemas, and UML 2.0 diagrams."
tags: ["iso42010", "component_view", "uml2", "class_diagram", "pandera", "pydantic"]
timestamp: "2026-07-31T16:40:00Z"
---

# ISO 42010 Component View: Subsystems & UML 2.0 Class Diagrams

## 1. Package Architecture Breakdown

```mermaid
graph TD
    CORE["autogen_team.core (Schemas & Security)"]
    APP["autogen_team.application (Agents, Jobs, Workflows, MCP)"]
    INFRA["autogen_team.infrastructure (Client, IO, Messaging, Orchestration)"]
    DATA["autogen_team.data_access (Entities & Repositories)"]
    EVAL["autogen_team.evaluation (Metrics & Services)"]
    MODELS["autogen_team.models (Entities & Repositories)"]
    REGISTRY["autogen_team.registry (Adapters & Repositories)"]

    APP --> CORE
    APP --> INFRA
    APP --> DATA
    APP --> EVAL
    REGISTRY --> MODELS
    INFRA --> REGISTRY
```

---

## 2. UML 2.0 Class Diagram: Pandera Schemas & Pydantic Settings

```mermaid
classDiagram
    direction BT

    class DataFrameModel {
        <<interface>>
        +validate(data: DataFrame)* DataFrame
    }

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

    class SHAPValuesSchema {
        +sample: Series[String]
        +explanation: Series[String]
        +shap_value: Series[Float32]
    }

    class Settings {
        <<pydantic>>
    }

    class MainSettings {
        +job: JobKind
    }

    DataFrameModel <|-- Schema : Inheritance
    Schema <|-- InputsSchema : Inheritance
    Schema <|-- OutputsSchema : Inheritance
    Schema <|-- TargetsSchema : Inheritance
    Schema <|-- SHAPValuesSchema : Inheritance
    Settings <|-- MainSettings : Inheritance
```

---

## 3. Core Module Specifications

### 1. `autogen_team.core.schemas`
- **Source Line Citation**: `src/autogen_team/core/schemas.py:L18-L98`
- **Purpose**: Defines Pandera DataFrame models (`InputsSchema`, `OutputsSchema`, `TargetsSchema`, `SHAPValuesSchema`, `FeatureImportancesSchema`) enforcing runtime type checks and coercions (`coerce=True`, `strict=True`).

### 2. `autogen_team.settings`
- **Source Line Citation**: `src/autogen_team/settings.py:L13-L29`
- **Purpose**: Provides immutable Pydantic settings (`MainSettings`, `Settings`) configured with `strict=True`, `frozen=True`, and `extra="forbid"`.
