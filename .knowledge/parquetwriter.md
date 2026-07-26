---
type: class
title: "ParquetWriter"
source_path: "src/autogen_team/data_access/adapters/datasets.py"
description: "Writer a dataframe to a parquet file.  Parameters:     path (str): local or S3 path to the dataset."
tags: [class]
last_verified_commit: "dc137c3"
---

# ParquetWriter

Source File: `src/autogen_team/data_access/adapters/datasets.py`

Writer a dataframe to a parquet file.  Parameters:     path (str): local or S3 path to the dataset.

## Architecture Visualization

```mermaid
classDiagram
    class ParquetWriter {
        +write(data)
    }
```
