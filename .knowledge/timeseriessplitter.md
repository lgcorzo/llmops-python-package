---
type: class
title: "TimeSeriesSplitter"
source_path: "src/autogen_team/infrastructure/utils/splitters.py"
description: "Split a dataframe into fixed time series subsets.  Parameters:     gap (int): gap between splits.     n_splits (int): number of split to generate.     test_size (int | float): number or ratio for the test dataset."
tags: [class]
last_verified_commit: "dc137c3"
---

# TimeSeriesSplitter

Source File: `src/autogen_team/infrastructure/utils/splitters.py`

Split a dataframe into fixed time series subsets.  Parameters:     gap (int): gap between splits.     n_splits (int): number of split to generate.     test_size (int | float): number or ratio for the test dataset.

## Architecture Visualization

```mermaid
classDiagram
    class TimeSeriesSplitter {
        +split(inputs, targets, groups)
        +get_n_splits(inputs, targets, groups)
    }
```
