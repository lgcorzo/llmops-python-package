---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: conftest"
source_path: "tests/conftest.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-09-02T05:14:17.126486+00:00"
---

# Module Specification: conftest

* **Source Reference:** `tests/conftest.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to conftest.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `os`
- `typing`
- `typing.Any`
- `typing.cast`
- `omegaconf`
- `pytest`
- `_pytest.logging`
- `agent_framework.Message`
- `agent_framework.openai.OpenAIChatClient`
- `autogen_team.core.schemas`
- `autogen_team.data_access.adapters.datasets`
- `autogen_team.evaluation.metrics`
- `autogen_team.infrastructure.services`
- `autogen_team.infrastructure.utils.searchers`
- `autogen_team.infrastructure.utils.signers`
- `autogen_team.infrastructure.utils.splitters`
- `autogen_team.models.entities`
- `autogen_team.registry.adapters.mlflow_adapter`
- `mocogpt.GptServer`
- `mocogpt.gpt_server`
- `openai.OpenAI`

**Exported Classes:**
- None

**Exported Functions:**
- `_patched_prepare`
- `tests_path`
- `data_path`
- `confs_path`
- `inputs_path`
- `targets_path`
- `outputs_path`
- `tmp_outputs_path`
- `tmp_models_explanations_path`
- `tmp_samples_explanations_path`
- `extra_config`
- `inputs_reader`
- `inputs_samples_reader`
- `targets_reader`
- `outputs_reader`
- `tmp_outputs_writer`
- `tmp_models_explanations_writer`
- `tmp_samples_explanations_writer`
- `inputs`
- `inputs_samples`
- `targets`
- `outputs`
- `train_test_splitter`
- `time_series_splitter`
- `searcher`
- `train_test_sets`
- `model`
- `metric`
- `signer`
- `logger_service`
- `logger_caplog`
- `alerts_service`
- `mlflow_service`
- `chtgpt_service`
- `tests_path_resolver`
- `tmp_path_resolver`
- `signature`
- `saver`
- `loader`
- `register`
- `model_version`
- `model_alias`

**Exported Interfaces:**
- Not explicitly defined.

**Public API:**
- Not explicitly defined.

## 3. Architecture & Execution
### Internal Architecture
Not explicitly defined.

### Execution Flow
Not explicitly defined.

### Sequence Explanation
Not explicitly defined.

### Examples
Not explicitly defined.

## 4. UML 2.0 Diagrams
### Class Diagram
```plantuml
@startuml
    ' No classes found in module
