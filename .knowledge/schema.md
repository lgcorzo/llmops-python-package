---
type: class
title: "Schema"
source_path: "src/autogen_team/core/schemas.py"
description: "Base class for a dataframe schema.  Use a schema to type your dataframe object. e.g., to communicate and validate its fields."
tags: [class]
last_verified_commit: "dc137c3"
---

# Schema

Source File: `src/autogen_team/core/schemas.py`

Base class for a dataframe schema.  Use a schema to type your dataframe object. e.g., to communicate and validate its fields.

## Architecture Visualization

```mermaid
classDiagram
    class Schema {
        +check(cls, data)
    }
```
