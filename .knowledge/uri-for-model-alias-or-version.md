---
type: api
title: "uri_for_model_alias_or_version"
source_path: "src/autogen_team/registry/adapters/mlflow_adapter.py"
description: "Create a model URi from a model name and an alias or version.  Args:     name (str): name of the mlflow registered model.     alias_or_version (str | int): alias or version of the registered model.  Returns:     str: model URI as "models:/name@alias" or "models:/name/version" based on input."
tags: [api]
last_verified_commit: "dc137c3"
---

# uri_for_model_alias_or_version

Source File: `src/autogen_team/registry/adapters/mlflow_adapter.py`

Create a model URi from a model name and an alias or version.  Args:     name (str): name of the mlflow registered model.     alias_or_version (str | int): alias or version of the registered model.  Returns:     str: model URI as "models:/name@alias" or "models:/name/version" based on input.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[isinstance]
    call_0 --> call_1[uri_for_model_version]
    call_1 --> call_2[uri_for_model_alias]
    call_2 --> call_3[str]
    call_3 --> End
```