@enduml
```

### Package Diagram
```plantuml
@startuml
    package "tests" {
        [conftest.py]
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    _patched_prepare -> _orig_prepare : call
    _patched_prepare -> len : call
    _patched_prepare -> isinstance : call
    _patched_prepare -> get : call
    tests_path -> dirname : call
    tests_path -> abspath : call
    tests_path -> fixture : call
    data_path -> join : call
    data_path -> fixture : call
    confs_path -> join : call
    confs_path -> fixture : call
    inputs_path -> join : call
    inputs_path -> fixture : call
    targets_path -> join : call
    targets_path -> fixture : call
    outputs_path -> join : call
    outputs_path -> fixture : call
    tmp_outputs_path -> join : call
    tmp_outputs_path -> fixture : call
    tmp_models_explanations_path -> join : call
    tmp_models_explanations_path -> fixture : call
    tmp_samples_explanations_path -> join : call
    tmp_samples_explanations_path -> fixture : call
    extra_config -> fixture : call
    inputs_reader -> ParquetReader : call
    inputs_reader -> fixture : call
    inputs_samples_reader -> ParquetReader : call
    inputs_samples_reader -> fixture : call
    targets_reader -> ParquetReader : call
    targets_reader -> fixture : call
    outputs_reader -> write : call
    outputs_reader -> read : call
    outputs_reader -> fixture : call
    outputs_reader -> check : call
    outputs_reader -> predict : call
    outputs_reader -> fit : call
    outputs_reader -> ParquetReader : call
    outputs_reader -> ParquetWriter : call
    outputs_reader -> load_context : call
    outputs_reader -> BaselineAutogenModel : call
    outputs_reader -> exists : call
    tmp_outputs_writer -> ParquetWriter : call
    tmp_outputs_writer -> fixture : call
    tmp_models_explanations_writer -> ParquetWriter : call
    tmp_models_explanations_writer -> fixture : call
    tmp_samples_explanations_writer -> ParquetWriter : call
    tmp_samples_explanations_writer -> fixture : call
    inputs -> read : call
    inputs -> fixture : call
    inputs -> check : call
    inputs_samples -> read : call
    inputs_samples -> fixture : call
    inputs_samples -> check : call
    targets -> read : call
    targets -> fixture : call
    targets -> check : call
    outputs -> read : call
    outputs -> fixture : call
    outputs -> check : call
    train_test_splitter -> TrainTestSplitter : call
    train_test_splitter -> fixture : call
    time_series_splitter -> fixture : call
    time_series_splitter -> TimeSeriesSplitter : call
    searcher -> cast : call
    searcher -> GridCVSearcher : call
    searcher -> fixture : call
    train_test_sets -> split : call
    train_test_sets -> next : call
    train_test_sets -> cast : call
    train_test_sets -> fixture : call
    model -> BaselineAutogenModel : call
    model -> fit : call
    model -> fixture : call
    model -> load_context : call
    metric -> AutogenMetric : call
    metric -> fixture : call
    signer -> InferSigner : call
    signer -> fixture : call
    logger_service -> LoggerService : call
    logger_service -> stop : call
    logger_service -> start : call
    logger_service -> fixture : call
    logger_caplog -> remove : call
    logger_caplog -> logger : call
    logger_caplog -> add : call
    alerts_service -> stop : call
    alerts_service -> start : call
    alerts_service -> fixture : call
    alerts_service -> AlertsService : call
    mlflow_service -> MlflowService : call
    mlflow_service -> stop : call
    mlflow_service -> start : call
    mlflow_service -> fixture : call
    chtgpt_service -> zip : call
    chtgpt_service -> fixture : call
    chtgpt_service -> request : call
    chtgpt_service -> gpt_server : call
    chtgpt_service -> response : call
    chtgpt_service -> OpenAI : call
    chtgpt_service -> create : call
    tests_path_resolver -> register_new_resolver : call
    tests_path_resolver -> fixture : call
    tmp_path_resolver -> register_new_resolver : call
    tmp_path_resolver -> fixture : call
    signature -> sign : call
    signature -> fixture : call
    saver -> CustomSaver : call
    saver -> fixture : call
    loader -> fixture : call
    loader -> CustomLoader : call
    register -> MlflowRegister : call
    register -> fixture : call
    model_version -> register : call
    model_version -> fixture : call
    model_version -> run_context : call
    model_version -> RunConfig : call
    model_version -> save : call
    model_alias -> client : call
    model_alias -> set_registered_model_alias : call
    model_alias -> get_model_version_by_alias : call
    model_alias -> fixture : call
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Infrastructure/Other" {
        [conftest.py]
    }
    [conftest.py] --> [os]
    [conftest.py] --> [typing]
    [conftest.py] --> [typing.Any]
    [conftest.py] --> [typing.cast]
    [conftest.py] --> [omegaconf]
    [conftest.py] --> [pytest]
    [conftest.py] --> [_pytest.logging]
    [conftest.py] --> [agent_framework.Message]
    [conftest.py] --> [agent_framework.openai.OpenAIChatClient]
    [conftest.py] --> [autogen_team.core.schemas]
    [conftest.py] --> [autogen_team.data_access.adapters.datasets]
    [conftest.py] --> [autogen_team.evaluation.metrics]
    [conftest.py] --> [autogen_team.infrastructure.services]
    [conftest.py] --> [autogen_team.infrastructure.utils.searchers]
    [conftest.py] --> [autogen_team.infrastructure.utils.signers]
    [conftest.py] --> [autogen_team.infrastructure.utils.splitters]
    [conftest.py] --> [autogen_team.models.entities]
    [conftest.py] --> [autogen_team.registry.adapters.mlflow_adapter]
    [conftest.py] --> [mocogpt.GptServer]
    [conftest.py] --> [mocogpt.gpt_server]
    [conftest.py] --> [openai.OpenAI]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [os] : imports
    [Module] --> [typing] : imports
    [Module] --> [typing.Any] : imports
    [Module] --> [typing.cast] : imports
    [Module] --> [omegaconf] : imports
    [Module] --> [pytest] : imports
    [Module] --> [_pytest.logging] : imports
    [Module] --> [agent_framework.Message] : imports
    [Module] --> [agent_framework.openai.OpenAIChatClient] : imports
    [Module] --> [autogen_team.core.schemas] : imports
    [Module] --> [autogen_team.data_access.adapters.datasets] : imports
    [Module] --> [autogen_team.evaluation.metrics] : imports
    [Module] --> [autogen_team.infrastructure.services] : imports
    [Module] --> [autogen_team.infrastructure.utils.searchers] : imports
    [Module] --> [autogen_team.infrastructure.utils.signers] : imports
    [Module] --> [autogen_team.infrastructure.utils.splitters] : imports
    [Module] --> [autogen_team.models.entities] : imports
    [Module] --> [autogen_team.registry.adapters.mlflow_adapter] : imports
    [Module] --> [mocogpt.GptServer] : imports
    [Module] --> [mocogpt.gpt_server] : imports
    [Module] --> [openai.OpenAI] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `_patched_prepare(self: OpenAIChatClient, message: Message) -> T.List[T.Dict[str, T.Any]]` (Private)
