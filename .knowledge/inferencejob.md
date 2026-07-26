---
type: class
title: "InferenceJob"
source_path: "src/autogen_team/application/jobs/inference.py"
description: "Generate batch predictions from a registered model.  Parameters:     inputs (datasets.ReaderKind): reader for the inputs data.     outputs (datasets.WriterKind): writer for the outputs data.     alias_or_version (str | int): alias or version for the  model.     loader (registries.LoaderKind): registry loader for the model."
tags: [class]
last_verified_commit: "dc137c3"
---

# InferenceJob

Source File: `src/autogen_team/application/jobs/inference.py`

Generate batch predictions from a registered model.  Parameters:     inputs (datasets.ReaderKind): reader for the inputs data.     outputs (datasets.WriterKind): writer for the outputs data.     alias_or_version (str | int): alias or version for the  model.     loader (registries.LoaderKind): registry loader for the model.

## Architecture Visualization

```mermaid
classDiagram
    class InferenceJob {
        +run()
    }
```
