---
type: class
title: "Model"
source_path: "src/autogen_team/models/entities.py"
description: "Base class for a project model.  Use a model to adapt AI/ML frameworks. e.g., to swap easily one model with another."
tags: [class]
last_verified_commit: "dc137c3"
---

# Model

Source File: `src/autogen_team/models/entities.py`

Base class for a project model.  Use a model to adapt AI/ML frameworks. e.g., to swap easily one model with another.

## Architecture Visualization

```mermaid
classDiagram
    class Model {
        +get_params(deep)
        +set_params()
        +load_context(model_config)
        +fit(inputs, targets)
        +predict(inputs)
        +explain_model()
        +explain_samples(inputs)
        +get_internal_model()
    }
```
