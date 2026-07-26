---
type: class
title: "BaselineAutogenModel"
source_path: "src/autogen_team/models/entities.py"
description: "Simple baseline model based on autogen. https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/group-chat.html Parameters:     max_tokens (int): maximum token of the prompt     temperature (float): temperature for the sampling"
tags: [class]
last_verified_commit: "dc137c3"
---

# BaselineAutogenModel

Source File: `src/autogen_team/models/entities.py`

Simple baseline model based on autogen. https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/group-chat.html Parameters:     max_tokens (int): maximum token of the prompt     temperature (float): temperature for the sampling

## Architecture Visualization

```mermaid
classDiagram
    class BaselineAutogenModel {
        +model_config_path
        +model_config_data
        +max_tokens
        +temperature
        -__init__(model_config_path, model_config_data, max_tokens, temperature)
        +load_context_path(model_config_path)
        +load_context(model_config)
        +fit(inputs, targets)
        #_rungroupchat(content)
        +predict(inputs)
        +get_internal_model()
        +explain_model()
        +explain_samples(inputs)
        -__getstate__()
        -__setstate__(state)
    }
```