**Purpose:** Executes the patched prepare operation.

**Parameters:**
- `self`: OpenAIChatClient
- `message`: Message

**Return value:**
- `T.List[T.Dict[str, T.Any]]`

### `tests_path() -> str` (Public)
**Description:** Return the path of the tests folder.

**Inputs:**
- None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tests_path()
```

### `data_path(tests_path: str) -> str` (Public)
**Description:** Return the path of the data folder.

**Inputs:**
- `tests_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = data_path(...)
```

### `confs_path(tests_path: str) -> str` (Public)
**Description:** Return the path of the confs folder.

**Inputs:**
- `tests_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = confs_path(...)
```

### `inputs_path(data_path: str) -> str` (Public)
**Description:** Return the path of the inputs dataset.

**Inputs:**
- `data_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = inputs_path(...)
```

### `targets_path(data_path: str) -> str` (Public)
**Description:** Return the path of the targets dataset.

**Inputs:**
- `data_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = targets_path(...)
```

### `outputs_path(data_path: str) -> str` (Public)
**Description:** Return the path of the outputs dataset.

**Inputs:**
- `data_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = outputs_path(...)
```

### `tmp_outputs_path(tmp_path: str) -> str` (Public)
**Description:** Return a tmp path for the outputs dataset.

**Inputs:**
- `tmp_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tmp_outputs_path(...)
```

### `tmp_models_explanations_path(tmp_path: str) -> str` (Public)
**Description:** Return a tmp path for the model explanations dataset.

**Inputs:**
- `tmp_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tmp_models_explanations_path(...)
```

### `tmp_samples_explanations_path(tmp_path: str) -> str` (Public)
**Description:** Return a tmp path for the samples explanations dataset.

**Inputs:**
- `tmp_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tmp_samples_explanations_path(...)
```

### `extra_config() -> str` (Public)
**Description:** Extra config for scripts.

**Inputs:**
- None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = extra_config()
```

### `inputs_reader(inputs_path: str) -> datasets.ParquetReader` (Public)
**Description:** Return a reader for the inputs dataset.

**Inputs:**
- `inputs_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `datasets.ParquetReader`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = inputs_reader(...)
```

