# Backlog for Class Diagram Implementation

- [Backlog for Class Diagram Implementation](#backlog-for-class-diagram-implementation)
  - [**Features/packages**](#featurespackages)
    - [**FE: Core**](#fe-core)
    - [**FE: Input Outputs**](#fe-input-outputs)
    - [**FE: Jobs**](#fe-jobs)
    - [**FE: Utils**](#fe-utils)
    - [**FE: main**](#fe-main)
    - [**FE: Tasks for CI/CD**](#fe-tasks-for-cicd)
  - [UML packages relations](#uml-packages-relations)

---

## **Features/packages**

### **FE: Core**

https://github.com/mlflow/mlflow/blob/master/examples/gateway/mlflow_models/README.md

   The foundational components of the system that ensure efficient functionality across various modules:

- **[US: Schemas](Schemas_stories.md)**: Define structured data formats for input, output, and intermediate processes, ensuring consistency and validation throughout the pipeline.
- **[US: Models](Models_stories.md)**: Define the structure of machine learning models, including architectures and checkpoints, to standardize training and deployment.
- **[US: Metrics](Metrics_stories.md)**: Provide standardized measurements for model performance, accuracy, and evaluation. Useful for tracking improvement and identifying bottlenecks.


### **FE: Input Outputs**

 Handle configuration, data ingestion, and external environment variables for seamless integration:

- **[US: Config](Configs_stories.md)**: Store and manage configuration files to customize and control the behavior of different modules.
- **[US: Dataset](Datasets_stories.md)**: Handle loading, preprocessing, and managing data sets for training, evaluation, and inference.
- **[US: OSVariables](OSvariables_stories.md)**: Provide environment variables and system-level configurations for portability across various environments.
- **[US: Registries](Regristries_stories.md)**: Maintain a central repository for tracking artifacts like models, datasets, and configurations.
- **[US: Services](Services_stories.md)**: Connect and integrate external or internal services such as APIs, databases, and message brokers.

### **FE: Jobs**

   Define and manage specific tasks and workflows for various stages in the machine learning lifecycle:

- **[US: Base](Base_stories.md)**: The foundational job configurations and implementations shared across all job types.
- **[US: Evaluations](Evaluations_stories.md)**: Execute performance tests and comparisons for models, ensuring they meet predefined criteria.
- **[US: Explanations](Explanations_stories.md)**: Generate explainability reports for machine learning models to provide insights into predictions and decisions.
- **[US: Inference](Inference_stories.md)**: Execute predictions using trained models, optimized for low latency and high throughput.
- **US: KafkaInference**: Specialized inference jobs designed to integrate with Kafka for real-time data streaming applications.
- **[US: Promotion](Promotions_stories.md)**: Automate the promotion of models from development to production environments, ensuring governance and validation.
- **[US: Training](Trainning_stories.md)**: Handle the full model training process, including data preparation, model fitting, and checkpointing.
- **[US: Tuning](Tuning_stories.md)**: Optimize hyperparameters and configurations to improve model performance systematically.

### **FE: Utils**

Auxiliary tools and configurations that enhance functionality and streamline development

- **[US: Searchers](Searchers_stories.md)**: Define functionalities for finding the best hyperparameters for a model.
- **[US: Signers](Signers_stories.md)**:  Generate signatures for AI/ML models.
- **[US: Splitters](Splitters_stories.md)**: Split dataframes into subsets for model training and evaluation.

### **FE: main**

General execution scripts

- **[US. Scripts](Scripts_stories.md)**: Include utility scripts for automating tasks, data handling, and system management.
- **[US: Settings](Settings_stories.md)**: Centralize settings and constants used across different modules for consistency and maintainability.

### **FE: Tasks for CI/CD**

Break down operational processes into manageable, modular tasks

- **US: Checks**: Validate system and code integrity with automated checks for errors, standards, and best practices.
- **US: Cleans**: Perform data cleaning and preprocessing to ensure data quality and consistency.
- **US: Commits**: Automate code versioning and commit standards for collaborative development.
- **US: Containers**: Build and manage containerized environments for consistent deployments across platforms.
- **US: Docs**: Generate and maintain documentation for all modules, ensuring clear usage and collaboration.
- **US: Formats**: Enforce code formatting standards for readability and maintainability.
- **US: Installs**: Manage dependency installation for smooth setup across different environments.
- **US: MLFlow**: Integrate with MLFlow for experiment tracking, model registry, and deployment workflows.
- **US: Packages**: Organize and manage Python or other language packages for modularized codebases.
- **US: Projects**: Create and maintain projects, ensuring that each has the structure, configuration, and tools needed for success.

## UML packages relations

```mermaid
graph LR
    subgraph model_name
    end
    subgraph model_name.__main__
    end
    subgraph model_name.core
    end
    subgraph model_name.core.metrics
    end
    subgraph model_name.core.models
    end
    subgraph model_name.core.schemas
    end
    subgraph model_name.io
    end
    subgraph model_name.io.configs
    end
    subgraph model_name.io.datasets
    end
    subgraph model_name.io.osvariables
    end
    subgraph model_name.io.registries
    end
    subgraph model_name.io.services
    end
    subgraph model_name.jobs
    end
    subgraph model_name.jobs.base
    end
    subgraph model_name.jobs.evaluations
    end
    subgraph model_name.jobs.explanations
    end
    subgraph model_name.jobs.inference
    end
    subgraph model_name.jobs.kafkainference
    end
    subgraph model_name.jobs.promotion
    end
    subgraph model_name.jobs.training
    end
    subgraph model_name.jobs.tuning
    end
    subgraph model_name.scripts
    end
    subgraph model_name.settings
    end
    subgraph model_name.utils
    end
    subgraph model_name.utils.searchers
    end
    subgraph model_name.utils.signers
    end
    subgraph model_name.utils.splitters
    end

    model_name.__main__ --> model_name
    model_name.__main__ --> model_name.scripts
    model_name.core.metrics --> model_name.core
    model_name.core.metrics --> model_name.core.models
    model_name.core.metrics --> model_name.core.schemas
    model_name.core.models --> model_name.core
    model_name.core.models --> model_name.core.schemas
    model_name.io.registries --> model_name.core
    model_name.io.registries --> model_name.core.models
    model_name.io.registries --> model_name.core.schemas
    model_name.io.registries --> model_name.utils
    model_name.io.registries --> model_name.utils.signers
    model_name.io.services --> model_name.io.osvariables
    model_name.jobs --> model_name.jobs.evaluations
    model_name.jobs --> model_name.jobs.explanations
    model_name.jobs --> model_name.jobs.inference
    model_name.jobs --> model_name.jobs.promotion
    model_name.jobs --> model_name.jobs.training
    model_name.jobs --> model_name.jobs.tuning
    model_name.jobs.base --> model_name.io
    model_name.jobs.base --> model_name.io.services
    model_name.jobs.evaluations --> model_name.core
    model_name.jobs.evaluations --> model_name.core.metrics
    model_name.jobs.evaluations --> model_name.core.schemas
    model_name.jobs.evaluations --> model_name.io
    model_name.jobs.evaluations --> model_name.io.datasets
    model_name.jobs.evaluations --> model_name.io.registries
    model_name.jobs.evaluations --> model_name.io.services
    model_name.jobs.evaluations --> model_name.jobs
    model_name.jobs.evaluations --> model_name.jobs.base
    model_name.jobs.explanations --> model_name.core
    model_name.jobs.explanations --> model_name.core.schemas
    model_name.jobs.explanations --> model_name.io
    model_name.jobs.explanations --> model_name.io.datasets
    model_name.jobs.explanations --> model_name.io.registries
    model_name.jobs.explanations --> model_name.jobs
    model_name.jobs.explanations --> model_name.jobs.base
    model_name.jobs.inference --> model_name.core
    model_name.jobs.inference --> model_name.core.schemas
    model_name.jobs.inference --> model_name.io
    model_name.jobs.inference --> model_name.io.datasets
    model_name.jobs.inference --> model_name.io.registries
    model_name.jobs.inference --> model_name.jobs
    model_name.jobs.inference --> model_name.jobs.base
    model_name.jobs.promotion --> model_name.jobs
    model_name.jobs.promotion --> model_name.jobs.base
    model_name.jobs.training --> model_name.core
    model_name.jobs.training --> model_name.core.metrics
    model_name.jobs.training --> model_name.core.models
    model_name.jobs.training --> model_name.core.schemas
    model_name.jobs.training --> model_name.io
    model_name.jobs.training --> model_name.io.datasets
    model_name.jobs.training --> model_name.io.registries
    model_name.jobs.training --> model_name.io.services
    model_name.jobs.training --> model_name.jobs
    model_name.jobs.training --> model_name.jobs.base
    model_name.jobs.training --> model_name.utils
    model_name.jobs.training --> model_name.utils.signers
    model_name.jobs.training --> model_name.utils.splitters
    model_name.jobs.tuning --> model_name.core
    model_name.jobs.tuning --> model_name.core.metrics
    model_name.jobs.tuning --> model_name.core.models
    model_name.jobs.tuning --> model_name.core.schemas
    model_name.jobs.tuning --> model_name.io
    model_name.jobs.tuning --> model_name.io.datasets
    model_name.jobs.tuning --> model_name.io.services
    model_name.jobs.tuning --> model_name.jobs
    model_name.jobs.tuning --> model_name.jobs.base
    model_name.jobs.tuning --> model_name.utils
    model_name.jobs.tuning --> model_name.utils.searchers
    model_name.jobs.tuning --> model_name.utils.splitters
    model_name.scripts --> model_name
    model_name.scripts --> model_name.io
    model_name.scripts --> model_name.io.configs
    model_name.scripts --> model_name.settings
    model_name.settings --> model_name
    model_name.settings --> model_name.jobs
    model_name.utils.searchers --> model_name.core
    model_name.utils.searchers --> model_name.core.metrics
    model_name.utils.searchers --> model_name.core.models
    model_name.utils.searchers --> model_name.core.schemas
    model_name.utils.searchers --> model_name.utils
    model_name.utils.searchers --> model_name.utils.splitters
    model_name.utils.signers --> model_name.core
    model_name.utils.signers --> model_name.core.schemas
    model_name.utils.splitters --> model_name.core
    model_name.utils.splitters --> model_name.core.schemas

```

```mermaid
graph TD
    A[FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models]
    A --> B[Financial AI Agents]
    A --> C[Financial LLMs]
    A --> D[LLMOps]
    A --> E[Multi-Source LLM Foundation Models]

    B --> B1[Market Forecasting Agents]
    B --> B2[Document Analysis & Generation Agents]
    
    B1 --> B1A[Trading Strategist Agent]
    B1 --> B1B[Multimodal Agent]
    B1 --> B1C[Global Stock Market Agent]
    
    B2 --> B2A[Earnings Report Analysis Agent]
    B2 --> B2B[Risk Assessment Report Analysis Agent]
    B2 --> B2C[Financial Report Generation Agent]
    B2 --> B2D[Equity Research Report Generation Agent]

    C --> C1[Financial Large Language Model FinGPT]
    C --> C2[Financial Reinforcement Learning FinRL]
    C --> C3[Financial Machine Learning FinML]
    
    D --> D1[Prompt Engineering]
    D --> D2[SFT]
    D --> D3[Model Deployment]
    D --> D4[LoRA/QLoRA]
    D --> D5[Model Evaluation]
    D --> D6[Smart Scheduler]
    
    D --> D7[Instruction Tuning]
    D --> D8[RLHF]
    D --> D9[CI/CD]

    D --> F[DataOps]
    F --> F1[FinRL-Meta]
    F1 --> F1A[Tabular Data]
    F1 --> F1B[Gym Env]
    F --> F2[Financial Data & FinNLP]
    F2 --> F2A[Market News]
    F2 --> F2B[Social Media]
    F2 --> F2C[Market Sentiment]
    F2 --> F2D[Financial Ratios]
    F --> F3[Vector Database]
    F --> F4[RAG]
    F --> F5[Knowledge Graph]

    E --> E1[Llama3]
    E --> E2[Falcon]
    E --> E3[ChatGLM3]
    E --> E4[ChatGPT]
    E --> E5[Gemma]
    E --> E6[Baichuan]
    E --> E7[Mistral]

```
