---
type: class
title: "ParquetReader"
source_path: "src/autogen_team/data_access/adapters/datasets.py"
description: "Read a dataframe from a parquet file.  Parameters:     path (str): local path to the dataset."
tags: [class]
last_verified_commit: "dc137c3"
---

# ParquetReader

Source File: `src/autogen_team/data_access/adapters/datasets.py`

Read a dataframe from a parquet file.  Parameters:     path (str): local path to the dataset.

## Architecture Visualization

```mermaid
classDiagram
    class ParquetReader {
        +read()
        +lineage(name, data, targets, predictions)
    }
```
