---
type: class
title: "TrainTestSplitter"
source_path: "src/autogen_team/infrastructure/utils/splitters.py"
description: "Split a dataframe into a train and test set.  Parameters:     shuffle (bool): shuffle the dataset. Default is False.     test_size (int | float): number/ratio for the test set.     random_state (int): random state for the splitter object."
tags: [class]
last_verified_commit: "dc137c3"
---

# TrainTestSplitter

Source File: `src/autogen_team/infrastructure/utils/splitters.py`

Split a dataframe into a train and test set.  Parameters:     shuffle (bool): shuffle the dataset. Default is False.     test_size (int | float): number/ratio for the test set.     random_state (int): random state for the splitter object.

## Architecture Visualization

```mermaid
classDiagram
    class TrainTestSplitter {
        +split(inputs, targets, groups)
        +get_n_splits(inputs, targets, groups)
    }
```
