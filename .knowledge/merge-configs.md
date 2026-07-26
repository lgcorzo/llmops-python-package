---
type: api
title: "merge_configs"
source_path: "src/autogen_team/infrastructure/io/configs.py"
description: "Merge a list of config into a single config.  Args:     configs (T.Sequence[Config]): list of configs.  Returns:     Config: representation of the merged config objects."
tags: [api]
last_verified_commit: "dc137c3"
---

# merge_configs

Source File: `src/autogen_team/infrastructure/io/configs.py`

Merge a list of config into a single config.  Args:     configs (T.Sequence[Config]): list of configs.  Returns:     Config: representation of the merged config objects.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[merge]
    call_0 --> End
```
