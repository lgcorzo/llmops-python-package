---
type: api
title: "parse_file"
source_path: "src/autogen_team/infrastructure/io/configs.py"
description: "Parse a config file from a path.  Args:     path (str): path to local config.  Returns:     Config: representation of the config file."
tags: [api]
last_verified_commit: "dc137c3"
---

# parse_file

Source File: `src/autogen_team/infrastructure/io/configs.py`

Parse a config file from a path.  Args:     path (str): path to local config.  Returns:     Config: representation of the config file.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[load]
    call_0 --> End
```