### `inputs_samples_reader(inputs_path: str) -> datasets.ParquetReader` (Public)
**Description:** Return a reader for the inputs samples dataset.

**Inputs:**
- `inputs_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `datasets.ParquetReader`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = inputs_samples_reader(...)
```

### `targets_reader(targets_path: str) -> datasets.ParquetReader` (Public)
**Description:** Return a reader for the targets dataset.

**Inputs:**
- `targets_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `datasets.ParquetReader`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = targets_reader(...)
```

### `outputs_reader(outputs_path: str, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader) -> datasets.ParquetReader` (Public)
**Description:** Return a reader for the outputs dataset.

**Inputs:**
- `outputs_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `inputs_reader`
  - type: datasets.ParquetReader
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `targets_reader`
  - type: datasets.ParquetReader
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `datasets.ParquetReader`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = outputs_reader(..., ..., ...)
```

### `tmp_outputs_writer(tmp_outputs_path: str) -> datasets.ParquetWriter` (Public)
**Description:** Return a writer for the tmp outputs dataset.

**Inputs:**
- `tmp_outputs_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `datasets.ParquetWriter`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tmp_outputs_writer(...)
```

### `tmp_models_explanations_writer(tmp_models_explanations_path: str) -> datasets.ParquetWriter` (Public)
**Description:** Return a writer for the tmp model explanations dataset.

**Inputs:**
- `tmp_models_explanations_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `datasets.ParquetWriter`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tmp_models_explanations_writer(...)
```

### `tmp_samples_explanations_writer(tmp_samples_explanations_path: str) -> datasets.ParquetWriter` (Public)
**Description:** Return a writer for the tmp samples explanations dataset.

**Inputs:**
- `tmp_samples_explanations_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `datasets.ParquetWriter`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tmp_samples_explanations_writer(...)
```

### `inputs(inputs_reader: datasets.ParquetReader) -> schemas.Inputs` (Public)
**Description:** Return the inputs data.

**Inputs:**
- `inputs_reader`
  - type: datasets.ParquetReader
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `schemas.Inputs`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = inputs(...)
```

### `inputs_samples(inputs_samples_reader: datasets.ParquetReader) -> schemas.Inputs` (Public)
**Description:** Return the inputs samples data.

**Inputs:**
- `inputs_samples_reader`
  - type: datasets.ParquetReader
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `schemas.Inputs`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = inputs_samples(...)
```

### `targets(targets_reader: datasets.ParquetReader) -> schemas.Targets` (Public)
**Description:** Return the targets data.

**Inputs:**
- `targets_reader`
  - type: datasets.ParquetReader
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `schemas.Targets`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = targets(...)
```

### `outputs(outputs_reader: datasets.ParquetReader) -> schemas.Outputs` (Public)
**Description:** Return the outputs data.

**Inputs:**
- `outputs_reader`
  - type: datasets.ParquetReader
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `schemas.Outputs`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = outputs(...)
```

### `train_test_splitter() -> splitters.TrainTestSplitter` (Public)
**Description:** Return the default train test splitter.

**Inputs:**
- None

**Output:**
- return type: `splitters.TrainTestSplitter`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = train_test_splitter()
```

### `time_series_splitter() -> splitters.TimeSeriesSplitter` (Public)
**Description:** Return the default time series splitter.

**Inputs:**
- None

**Output:**
- return type: `splitters.TimeSeriesSplitter`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = time_series_splitter()
```

### `searcher() -> searchers.Searcher` (Public)
**Description:** Return the default searcher object.

**Inputs:**
- None

**Output:**
- return type: `searchers.Searcher`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = searcher()
```

### `train_test_sets(train_test_splitter: splitters.Splitter, inputs: schemas.Inputs, targets: schemas.Targets) -> tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]` (Public)
**Description:** Return the inputs and targets train and test sets from the splitter.

**Inputs:**
- `train_test_splitter`
  - type: splitters.Splitter
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `inputs`
  - type: schemas.Inputs
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `targets`
  - type: schemas.Targets
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = train_test_sets(..., ..., ...)
```

