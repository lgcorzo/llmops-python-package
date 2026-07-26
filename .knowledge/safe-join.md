---
type: api
title: "safe_join"
source_path: "src/autogen_team/core/security.py"
description: "Safely join paths, ensuring the result is within the base directory.  Args:     base (str): The base directory.     *paths (str): Paths to join.  Returns:     str: The joined path.  Raises:     ValueError: If the resolved path is outside the base directory."
tags: [api]
last_verified_commit: "dc137c3"
---

# safe_join

Source File: `src/autogen_team/core/security.py`

Safely join paths, ensuring the result is within the base directory.  Args:     base (str): The base directory.     *paths (str): Paths to join.  Returns:     str: The joined path.  Raises:     ValueError: If the resolved path is outside the base directory.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[realpath]
    call_0 --> call_1[realpath]
    call_1 --> call_2[join]
    call_2 --> call_3[commonpath]
    call_3 --> call_4[ValueError]
    call_4 --> End
```
