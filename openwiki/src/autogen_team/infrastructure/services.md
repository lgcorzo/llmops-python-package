---
type: "module-architecture"
title: "Infrastructure Services Architecture: src/autogen_team/infrastructure/services"
description: "Technical architecture and class hierarchy for infrastructure management services"
tags: ["architecture", "infrastructure", "services", "mlflow", "hatchet", "sandbox", "openwiki"]
timestamp: "2026-07-30T00:00:00Z"
---

# Module Name: infrastructure/services

* **Source Directory Reference:** `src/autogen_team/infrastructure/services/`
* **Package Dependency:** Upstream: `pydantic`, `loguru`, `mlflow`, `hatchet_sdk`. Downstream: `src/autogen_team/application/jobs/base.py`.

## 1. Executive Summary & Purpose

The `infrastructure/services` module defines the lifecycle managers for system-wide infrastructure services: `LoggerService`, `AlertsService`, `MlflowService`, `HatchetService`, `MCPService`, and `SandboxService`. Each service implements start/stop lifecycle methods and is managed inside `Job.__enter__()`/`__exit__()` context blocks.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)

```mermaid
classDiagram
    direction BT
    class Service {
        <<interface>>
        +start()* None
        +stop()* None
    }
    class LoggerService {
        +start() None
        +stop() None
        +logger() Logger
    }
    class AlertsService {
        +start() None
        +stop() None
        +send_alert(msg: str) None
    }
    class MlflowService {
        +start() None
        +stop() None
        +log_params(params: dict) None
        +log_metrics(metrics: dict) None
    }
    class HatchetService {
        +start() None
        +stop() None
        +trigger_workflow(name: str, payload: dict) None
    }
    class MCPService {
        +start() None
        +stop() None
        +register_tool(name, handler) None
    }
    class SandboxService {
        +start() None
        +stop() None
        +run_in_sandbox(cmd: str) dict
    }

    Service <|-- LoggerService
    Service <|-- AlertsService
    Service <|-- MlflowService
    Service <|-- HatchetService
    Service <|-- MCPService
    Service <|-- SandboxService
```

## 3. Package & Class Relations

* **Service Injection (`Job` Base Class):** Default instances of `LoggerService`, `AlertsService`, and `MlflowService` are instantiated as frozen Pydantic fields on `Job`, ensuring consistent logging, alerting, and experiment tracking across all execution runs.
* **Sandbox & MCP Isolation:** `SandboxService` provides code execution isolation for `ExecuteCodeTool`, while `MCPService` handles tool registration and RPC routing.

## 4. Execution Flow & Runtime Behavior

```mermaid
sequenceDiagram
    autonumber
    participant JobContext as Job Context Manager
    participant Logger as LoggerService
    participant Alerts as AlertsService
    participant Mlflow as MlflowService

    JobContext->>Logger: start()
    Logger-->>JobContext: Logger Initialized
    JobContext->>Alerts: start()
    Alerts-->>JobContext: Alerts Initialized
    JobContext->>Mlflow: start()
    Mlflow-->>JobContext: MLflow Run Started

    Note over JobContext: Execution of Job Pipeline

    JobContext->>Mlflow: stop()
    Mlflow-->>JobContext: MLflow Run Terminated
    JobContext->>Alerts: stop()
    Alerts-->>JobContext: Alerts Shutdown
    JobContext->>Logger: stop()
    Logger-->>JobContext: Logger Flushed & Shutdown
```

---

* **Source Citations:**
  * Logger Service: `src/autogen_team/infrastructure/services/logger_service.py:1-35`
  * Alert Service: `src/autogen_team/infrastructure/services/alert_service.py:1-35`
  * MLflow Service: `src/autogen_team/infrastructure/services/mlflow_service.py:1-35`
  * Hatchet Service: `src/autogen_team/infrastructure/services/hatchet_service.py:1-35`
  * MCP Service: `src/autogen_team/infrastructure/services/mcp_service.py:1-35`
  * Sandbox Service: `src/autogen_team/infrastructure/services/sandbox_service.py:1-35`