### `model(train_test_sets: tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]) -> models.BaselineAutogenModel` (Public)
**Description:** Return a train model for testing.

**Inputs:**
- `train_test_sets`
  - type: tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `models.BaselineAutogenModel`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = model(...)
```

### `metric() -> metrics.AutogenMetric` (Public)
**Description:** Return the default metric.

**Inputs:**
- None

**Output:**
- return type: `metrics.AutogenMetric`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = metric()
```

### `signer() -> signers.Signer` (Public)
**Description:** Return a model signer.

**Inputs:**
- None

**Output:**
- return type: `signers.Signer`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = signer()
```

### `logger_service() -> T.Generator[services.LoggerService, None, None]` (Public)
**Description:** Return and start the logger service.

**Inputs:**
- None

**Output:**
- return type: `T.Generator[services.LoggerService, None, None]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = logger_service()
```

### `logger_caplog(caplog: pl.LogCaptureFixture, logger_service: services.LoggerService) -> T.Generator[pl.LogCaptureFixture, None, None]` (Public)
**Description:** Extend pytest caplog fixture with the logger service (loguru).

**Inputs:**
- `caplog`
  - type: pl.LogCaptureFixture
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `logger_service`
  - type: services.LoggerService
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `T.Generator[pl.LogCaptureFixture, None, None]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = logger_caplog(..., ...)
```

### `alerts_service() -> T.Generator[services.AlertsService, None, None]` (Public)
**Description:** Return and start the alerter service.

**Inputs:**
- None

**Output:**
- return type: `T.Generator[services.AlertsService, None, None]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = alerts_service()
```

### `mlflow_service(tmp_path: str) -> T.Generator[services.MlflowService, None, None]` (Public)
**Description:** Return and start the mlflow service.

**Inputs:**
- `tmp_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `T.Generator[services.MlflowService, None, None]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = mlflow_service(...)
```

### `chtgpt_service(targets: schemas.Targets, inputs_samples: schemas.Inputs) -> GptServer` (Public)
**Description:** Return and start the logger service.

**Inputs:**
- `targets`
  - type: schemas.Targets
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `inputs_samples`
  - type: schemas.Inputs
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `GptServer`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = chtgpt_service(..., ...)
```

### `tests_path_resolver(tests_path: str) -> str` (Public)
**Description:** Register the tests path resolver with OmegaConf.

**Inputs:**
- `tests_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tests_path_resolver(...)
```

### `tmp_path_resolver(tmp_path: str) -> str` (Public)
**Description:** Register the tmp path resolver with OmegaConf.

**Inputs:**
- `tmp_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `str`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = tmp_path_resolver(...)
```

### `signature(signer: signers.Signer, inputs: schemas.Inputs, outputs: schemas.Outputs) -> signers.Signature` (Public)
**Description:** Return the signature for the testing model.

**Inputs:**
- `signer`
  - type: signers.Signer
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `inputs`
  - type: schemas.Inputs
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `outputs`
  - type: schemas.Outputs
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `signers.Signature`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = signature(..., ..., ...)
```

### `saver() -> registries.CustomSaver` (Public)
**Description:** Return the default model saver.

**Inputs:**
- None

**Output:**
- return type: `registries.CustomSaver`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = saver()
```

### `loader() -> registries.CustomLoader` (Public)
**Description:** Return the default model loader.

**Inputs:**
- None

**Output:**
- return type: `registries.CustomLoader`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = loader()
```

### `register() -> registries.MlflowRegister` (Public)
**Description:** Return the default model register.

**Inputs:**
- None

**Output:**
- return type: `registries.MlflowRegister`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = register()
```

### `model_version(model: models.Model, inputs: schemas.Inputs, signature: signers.Signature, saver: registries.Saver, register: registries.Register, mlflow_service: services.MlflowService) -> registries.Version` (Public)
**Description:** Save and register the default model version.

**Inputs:**
- `model`
  - type: models.Model
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `inputs`
  - type: schemas.Inputs
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `signature`
  - type: signers.Signature
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `saver`
  - type: registries.Saver
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `register`
  - type: registries.Register
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `mlflow_service`
  - type: services.MlflowService
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `registries.Version`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = model_version(..., ..., ..., ..., ..., ...)
```

