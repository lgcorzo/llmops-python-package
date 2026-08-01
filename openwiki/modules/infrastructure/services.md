---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Infrastructure Services"
source_path: "src/autogen_team/infrastructure/services/"
description: "Global service abstractions: Service, LoggerService, MCPService, MlflowService, HatchetService, AlertsService, SandboxService."
tags: ["infrastructure", "services", "otel", "hatchet", "mlflow", "sandbox"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Module Specification: Infrastructure Services

* **Source Reference:** `src/autogen_team/infrastructure/services/` (7 service files)
* **Downstream Consumers:** [[Modules/Application/Jobs]], [[Modules/Application/Agents]], [[Modules/Application/MCPTools]]

## 1. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Service {
        <<abstract>>
        +start()* void
        +stop() void
    }
    class LoggerService {
        +sink: str = "stderr"
        +level: str = "DEBUG"
        +format: str
        +colorize: bool = True
        +serialize: bool = False
        +start() void
        +logger() Logger
    }
    class MCPService {
        +litellm_api_base: str
        +litellm_api_key: str
        +litellm_model: str
        +r2r_base_url: str
        +host: str
        +port: int
        +start() void
        +get_prompt(tool_name: str, role: str) str
    }
    class MlflowService {
        +tracking_uri: str
        +registry_uri: str
        +experiment_name: str
        +start() void
        +stop() void
    }
    class HatchetService {
        +token: str
        +namespace: str
        +start() void
        +stop() void
        +client() Hatchet
    }
    class AlertsService {
        +start() void
    }
    class SandboxService {
        -use_e2b_fallback: bool
        -active_sandboxes: Dict
        +create_sandbox(metadata: Dict) str
        +execute(sandbox_id: str, command: str) SandboxExecutionResult
        +run_python_tests(sandbox_id: str, workspace_dir: str) SandboxExecutionResult
        +destroy(sandbox_id: str) void
        +upload_artifact(sandbox_id: str, file_path: str) str
    }

    Service <|-- LoggerService : Inheritance
    Service <|-- MCPService : Inheritance
    Service <|-- MlflowService : Inheritance
    Service <|-- HatchetService : Inheritance
    Service <|-- AlertsService : Inheritance
```

## 2. Service Specifications

### `Service` (abstract base) (`src/autogen_team/infrastructure/services/logger_service.py:L27-L35`)

Abstract base class for all global services. Uses Pydantic `BaseModel` with `strict=True, frozen=True, extra="forbid"`.

### `LoggerService` (`src/autogen_team/infrastructure/services/logger_service.py:L38-L88`)

Structured logging with OpenTelemetry integration:
- Configures `loguru` logger with customizable sink, level, format
- Sets up `TracerProvider` with OTLP span exporter
- Sets up `LoggerProvider` with OTLP log exporter
- Propagates loguru logs to standard Python logging via `PropagateHandler`

### `MCPService` (`src/autogen_team/infrastructure/services/mcp_service.py:L17-L84`)

Configuration and utilities for the MCP tool server:
- Loads LiteLLM configuration from `Env` singleton
- Loads MCP prompts from YAML config file (`confs/mcp_prompts.yaml`)
- Provides `get_prompt(tool_name, role)` for retrieving system prompts

### `HatchetService` (`src/autogen_team/infrastructure/services/hatchet_service.py:L15-L86`)

Manages the Hatchet workflow orchestration client:
- Lazy initialization via `client` property
- Automatic mock fallback for local development and tests
- Environment variable forwarding (`HATCHET_CLIENT_TOKEN`, `HATCHET_CLIENT_HOST_PORT`, etc.)

### `SandboxService` (`src/autogen_team/infrastructure/services/sandbox_service.py:L39-L189`)

Manages ephemeral MicroVM sandboxes:
- Creates E2B Code Interpreter sandboxes (Firecracker-based)
- Executes commands with configurable timeout
- Uploads sandbox artifacts to MinIO/S3 via boto3
- Path traversal protection via `safe_join()`
