---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: conftest"
source_path: "tests/conftest.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-11T06:05:51.229543+00:00"
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
    ' No classes found in module
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
### `_patched_prepare(self: OpenAIChatClient, message: Message)`
No description provided.

**Inputs:**
- `self`: OpenAIChatClient
- `message`: Message

**Output:**
- Return Type: `T.List[T.Dict[str, T.Any]]`

### `tests_path()`
Return the path of the tests folder.

**Inputs:**
- None

**Output:**
- Return Type: `str`

### `data_path(tests_path: str)`
Return the path of the data folder.

**Inputs:**
- `tests_path`: str

**Output:**
- Return Type: `str`

### `confs_path(tests_path: str)`
Return the path of the confs folder.

**Inputs:**
- `tests_path`: str

**Output:**
- Return Type: `str`

### `inputs_path(data_path: str)`
Return the path of the inputs dataset.

**Inputs:**
- `data_path`: str

**Output:**
- Return Type: `str`

### `targets_path(data_path: str)`
Return the path of the targets dataset.

**Inputs:**
- `data_path`: str

**Output:**
- Return Type: `str`

### `outputs_path(data_path: str)`
Return the path of the outputs dataset.

**Inputs:**
- `data_path`: str

**Output:**
- Return Type: `str`

### `tmp_outputs_path(tmp_path: str)`
Return a tmp path for the outputs dataset.

**Inputs:**
- `tmp_path`: str

**Output:**
- Return Type: `str`

### `tmp_models_explanations_path(tmp_path: str)`
Return a tmp path for the model explanations dataset.

**Inputs:**
- `tmp_path`: str

**Output:**
- Return Type: `str`

### `tmp_samples_explanations_path(tmp_path: str)`
Return a tmp path for the samples explanations dataset.

**Inputs:**
- `tmp_path`: str

**Output:**
- Return Type: `str`

### `extra_config()`
Extra config for scripts.

**Inputs:**
- None

**Output:**
- Return Type: `str`

### `inputs_reader(inputs_path: str)`
Return a reader for the inputs dataset.

**Inputs:**
- `inputs_path`: str

**Output:**
- Return Type: `datasets.ParquetReader`

### `inputs_samples_reader(inputs_path: str)`
Return a reader for the inputs samples dataset.

**Inputs:**
- `inputs_path`: str

**Output:**
- Return Type: `datasets.ParquetReader`

### `targets_reader(targets_path: str)`
Return a reader for the targets dataset.

**Inputs:**
- `targets_path`: str

**Output:**
- Return Type: `datasets.ParquetReader`

### `outputs_reader(outputs_path: str, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader)`
Return a reader for the outputs dataset.

**Inputs:**
- `outputs_path`: str
- `inputs_reader`: datasets.ParquetReader
- `targets_reader`: datasets.ParquetReader

**Output:**
- Return Type: `datasets.ParquetReader`

### `tmp_outputs_writer(tmp_outputs_path: str)`
Return a writer for the tmp outputs dataset.

**Inputs:**
- `tmp_outputs_path`: str

**Output:**
- Return Type: `datasets.ParquetWriter`

### `tmp_models_explanations_writer(tmp_models_explanations_path: str)`
Return a writer for the tmp model explanations dataset.

**Inputs:**
- `tmp_models_explanations_path`: str

**Output:**
- Return Type: `datasets.ParquetWriter`

### `tmp_samples_explanations_writer(tmp_samples_explanations_path: str)`
Return a writer for the tmp samples explanations dataset.

**Inputs:**
- `tmp_samples_explanations_path`: str

**Output:**
- Return Type: `datasets.ParquetWriter`

### `inputs(inputs_reader: datasets.ParquetReader)`
Return the inputs data.

**Inputs:**
- `inputs_reader`: datasets.ParquetReader

**Output:**
- Return Type: `schemas.Inputs`

### `inputs_samples(inputs_samples_reader: datasets.ParquetReader)`
Return the inputs samples data.

**Inputs:**
- `inputs_samples_reader`: datasets.ParquetReader

**Output:**
- Return Type: `schemas.Inputs`

### `targets(targets_reader: datasets.ParquetReader)`
Return the targets data.

**Inputs:**
- `targets_reader`: datasets.ParquetReader

**Output:**
- Return Type: `schemas.Targets`

### `outputs(outputs_reader: datasets.ParquetReader)`
Return the outputs data.

**Inputs:**
- `outputs_reader`: datasets.ParquetReader

