---
type: class
title: "AutogenMetric"
source_path: "src/autogen_team/evaluation/metrics/metrics.py"
description: "Evaluate text-based Autogen responses using conversation metrics.  Parameters:     metric_type (str): Type of text metric (exact_match, similarity, length_ratio)     similarity_threshold (float): Minimum similarity score for partial matches"
tags: [class]
last_verified_commit: "dc137c3"
---

# AutogenMetric

Source File: `src/autogen_team/evaluation/metrics/metrics.py`

Evaluate text-based Autogen responses using conversation metrics.  Parameters:     metric_type (str): Type of text metric (exact_match, similarity, length_ratio)     similarity_threshold (float): Minimum similarity score for partial matches

## Architecture Visualization

```mermaid
classDiagram
    class AutogenMetric {
        +score(targets, outputs)
        #_exact_match_score(y_true, y_pred)
        #_similarity_score(y_true, y_pred)
        #_length_ratio(y_true, y_pred)
    }
```
