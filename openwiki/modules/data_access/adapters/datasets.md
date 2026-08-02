---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Datasets"
source_path: "src/autogen_team/data_access/adapters/datasets.py"
description: "Exhaustive functional summary for Datasets."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---
# Module Specification: Datasets

* **Source Reference:** `src/autogen_team/data_access/adapters/datasets.py`

## Overview
This module provides data access functionality for Datasets.

## UML Diagrams

```mermaid
classDiagram
    class ParquetReader {
        +T.Literal['ParquetReader'] KIND
        +str path
        +lineage(name: str, data: pd.DataFrame, targets: str \| None, predictions: str \| None): Lineage
        +read(): pd.DataFrame
    }
    class ParquetWriter {
        +T.Literal['ParquetWriter'] KIND
        +str path
        +write(data: pd.DataFrame): None
    }
    class Reader {
        +str KIND
        +int \ limit
        +None
        +|lineage(name: str, data: pd.DataFrame, targets: str \| None, predictions: str \| None): Lineage
        +read(): pd.DataFrame
    }
    class Writer {
        +str KIND
        +write(data: pd.DataFrame): None
    }
    Reader <|-- ParquetReader
    Writer <|-- ParquetWriter
    EvaluationsJob --> ParquetReader
    EvaluationsJob --> ParquetReader
    ExplanationsJob --> ParquetReader
    HatchetInferenceJob --> ParquetReader
    InferenceJob --> ParquetReader
    TrainingJob --> ParquetReader
    TrainingJob --> ParquetReader
    TuningJob --> ParquetReader
    TuningJob --> ParquetReader
    ExplanationsJob --> ParquetWriter
    ExplanationsJob --> ParquetWriter
    HatchetInferenceJob --> ParquetWriter
    InferenceJob --> ParquetWriter
```
