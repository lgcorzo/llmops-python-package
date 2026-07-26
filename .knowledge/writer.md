---
type: class
title: "Writer"
source_path: "src/autogen_team/data_access/adapters/datasets.py"
description: "Base class for a dataset writer.  Use a writer to save a dataset from memory. e.g., to write file, database, cloud storage, ..."
tags: [class]
last_verified_commit: "dc137c3"
---

# Writer

Source File: `src/autogen_team/data_access/adapters/datasets.py`

Base class for a dataset writer.  Use a writer to save a dataset from memory. e.g., to write file, database, cloud storage, ...

## Architecture Visualization

```mermaid
classDiagram
    class Writer {
        +write(data)
    }
```
