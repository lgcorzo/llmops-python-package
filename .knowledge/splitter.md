---
type: class
title: "Splitter"
source_path: "src/autogen_team/infrastructure/utils/splitters.py"
description: "Base class for a splitter.  Use splitters to split data in sets. e.g., split between a train/test subsets.  # https://scikit-learn.org/stable/glossary.html#term-CV-splitter"
tags: [class]
last_verified_commit: "dc137c3"
---

# Splitter

Source File: `src/autogen_team/infrastructure/utils/splitters.py`

Base class for a splitter.  Use splitters to split data in sets. e.g., split between a train/test subsets.  # https://scikit-learn.org/stable/glossary.html#term-CV-splitter

## Architecture Visualization

```mermaid
classDiagram
    class Splitter {
        +split(inputs, targets, groups)
        +get_n_splits(inputs, targets, groups)
    }
```
