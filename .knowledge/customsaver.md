---
type: class
title: "CustomSaver"
source_path: "src/autogen_team/registry/adapters/mlflow_adapter.py"
description: "Saver for project models using the Mlflow PyFunc module.  https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html https://mlflow.org/blog/autogen-image-agent https://mlflow.org/blog/custom-pyfunc"
tags: [class]
last_verified_commit: "dc137c3"
---

# CustomSaver

Source File: `src/autogen_team/registry/adapters/mlflow_adapter.py`

Saver for project models using the Mlflow PyFunc module.  https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html https://mlflow.org/blog/autogen-image-agent https://mlflow.org/blog/custom-pyfunc

## Architecture Visualization

```mermaid
classDiagram
    class CustomSaver {
        +save(model, signature, input_example)
    }
```