### `model_alias(model_version: registries.Version, mlflow_service: services.MlflowService) -> registries.Alias` (Public)
**Description:** Promote the default model version with an alias.

**Inputs:**
- `model_version`
  - type: registries.Version
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `mlflow_service`
  - type: services.MlflowService
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `registries.Alias`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = model_alias(..., ...)
```

## 7. Call Graph
```plantuml
@startuml
[conftest] --> [set_registered_model_alias] : calls
[conftest] --> [read] : calls
[conftest] --> [register] : calls
[conftest] --> [RunConfig] : calls
[conftest] --> [MlflowService] : calls
[conftest] --> [cast] : calls
[conftest] --> [add] : calls
[conftest] --> [response] : calls
[conftest] --> [sign] : calls
[conftest] --> [logger] : calls
[conftest] --> [TimeSeriesSplitter] : calls
[conftest] --> [get] : calls
[conftest] --> [join] : calls
[conftest] --> [client] : calls
[conftest] --> [BaselineAutogenModel] : calls
[conftest] --> [InferSigner] : calls
[conftest] --> [isinstance] : calls
[conftest] --> [fit] : calls
[conftest] --> [zip] : calls
[conftest] --> [predict] : calls
[conftest] --> [gpt_server] : calls
[conftest] --> [AutogenMetric] : calls
[conftest] --> [get_model_version_by_alias] : calls
[conftest] --> [ParquetWriter] : calls
[conftest] --> [LoggerService] : calls
[conftest] --> [split] : calls
[conftest] --> [GridCVSearcher] : calls
[conftest] --> [CustomLoader] : calls
[conftest] --> [MlflowRegister] : calls
[conftest] --> [len] : calls
[conftest] --> [remove] : calls
[conftest] --> [TrainTestSplitter] : calls
[conftest] --> [exists] : calls
[conftest] --> [write] : calls
[conftest] --> [stop] : calls
[conftest] --> [fixture] : calls
[conftest] --> [check] : calls
[conftest] --> [AlertsService] : calls
[conftest] --> [register_new_resolver] : calls
[conftest] --> [run_context] : calls
[conftest] --> [request] : calls
[conftest] --> [_orig_prepare] : calls
[conftest] --> [next] : calls
[conftest] --> [OpenAI] : calls
[conftest] --> [start] : calls
[conftest] --> [dirname] : calls
[conftest] --> [ParquetReader] : calls
[conftest] --> [load_context] : calls
[conftest] --> [CustomSaver] : calls
[conftest] --> [create] : calls
[conftest] --> [save] : calls
[conftest] --> [abspath] : calls
@enduml
```

## 8. Cross References
- **Dependencies:** [Dependencies](../../dependencies/index.md)
- **Used by:** None
- **Calls:** set_registered_model_alias, read, register, RunConfig, MlflowService, cast, add, response, sign, logger, TimeSeriesSplitter, get, join, client, BaselineAutogenModel, InferSigner, isinstance, fit, zip, predict, gpt_server, AutogenMetric, get_model_version_by_alias, ParquetWriter, LoggerService, split, GridCVSearcher, CustomLoader, MlflowRegister, len, remove, TrainTestSplitter, exists, write, stop, fixture, check, AlertsService, register_new_resolver, run_context, request, _orig_prepare, next, OpenAI, start, dirname, ParquetReader, load_context, CustomSaver, create, save, abspath
- **Called from:** registry/adapters/test_registries.md, ../src/autogen_team/application/jobs/training.md, test_coverage_gap_fillers.md
- **Related classes:** [Classes](../../classes/index.md)
- **Related diagrams:** [Diagrams](../../diagrams/index.md)
