---
type: class
title: "RegistryRepository"
source_path: "src/autogen_team/registry/repositories.py"
description: "Abstract repository for model registry."
tags: [class]
last_verified_commit: "dc137c3"
---

# RegistryRepository

Source File: `src/autogen_team/registry/repositories.py`

Abstract repository for model registry.

## Architecture Visualization

```mermaid
classDiagram
    class RegistryRepository {
        +register(name, model_uri)
        +promote(name, version, stage)
    }
```
