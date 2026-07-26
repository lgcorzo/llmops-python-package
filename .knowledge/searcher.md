---
type: class
title: "Searcher"
source_path: "src/autogen_team/infrastructure/utils/searchers.py"
description: "Base class for a searcher.  Use searcher to fine-tune models. i.e., to find the best model params.  Parameters:     param_grid (Grid): mapping of param key -> values."
tags: [class]
last_verified_commit: "dc137c3"
---

# Searcher

Source File: `src/autogen_team/infrastructure/utils/searchers.py`

Base class for a searcher.  Use searcher to fine-tune models. i.e., to find the best model params.  Parameters:     param_grid (Grid): mapping of param key -> values.

## Architecture Visualization

```mermaid
classDiagram
    class Searcher {
        +search(model, metric, inputs, targets, cv)
    }
```
