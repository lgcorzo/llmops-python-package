---
type: "module-architecture"
title: "Registry Architecture: src/autogen_team/registry"
description: "Technical architecture and class hierarchy for model registry, MLflow tracking, and metadata entities"
tags: ["architecture", "registry", "mlflow", "models", "openwiki"]
timestamp: "2026-07-30T00:00:00Z"
---

# Module Name: registry

* **Source Directory Reference:** `src/autogen_team/registry/`
* **Package Dependency:** Upstream: `mlflow`, `pydantic`, `src/autogen_team/models/`. Downstream: `src/autogen_team/application/jobs/promotion.py`, `src/autogen_team/infrastructure/services/mlflow_service.py`.

## 1. Executive Summary & Purpose

The `registry` module manages model versioning, artifact registration, run metadata logging, and stage transitions (Staging, Production, Archived). It defines `RegistryRepository` interface, `MlflowAdapter` implementation, and entity representations for model metadata.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)

```mermaid
classDiagram
    direction BT
    class ABC {
        <<external: abc>>
    }
    class RegistryRepository {
        <<interface>>
        +register_model(model_name, model_uri)* ModelVersion
        +transition_stage(model_name, version, stage)* None
        +get_latest_version(model_name, stage)* ModelVersion
    }
    class MlflowAdapter {
        +tracking_uri: str
        +register_model(model_name, model_uri) ModelVersion
        +transition_stage(model_name, version, stage) None
        +get_latest_version(model_name, stage) ModelVersion
    }
    class RegisteredModelEntity {
        +name: str
        +latest_versions: list
    }
    class ModelVersionEntity {
        +name: str
        +version: str
        +current_stage: str
        +source: str
    }

    ABC <|-- RegistryRepository
    RegistryRepository <|-- MlflowAdapter
```

## 3. Package & Class Relations

* **Registry Abstraction (`RegistryRepository`):** Provides model registration APIs decoupled from the specific underlying registry provider.
* **MLflow Integration (`MlflowAdapter`):** Interacts with MLflow Tracking Server (`mlflow.tracking.MlflowClient`) to register trained models, tag run artifacts, promote models to Production, and retrieve staged versions.

## 4. Execution Flow & Runtime Behavior

```mermaid
sequenceDiagram
    autonumber
    participant Job as Promotion Job
    participant Adapter as MlflowAdapter
    participant MLflow as MLflow Tracking Server

    Job->>Adapter: register_model("autogen_team_model", "runs:/12345/model")
    Adapter->>MLflow: create_model_version(name, source, run_id)
    MLflow-->>Adapter: ModelVersion Metadata
    Adapter-->>Job: ModelVersionEntity

    Job->>Adapter: transition_stage("autogen_team_model", "1", "Production")
    Adapter->>MLflow: transition_model_version_stage(...)
    MLflow-->>Adapter: Stage Updated
    Adapter-->>Job: Success
```

---

* **Source Citations:**
  * Registry Repository Interface: `src/autogen_team/registry/repositories.py:1-25`
  * MLflow Adapter Implementation: `src/autogen_team/registry/adapters/mlflow_adapter.py:1-40`
  * Registry Entities: `src/autogen_team/registry/entities.py:1-30`
