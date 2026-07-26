---
type: class
title: "ModelRepository"
source_path: "src/autogen_team/models/repositories.py"
description: "Abstract repository for model persistence."
tags: [class]
last_verified_commit: "dc137c3"
---

# ModelRepository

Source File: `src/autogen_team/models/repositories.py`

Abstract repository for model persistence.

## Architecture Visualization

```mermaid
classDiagram
    class ModelRepository {
        +save(model, path)
        +load(path)
    }
```
