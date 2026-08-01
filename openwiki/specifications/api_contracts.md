---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "specification"
title: "API & Interface Contracts"
description: "Complete API and interface specification: MCP tool schemas, Kafka messages, FastAPI endpoints, Pydantic models, and abstract class interfaces."
tags: ["iso15289", "api", "contracts", "interfaces", "mcp"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# API & Interface Contracts: Autogen Team

## 1. MCP Tool Schemas

All MCP tools are async functions registered on the MCP server (`src/autogen_team/application/mcp/tools/`).

### `plan_mission(goal: str) -> Dict[str, Any]`
**Source:** `application/mcp/tools/plan_mission.py:L13-L58`
- **Input:** `goal` (str) — High-level goal string
- **Output:** `{"goal": str, "parallel_tasks": List[Dict], "error"?: str}`
- **Backend:** LiteLLM completion with JSON response format

### `execute_code(task: Dict) -> Dict[str, Any]`
**Source:** `application/mcp/tools/execute_code.py`
- **Input:** Task dict with `id`, `description`, `relevant_files`, `constraints`
- **Output:** Execution result with `file_changes`, `status`
- **Backend:** LiteLLM + Sandbox execution

### `run_tests(changes: str, workspace_dir: str) -> Dict[str, Any]`
**Source:** `application/mcp/tools/run_tests.py`
- **Input:** Code changes diff, workspace directory
- **Output:** `{"status": str, "report": str}`
- **Backend:** `SandboxService.run_python_tests()`

### `security_review(diff: str) -> Dict[str, Any]`
**Source:** `application/mcp/tools/security_review.py`
- **Input:** Code diff string
- **Output:** `{"status": str, "analysis": str, "owasp_findings": List, "r2r_findings": List}`
- **Backend:** OWASP regex scanner + R2R RAG query

### `retrieve_context(query: str) -> Dict[str, Any]`
**Source:** `application/mcp/tools/retrieve_context.py`
- **Input:** Semantic search query
- **Output:** `{"documents": List[Dict]}`
- **Backend:** R2R RAG HTTP API

### `index_code(file_path: str, content: str) -> Dict[str, Any]`
**Source:** `application/mcp/tools/index_code.py`
- **Input:** File path and content
- **Output:** `{"status": str, "indexed_path": str}`
- **Backend:** R2R RAG HTTP API

### `generate_mission_docs(mission_context: Dict) -> Dict[str, Any]`
**Source:** `application/mcp/tools/generate_mission_docs.py`
- **Input:** Mission context with goal, tasks, results, file_changes
- **Output:** `{"summary": str, "diagrams": str}`
- **Backend:** LiteLLM completion

## 2. A2A Protocol Messages

Pydantic models for Agent-to-Agent communication (`src/autogen_team/infrastructure/messaging/a2a_protocol.py:L1-L45`):

| Model | Fields | Purpose |
| :--- | :--- | :--- |
| `MissionStart` | `mission_id`, `goal`, `repository_path`, `context?` | Event to start a new autonomous mission |
| `TaskAssignment` | `task_id`, `mission_id`, `description`, `relevant_files`, `constraints?` | Assign a task to a Coder Agent |
| `TaskResult` | `task_id`, `mission_id`, `status` (completed\|failed), `diff?`, `file_changes`, `error_message?` | Result from a Coder Agent |
| `ReviewResult` | `mission_id`, `approved`, `comments`, `suggested_changes?` | Result from a Reviewer Agent |

## 3. Hatchet Workflow Models

Pydantic models for workflow I/O (`src/autogen_team/application/workflows/autonomous_mission.py:L32-L54`):

| Model | Fields | Purpose |
| :--- | :--- | :--- |
| `MissionInput` | `goal: str`, `repository_path: str` | Top-level mission workflow input |
| `TaskInput` | `task_id: str`, `description: str`, `relevant_files: List[str]`, `constraints: str?` | Child coding-task workflow input |
| `MissionOutput` | `status: str`, `pull_request_url: str`, `summary: str` | Final mission workflow output |

## 4. Kafka Message Formats

### Prediction Request (`PredictionRequest`)
**Source:** `infrastructure/messaging/kafka_app.py:L69-L76`

```json
{
  "input_data": {"input": ["text 1", "text 2"]}
}
```

### Prediction Response (`PredictionResponse`)
**Source:** `infrastructure/messaging/kafka_app.py:L79-L82`

```json
{
  "result": {"inference": [0.0], "quality": 0.0, "error": ""}
}
```

## 5. FastAPI Endpoints

| Endpoint | Method | Handler | Response |
| :--- | :--- | :--- | :--- |
| `/health` | GET | `health_check()` | `{"status": "healthy"}` |

**Source:** `infrastructure/messaging/kafka_app.py:L241-L244`

## 6. Abstract Class Interfaces

### Model Interface (`models/entities.py:L33-L130`)

| Method | Signature | Abstract |
| :--- | :--- | :--- |
| `load_context` | `(model_config: Dict[str, Any]) -> None` | ✅ |
| `fit` | `(inputs: Inputs, targets: Targets) -> Self` | ✅ |
| `predict` | `(inputs: Inputs) -> Outputs` | ✅ |
| `explain_model` | `() -> FeatureImportances` | ❌ (raises `NotImplementedError`) |
| `explain_samples` | `(inputs: Inputs) -> SHAPValues` | ❌ (raises `NotImplementedError`) |
| `get_internal_model` | `() -> Any` | ❌ (raises `NotImplementedError`) |

### Service Interface (`infrastructure/services/logger_service.py:L27-L35`)

| Method | Signature | Abstract |
| :--- | :--- | :--- |
| `start` | `() -> None` | ✅ |
| `stop` | `() -> None` | ❌ (default no-op) |

### Reader/Writer Interfaces (`data_access/adapters/datasets.py`)

| Interface | Methods |
| :--- | :--- |
| `Reader` | `read() -> DataFrame`, `lineage(name, data, targets?, predictions?) -> Lineage` |
| `Writer` | `write(data: DataFrame) -> None` |

### Metric Interface (`evaluation/metrics/metrics.py:L33-L109`)

| Method | Signature | Abstract |
| :--- | :--- | :--- |
| `score` | `(targets: DataFrame, outputs: DataFrame) -> float` | ✅ |
| `scorer` | `(model: Model, inputs: Inputs, targets: DataFrame) -> float` | ❌ |
| `to_mlflow` | `() -> MlflowMetric` | ❌ |

### Registry Interfaces (`registry/adapters/mlflow_adapter.py`)

| Interface | Key Method |
| :--- | :--- |
| `Saver` | `save(model, signature, input_example) -> Info` |
| `Loader` | `load(uri: str) -> Adapter` |
| `Register` | `register(name: str, model_uri: str) -> Version` |
