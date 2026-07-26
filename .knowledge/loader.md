---
type: class
title: "Loader"
source_path: "src/autogen_team/registry/adapters/mlflow_adapter.py"
description: "Base class for loading models from registry.  Separate model definition from deserialization. e.g., to switch between deserialization flavors."
tags: [class]
last_verified_commit: "dc137c3"
---

# Loader

Source File: `src/autogen_team/registry/adapters/mlflow_adapter.py`

Base class for loading models from registry.  Separate model definition from deserialization. e.g., to switch between deserialization flavors.

## Architecture Visualization

```mermaid
classDiagram
    class Loader {
        +load(uri)
    }
```
