---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Infrastructure IO"
source_path: "src/autogen_team/infrastructure/io/"
description: "OmegaConf config parsing and Pydantic Settings Env singleton for environment variable management."
tags: ["infrastructure", "io", "config", "omegaconf", "pydantic-settings"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Module Specification: Infrastructure IO

* **Source Reference:** `src/autogen_team/infrastructure/io/` (2 files)
* **Downstream Consumers:** All layers via `Env` singleton, [[Modules/Application/Jobs]] via config parsing

## 1. OmegaConf Config Parsing (`configs.py`)

**Source:** `src/autogen_team/infrastructure/io/configs.py:L1-L69`

Provides parse, merge, and convert operations for OmegaConf configuration objects.

```mermaid
flowchart LR
    YAML["YAML File"] -->|parse_file| Config["Config (ListConfig | DictConfig)"]
    String["Config String"] -->|parse_string| Config
    Config -->|merge_configs| Merged["Merged Config"]
    Merged -->|to_object| PythonObj["Python dict/list"]
```

| Function | Signature | Purpose |
| :--- | :--- | :--- |
| `parse_file(path)` | `str -> Config` | Load YAML from disk via `OmegaConf.load()` |
| `parse_string(string)` | `str -> Config` | Parse inline config string via `OmegaConf.create()` |
| `merge_configs(configs)` | `Sequence[Config] -> Config` | Deep merge multiple configs via `OmegaConf.merge()` |
| `to_object(config, resolve)` | `Config -> object` | Convert to Python object with optional variable resolution |

## 2. Environment Variables Singleton (`osvariables.py`)

**Source:** `src/autogen_team/infrastructure/io/osvariables.py:L15-L53`

```mermaid
classDiagram
    class Singleton {
        <<abstract>>
        -_instances: Dict
        +__new__(cls) Singleton
    }
    class Env {
        +mlflow_tracking_uri: str
        +mlflow_registry_uri: str
        +mlflow_experiment_name: str
        +aws_access_key_id: str
        +aws_secret_access_key: str
        +hatchet_client_token: str
        +hatchet_namespace: str
        +litellm_api_base: str
        +litellm_api_key: str
        +litellm_model: str
        +r2r_base_url: str
        +mcp_host: str
        +mcp_port: int
        +mcp_prompts_path: str
    }
    Singleton <|-- Env : Inheritance
    BaseSettings <|-- Env : Inheritance
```

### Configuration Groups

| Group | Variables | Purpose |
| :--- | :--- | :--- |
| **MLflow** | `mlflow_tracking_uri`, `mlflow_registry_uri`, `mlflow_experiment_name`, `mlflow_registered_model_name` | Experiment tracking & model registry |
| **S3/MinIO** | `aws_access_key_id`, `aws_secret_access_key`, `mlflow_s3_endpoint_url`, `mlflow_s3_ignore_tls` | Object storage auth |
| **Hatchet** | `hatchet_client_token`, `hatchet_namespace`, `hatchet_client_host_port`, `hatchet_client_server_url`, `hatchet_client_tls_strategy` | Workflow orchestration |
| **LiteLLM** | `litellm_api_base`, `litellm_api_key`, `litellm_model` | LLM gateway |
| **R2R** | `r2r_base_url` | RAG API |
| **MCP** | `mcp_host`, `mcp_port`, `mcp_prompts_path` | MCP server |
