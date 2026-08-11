---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: datasets"
source_path: "src/autogen_team/data_access/adapters/datasets.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.159789+00:00"
---

# Module Specification: datasets

* **Source Reference:** `src/autogen_team/data_access/adapters/datasets.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to datasets.

**Architecture Layer:**
- Repositories

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `abc`
- `typing`
- `mlflow.data.pandas_dataset`
- `pandas`
- `pydantic`

**Exported Classes:**
- `Reader`
- `ParquetReader`
- `Writer`
- `ParquetWriter`

**Exported Functions:**
- None

## 3. Architecture & Execution
### Internal Architecture
Not explicitly defined.

### Execution Flow
Not explicitly defined.

### Sequence Explanation
Not explicitly defined.

## 4. UML 2.0 Diagrams
### Class Diagram
```plantuml
@startuml
    class Reader {
        +read() : pd.DataFrame
        +lineage() : Lineage
    }
    class ParquetReader {
        +read() : pd.DataFrame
        +lineage() : Lineage
    }
    class Writer {
        +write() : None
    }
    class ParquetWriter {
        +write() : None
    }
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [abc] : imports
    [Module] --> [typing] : imports
    [Module] --> [mlflow.data.pandas_dataset] : imports
    [Module] --> [pandas] : imports
    [Module] --> [pydantic] : imports
@enduml
```

## 5. Class & Method Specifications
### `Reader` ([`src/autogen_team/data_access/adapters/datasets.py`](/src/autogen_team/data_access/adapters/datasets.py))
#### Overview
Base class for a dataset reader.

Use a reader to load a dataset in memory.
e.g., to read file, database, cloud storage, ...

Parameters:
    limit (int, optional): maximum number of rows to read. Defaults to None.

#### Attributes
- None found.

#### Methods
##### `read(self) -> pd.DataFrame` (Public)
**Description:** Read a dataframe from a dataset.

Returns:
    pd.DataFrame: dataframe representation.

**Inputs:**
- None

**Output:**
- Return Type: `pd.DataFrame`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = Reader.read()
```

##### `lineage(self, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) -> Lineage` (Public)
**Description:** Generate lineage information.

Args:
    name (str): dataset name.
    data (pd.DataFrame): reader dataframe.
    targets (str | None): name of the target column.
    predictions (str | None): name of the prediction column.

Returns:
    Lineage: lineage information.

**Inputs:**
- `name`: str
- `data`: pd.DataFrame
- `targets`: str | None
- `predictions`: str | None

**Output:**
- Return Type: `Lineage`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = Reader.lineage(..., ..., ..., ...)
```

### `ParquetReader` ([`src/autogen_team/data_access/adapters/datasets.py`](/src/autogen_team/data_access/adapters/datasets.py))
#### Overview
Read a dataframe from a parquet file.

Parameters:
    path (str): local path to the dataset.

#### Attributes
- None found.

#### Methods
##### `read(self) -> pd.DataFrame` (Public)
**Description:** No description provided.

**Inputs:**
- None

**Output:**
- Return Type: `pd.DataFrame`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = ParquetReader.read()
```

##### `lineage(self, name: str, data: pd.DataFrame, targets: str | None, predictions: str | None) -> Lineage` (Public)
**Description:** No description provided.

**Inputs:**
- `name`: str
- `data`: pd.DataFrame
- `targets`: str | None
- `predictions`: str | None

**Output:**
- Return Type: `Lineage`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = ParquetReader.lineage(..., ..., ..., ...)
```

### `Writer` ([`src/autogen_team/data_access/adapters/datasets.py`](/src/autogen_team/data_access/adapters/datasets.py))
#### Overview
Base class for a dataset writer.

Use a writer to save a dataset from memory.
e.g., to write file, database, cloud storage, ...

#### Attributes
- None found.

#### Methods
##### `write(self, data: pd.DataFrame) -> None` (Public)
**Description:** Write a dataframe to a dataset.

Args:
    data (pd.DataFrame): dataframe representation.

**Inputs:**
- `data`: pd.DataFrame

**Output:**
- Return Type: `None`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = Writer.write(...)
```

### `ParquetWriter` ([`src/autogen_team/data_access/adapters/datasets.py`](/src/autogen_team/data_access/adapters/datasets.py))
#### Overview
Writer a dataframe to a parquet file.

Parameters:
    path (str): local or S3 path to the dataset.

#### Attributes
- None found.

#### Methods
##### `write(self, data: pd.DataFrame) -> None` (Public)
**Description:** No description provided.

**Inputs:**
- `data`: pd.DataFrame

**Output:**
- Return Type: `None`
- Semantic Meaning: Not explicitly defined.

**Side Effects:**
- Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = ParquetWriter.write(...)
```

## 6. Module Functions