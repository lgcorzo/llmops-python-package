---
type: class
title: "GridCVSearcher"
source_path: "src/autogen_team/infrastructure/utils/searchers.py"
description: "Grid searcher with cross-fold validation.  Convention: metric returns higher values for better models.  Parameters:     n_jobs (int, optional): number of jobs to run in parallel.     refit (bool): refit the model after the tuning.     verbose (int): set the searcher verbosity level.     error_score (str | float): strategy or value on error.     return_train_score (bool): include train scores if True."
tags: [class]
last_verified_commit: "dc137c3"
---

# GridCVSearcher

Source File: `src/autogen_team/infrastructure/utils/searchers.py`

Grid searcher with cross-fold validation.  Convention: metric returns higher values for better models.  Parameters:     n_jobs (int, optional): number of jobs to run in parallel.     refit (bool): refit the model after the tuning.     verbose (int): set the searcher verbosity level.     error_score (str | float): strategy or value on error.     return_train_score (bool): include train scores if True.

## Architecture Visualization

```mermaid
classDiagram
    class GridCVSearcher {
        +search(model, metric, inputs, targets, cv)
    }
```
