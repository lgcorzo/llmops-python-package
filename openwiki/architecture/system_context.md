---
iso_doc_type: "Description"
iso_viewpoint: "ContextView"
type: "architecture"
title: "System Context View"
description: "ISO 42010 Context View defining system boundaries, external actors, and integration points for the autogen_team system."
tags: ["iso42010", "context", "boundaries", "integrations"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# System Context View: Autogen Team

## 1. System Boundary

The `autogen_team` package operates as the **intelligence core** within the Dark Gravity CA/CD Autonomous Agent Factory cluster. It consumes and produces interactions with multiple external systems via well-defined integration points.

## 2. Context Diagram

```mermaid
C4Context
    title System Context Diagram — Autogen Team

    Person(developer, "Developer", "Triggers missions, manages configs")
    Person(ml_engineer, "ML Engineer", "Trains models, evaluates metrics")

    System(autogen_team, "Autogen Team", "Autonomous Agentic Core: multi-agent orchestration, LLMOps pipelines, MCP server")

    System_Ext(hatchet, "Hatchet", "Durable workflow orchestration (task DAGs, fan-out)")
    System_Ext(kafka, "Kafka", "Event streaming for real-time inference & A2A messaging")
    System_Ext(mlflow, "MLflow", "Experiment tracking, model registry, artifact storage")
    System_Ext(litellm, "LiteLLM Proxy", "Unified LLM API gateway (Azure, OpenAI, Ollama)")
    System_Ext(r2r, "R2R RAG", "Semantic code search & knowledge graph")
    System_Ext(minio, "MinIO / S3", "Object storage for model artifacts & sandbox outputs")
    System_Ext(e2b, "E2B / Firecracker", "Ephemeral MicroVM sandboxes for secure code execution")
    System_Ext(openziti, "OpenZiti", "Zero-trust network overlay for A2A communication")

    Rel(developer, autogen_team, "CLI / Invoke tasks / MCP Client")
    Rel(ml_engineer, autogen_team, "Training configs / Evaluation jobs")
    Rel(autogen_team, hatchet, "Workflow registration & execution", "gRPC/HTTP")
    Rel(autogen_team, kafka, "Produce/consume predictions", "Confluent Kafka")
    Rel(autogen_team, mlflow, "Log experiments, register models", "HTTP REST")
    Rel(autogen_team, litellm, "LLM completions for agents/tools", "HTTP/OpenAI API")
    Rel(autogen_team, r2r, "Semantic search & code indexing", "HTTP REST")
    Rel(autogen_team, minio, "Upload sandbox artifacts", "S3 API (boto3)")
    Rel(autogen_team, e2b, "Create/execute/destroy sandboxes", "E2B SDK")
    Rel(autogen_team, openziti, "Encrypted A2A agent traffic", "OpenZiti SDK")
```

## 3. External System Integration Details

| External System | Integration Module | Protocol | Configuration Source |
| :--- | :--- | :--- | :--- |
| **Hatchet** | `infrastructure/services/hatchet_service.py:L15-L86` | gRPC/HTTP | `Env.hatchet_client_*` |
| **Kafka** | `infrastructure/messaging/kafka_app.py:L86-L234` | Confluent Kafka | `DEFAULT_KAFKA_SERVER` env var |
| **MLflow** | `infrastructure/services/mlflow_service.py`, `registry/adapters/mlflow_adapter.py:L1-L341` | HTTP REST | `Env.mlflow_*` |
| **LiteLLM** | `infrastructure/services/mcp_service.py:L17-L84` | OpenAI-compatible API | `Env.litellm_*` |
| **R2R RAG** | `infrastructure/services/mcp_service.py:L44-L47` | HTTP REST | `Env.r2r_base_url` |
| **MinIO / S3** | `infrastructure/services/sandbox_service.py:L144-L189` | S3 API (boto3) | `MLFLOW_S3_ENDPOINT_URL`, `AWS_*` |
| **E2B** | `infrastructure/services/sandbox_service.py:L39-L143` | E2B SDK | `E2B_AVAILABLE` feature flag |
| **OpenZiti** | A2A Protocol schemas (`infrastructure/messaging/a2a_protocol.py:L1-L45`) | OpenZiti SDK | Cluster-level config |

## 4. Data Flow Summary

```mermaid
flowchart LR
    subgraph Inputs
        CLI["CLI / Invoke"]
        KafkaIn["Kafka Input Topic"]
        MCPReq["MCP Client Request"]
    end

    subgraph autogen_team["Autogen Team"]
        Jobs["Batch Jobs (Training/Eval/Inference)"]
        Agents["Autonomous Agents"]
        MCPTools["MCP Tools"]
        Workflows["Hatchet Workflows"]
    end

    subgraph Outputs
        MLflowReg["MLflow Registry"]
        KafkaOut["Kafka Output Topic"]
        Artifacts["MinIO Artifacts"]
        PRs["Pull Requests"]
    end

    CLI --> Jobs
    KafkaIn --> Jobs
    MCPReq --> MCPTools
    MCPTools --> Agents
    Agents --> Workflows
    Workflows --> Agents
    Jobs --> MLflowReg
    Jobs --> KafkaOut
    Workflows --> Artifacts
    Workflows --> PRs
```
