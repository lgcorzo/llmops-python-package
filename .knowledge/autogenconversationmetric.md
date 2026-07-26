---
type: class
title: "AutogenConversationMetric"
source_path: "src/autogen_team/evaluation/metrics/metrics.py"
description: "Evaluate conversation quality metrics for Autogen interactions.  Parameters:     check_termination (bool): Verify if conversation reached termination     check_error_messages (bool): Check for error messages in output"
tags: [class]
last_verified_commit: "dc137c3"
---

# AutogenConversationMetric

Source File: `src/autogen_team/evaluation/metrics/metrics.py`

Evaluate conversation quality metrics for Autogen interactions.  Parameters:     check_termination (bool): Verify if conversation reached termination     check_error_messages (bool): Check for error messages in output

## Architecture Visualization

```mermaid
classDiagram
    class AutogenConversationMetric {
        +score(targets, outputs)
    }
```