**Output:**
- Return Type: `schemas.Outputs`

### `train_test_splitter()`
Return the default train test splitter.

**Inputs:**
- None

**Output:**
- Return Type: `splitters.TrainTestSplitter`

### `time_series_splitter()`
Return the default time series splitter.

**Inputs:**
- None

**Output:**
- Return Type: `splitters.TimeSeriesSplitter`

### `searcher()`
Return the default searcher object.

**Inputs:**
- None

**Output:**
- Return Type: `searchers.Searcher`

### `train_test_sets(train_test_splitter: splitters.Splitter, inputs: schemas.Inputs, targets: schemas.Targets)`
Return the inputs and targets train and test sets from the splitter.

**Inputs:**
- `train_test_splitter`: splitters.Splitter
- `inputs`: schemas.Inputs
- `targets`: schemas.Targets

**Output:**
- Return Type: `tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]`

### `model(train_test_sets: tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets])`
Return a train model for testing.

**Inputs:**
- `train_test_sets`: tuple[schemas.Inputs, schemas.Targets, schemas.Inputs, schemas.Targets]

**Output:**
- Return Type: `models.BaselineAutogenModel`

### `metric()`
Return the default metric.

**Inputs:**
- None

**Output:**
- Return Type: `metrics.AutogenMetric`

### `signer()`
Return a model signer.

**Inputs:**
- None

**Output:**
- Return Type: `signers.Signer`

### `logger_service()`
Return and start the logger service.

**Inputs:**
- None

**Output:**
- Return Type: `T.Generator[services.LoggerService, None, None]`

### `logger_caplog(caplog: pl.LogCaptureFixture, logger_service: services.LoggerService)`
Extend pytest caplog fixture with the logger service (loguru).

**Inputs:**
- `caplog`: pl.LogCaptureFixture
- `logger_service`: services.LoggerService

**Output:**
- Return Type: `T.Generator[pl.LogCaptureFixture, None, None]`

### `alerts_service()`
Return and start the alerter service.

**Inputs:**
- None

**Output:**
- Return Type: `T.Generator[services.AlertsService, None, None]`

### `mlflow_service(tmp_path: str)`
Return and start the mlflow service.

**Inputs:**
- `tmp_path`: str

**Output:**
- Return Type: `T.Generator[services.MlflowService, None, None]`

### `chtgpt_service(targets: schemas.Targets, inputs_samples: schemas.Inputs)`
Return and start the logger service.

**Inputs:**
- `targets`: schemas.Targets
- `inputs_samples`: schemas.Inputs

**Output:**
- Return Type: `GptServer`

### `tests_path_resolver(tests_path: str)`
Register the tests path resolver with OmegaConf.

**Inputs:**
- `tests_path`: str

**Output:**
- Return Type: `str`

### `tmp_path_resolver(tmp_path: str)`
Register the tmp path resolver with OmegaConf.

**Inputs:**
- `tmp_path`: str

**Output:**
- Return Type: `str`

### `signature(signer: signers.Signer, inputs: schemas.Inputs, outputs: schemas.Outputs)`
Return the signature for the testing model.

**Inputs:**
- `signer`: signers.Signer
- `inputs`: schemas.Inputs
- `outputs`: schemas.Outputs

**Output:**
- Return Type: `signers.Signature`

### `saver()`
Return the default model saver.

**Inputs:**
- None

**Output:**
- Return Type: `registries.CustomSaver`

### `loader()`
Return the default model loader.

**Inputs:**
- None

**Output:**
- Return Type: `registries.CustomLoader`

### `register()`
Return the default model register.

**Inputs:**
- None

**Output:**
- Return Type: `registries.MlflowRegister`

### `model_version(model: models.Model, inputs: schemas.Inputs, signature: signers.Signature, saver: registries.Saver, register: registries.Register, mlflow_service: services.MlflowService)`
Save and register the default model version.

**Inputs:**
- `model`: models.Model
- `inputs`: schemas.Inputs
- `signature`: signers.Signature
- `saver`: registries.Saver
- `register`: registries.Register
- `mlflow_service`: services.MlflowService

**Output:**
- Return Type: `registries.Version`

### `model_alias(model_version: registries.Version, mlflow_service: services.MlflowService)`
Promote the default model version with an alias.

**Inputs:**
- `model_version`: registries.Version
- `mlflow_service`: services.MlflowService

**Output:**
- Return Type: `registries.Alias`
