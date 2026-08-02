---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Entities"
source_path: "src/autogen_team/models/entities.py"
description: "Exhaustive functional summary for Entities."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---
# Module Specification: Models Entities

* **Source Reference:** `src/autogen_team/models/entities.py` (Lines: L1-L413)
* **Bounded Context:** Models
* **Upstream Dependencies:** [[Modules/Core/Schemas]]

## 1. UML 2.0 Class Diagram


## 2. Abstract Model Interface (`L33-L130`)

The `Model` class serves as the pluggable model interface, compatible with scikit-learn's estimator protocol via `get_params()`/`set_params()`. 

| Method | Abstract | Purpose |
| :--- | :--- | :--- |
| `load_context(model_config)` | ✅ | Load model configuration at runtime |
| `fit(inputs, targets)` | ✅ | Train the model |
| `predict(inputs)` | ✅ | Generate predictions |
| `explain_model()` | ❌ | Return global feature importances |
| `explain_samples(inputs)` | ❌ | Return per-sample SHAP values |
| `get_internal_model()` | ❌ | Return underlying model object |

## 3. BaselineAutogenModel (`L132-L413`)

The primary model implementation, using OpenAI-compatible chat API via `autogen_ext.models.openai`:

### Configuration

| Parameter | Type | Default | Purpose |
| :--- | :--- | :--- | :--- |
| `max_tokens` | `int` | 1000 | Max generation length |
| `temperature` | `float` | 0.7 | Generation temperature |
| `agent_framework` | `str` | `"autogen"` | Agent framework selector |
| `api_base_url` | `str` | LiteLLM cluster URL | LLM API endpoint |
| `api_model` | `str` | `"minimax-m2.7:cloud"` | Model identifier |
| `api_key` | `str` | From env | API authentication |

### Key Methods

* **`load_context(model_config)`** (L199-L235): Loads config with `${VAR}` env var expansion. Initializes `OpenAIChatCompletionClient`.
* **`predict(inputs)`** (L238-L310): Processes each input row through a 2-agent group chat (UserProxyAgent + AssistantAgent). Returns Outputs DataFrame with response + metadata.
* **`_predict_single(prompt)`** (L312-L361): Async single prediction via `RoundRobinGroupChat`.
* **`_predict_batch(prompts)`** (L363-L400): Parallel batch predictions using `asyncio.gather`.

```mermaid
classDiagram
    class BaselineAutogenModel {
        +T.Literal['BaselineAutogenModel'] KIND
        +Optional[int] max_tokens
        +Optional[Dict[str, Any]] model_config_data
        +Optional[str] model_config_path
        +Optional[float] temperature
        +explain_model(): schemas.FeatureImportances
        +explain_samples(inputs: schemas.Inputs): schemas.SHAPValues
        +fit(inputs: schemas.Inputs, targets: schemas.Targets): 'BaselineAutogenModel'
        +get_internal_model(): Any
        +load_context(model_config: Dict[str, Any]): None
        +load_context_path(model_config_path: Optional[str]): None
        +predict(inputs: schemas.Inputs): schemas.Outputs
    }
    class Model {
        +str KIND
        +explain_model(): schemas.FeatureImportances
        +explain_samples(inputs: schemas.Inputs): schemas.SHAPValues
        +fit(inputs: schemas.Inputs, targets: schemas.Targets): T.Self
        +get_internal_model(): T.Any
        +get_params(deep: bool): Params
        +load_context(model_config: Dict[str, Any]): None
        +predict(inputs: schemas.Inputs): schemas.Outputs
        +set_params(): T.Self
    }
    Model <|-- BaselineAutogenModel
    TrainingJob --> BaselineAutogenModel
    TuningJob --> BaselineAutogenModel
    Model --> Adapter
```
