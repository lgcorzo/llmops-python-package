---
type: class
title: "MlflowService"
source_path: "src/autogen_team/infrastructure/services/mlflow_service.py"
description: "Service for Mlflow tracking and registry."
tags: [class]
last_verified_commit: "dc137c3"
---

# MlflowService

Source File: `src/autogen_team/infrastructure/services/mlflow_service.py`

Service for Mlflow tracking and registry.

## Architecture Visualization

```mermaid
classDiagram
    class MlflowService {
        +start()
        +run_context(run_config)
        +client()
    }
```
