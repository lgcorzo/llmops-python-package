# Model Entities
The `models/entities.py` file defines the core abstraction for machine learning models within the system. It uses a contract-based approach to ensure that different AI/ML frameworks (e.g., Scikit-learn, PyTorch, TensorFlow) can be swapped interchangeably as long as they implement the required interface.

## Model Architecture
The primary abstract class `Model` enforces the lifecycle of an ML model: loading configuration, fitting on data, and producing predictions.

```mermaid
classDiagram
    class Model {
        <<Abstract>>
        +String KIND
        +get_params() Params
        +set_params(**params)
        +load_context(model_config)
        +fit(inputs, targets)
        +predict(inputs)
        +explain_model()
    }

    class ModelPersistence {
        <<Interface>>
        +save(model, path)
        +load(path)
    }

    note for Model "Standardizes the interaction between \nthe application logic and raw ML models."
```

## Key Components:
- **`Model` (Base Class)**: 
    - Inherits from `pydantic.BaseModel` to handle validation of model configurations.
    - Implements standard methods like `get_params` and `set_params` for dynamic configuration management.
    - Defines abstract methods `load_context`, `fit`, and `predict` which must be implemented by specific models (e.g., `OpenAIModel`, `LlamaModel`).
- **`ModelRepository`**: 
    - Defined in `src/autogen_team/models/repositories.py`.
    - Provides a standard interface for persisting models to storage (File System, S3, etc.).

*Refer to:*
- *Core Schemas: `/openwiki/modules/core-schemas.md`*
- *Source File: `src/autogen_team/models/entities.py`*
