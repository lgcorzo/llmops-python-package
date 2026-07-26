---
type: class
title: "Threshold"
source_path: "src/autogen_team/evaluation/metrics/metrics.py"
description: "A project threshold for a metric.  Use thresholds to monitor model performances. e.g., to trigger an alert when a threshold is met.  Parameters:     threshold (int | float): absolute threshold value.     greater_is_better (bool): maximize or minimize result."
tags: [class]
last_verified_commit: "dc137c3"
---

# Threshold

Source File: `src/autogen_team/evaluation/metrics/metrics.py`

A project threshold for a metric.  Use thresholds to monitor model performances. e.g., to trigger an alert when a threshold is met.  Parameters:     threshold (int | float): absolute threshold value.     greater_is_better (bool): maximize or minimize result.

## Architecture Visualization

```mermaid
classDiagram
    class Threshold {
        +to_mlflow()
    }
```
