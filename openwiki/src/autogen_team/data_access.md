---
type: "module-architecture"
title: "Data Access Architecture: src/autogen_team/data_access"
description: "Technical architecture and class hierarchy for dataset readers, writers, and lineage adapters"
tags: ["architecture", "data_access", "parquet", "lineage", "mlflow", "openwiki"]
timestamp: "2026-07-30T00:00:00Z"
---

# Module Name: data_access

* **Source Directory Reference:** `src/autogen_team/data_access/`
* **Package Dependency:** Upstream: `pandas`, `pydantic`, `mlflow.data.pandas_dataset`. Downstream: `src/autogen_team/application/jobs/`, `src/autogen_team/models/`.

## 1. Executive Summary & Purpose

The `data_access` module provides clean abstractions for reading, writing, and tracking dataset lineage across external storage targets (local file system, Cloud Storage, S3 Parquet). It defines the `DatasetRepository` interface and concrete readers/writers (`Reader`, `ParquetReader`, `Writer`, `ParquetWriter`) integrated with MLflow data lineage tracking.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)

```mermaid
classDiagram
    direction BT
    class ABC {
        <<external: abc>>
    }
    class BaseModel {
        <<external: pydantic>>
    }
    class DatasetRepository {
        <<interface>>
        +read()* DataFrame
    }
    class Reader {
        <<abstract>>
        +KIND: str
        +limit: int | None
        +read()* DataFrame
        +lineage(name, data, targets, predictions)* PandasDataset
    }
    class ParquetReader {
        +KIND: "ParquetReader"
        +path: str
        +read() DataFrame
        +lineage(name, data, targets, predictions) PandasDataset
    }
    class Writer {
        <<abstract>>
        +KIND: str
        +write(data: DataFrame)* None
    }
    class ParquetWriter {
        +KIND: "ParquetWriter"
        +path: str
        +write(data: DataFrame) None
    }

    ABC <|-- DatasetRepository
    ABC <|-- Reader
    BaseModel <|-- Reader
    Reader <|-- ParquetReader
    ABC <|-- Writer
    BaseModel <|-- Writer
    Writer <|-- ParquetWriter
```

## 3. Package & Class Relations

* **Inheritance & Abstraction:** Both `Reader` and `Writer` inherit from `abc.ABC` and `pydantic.BaseModel` with `strict=True`, `frozen=True`, and `extra="forbid"`.
* **Parquet Serialization:** `ParquetReader` loads Parquet files into `pandas.DataFrame` objects and applies row-limit truncation when specified. `ParquetWriter` persists `pandas.DataFrame` objects back to disk.
* **Lineage Tracking:** `Reader.lineage()` constructs an `mlflow.data.pandas_dataset.PandasDataset` instance linking input DataFrames to MLflow run metadata.

## 4. Execution Flow & Runtime Behavior

```mermaid
sequenceDiagram
    autonumber
    participant Job as Job (e.g. Training)
    participant Reader as ParquetReader
    participant Storage as FileSystem / Parquet File
    participant Lineage as MLflow Lineage

    Job->>Reader: read()
    Reader->>Storage: pd.read_parquet(self.path)
    Storage-->>Reader: Returns DataFrame
    Reader-->>Job: Returns pandas.DataFrame

    Job->>Reader: lineage(name, data, targets, predictions)
    Reader->>Lineage: lineage.from_pandas(df, name, source=path, ...)
    Lineage-->>Reader: Returns PandasDataset Lineage Object
    Reader-->>Job: Returns Lineage Object
```

---

* **Source Citations:**
  * Dataset Repository Interface: `src/autogen_team/data_access/repositories.py:8-14`
  * Abstract Reader & ParquetReader: `src/autogen_team/data_access/adapters/datasets.py:19-92`
  * Abstract Writer & ParquetWriter: `src/autogen_team/data_access/adapters/datasets.py:97-130`
