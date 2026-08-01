---
iso_doc_type: "Description"
iso_viewpoint: "SequenceView"
type: "architecture"
title: "Runtime Sequence View"
description: "ISO 42010 Sequence View: dynamic interaction flows for autonomous missions, Kafka prediction, and MCP tool invocations."
tags: ["iso42010", "sequence", "runtime", "workflow", "mission"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Runtime Sequence View: Autogen Team

## 1. Autonomous Mission Lifecycle

The flagship workflow orchestrates Plan → Fan-Out → Review → Document using Hatchet's durable execution model (`src/autogen_team/application/workflows/autonomous_mission.py:L1-L214`).

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Hatchet as Hatchet Orchestrator
    participant PlanStep as plan()
    participant Planner as PlannerAgent
    participant MCP as MCPClient
    participant FanOut as fan_out_tasks()
    participant DT as DevelopTaskWorkflow
    participant Coder as CoderAgent
    participant Agg as aggregate_and_review()
    participant Tester as TesterAgent
    participant Reviewer as ReviewerAgent
    participant DocStep as document_mission()
    participant DocAgent as DocumentationAgent

    Dev->>Hatchet: Trigger "autonomous_mission" event (MissionInput)
    activate Hatchet

    Hatchet->>PlanStep: Step 1: plan()
    activate PlanStep
    PlanStep->>Planner: create_plan(goal, repo_path)
    activate Planner
    Planner->>MCP: connect()
    Planner->>MCP: call_tool("plan_mission", {goal})
    MCP-->>Planner: Task DAG
    Planner->>MCP: disconnect()
    Planner-->>PlanStep: mission_plan
    deactivate Planner
    PlanStep-->>Hatchet: {plan: mission_plan}
    deactivate PlanStep

    Hatchet->>FanOut: Step 2: fan_out_tasks()
    activate FanOut
    loop For each task in plan
        FanOut->>DT: aio_run_many(TaskInput)
        activate DT
        DT->>Coder: execute_task(task)
        activate Coder
        Coder->>MCP: call_tool("execute_code", {task})
        MCP-->>Coder: code result
        Coder-->>DT: result
        deactivate Coder
        DT-->>FanOut: task result
        deactivate DT
    end
    FanOut-->>Hatchet: {results: [...]}
    deactivate FanOut

    Hatchet->>Agg: Step 3: aggregate_and_review()
    activate Agg
    Agg->>Tester: run_tests()
    activate Tester
    Tester-->>Agg: test_results
    deactivate Tester
    Agg->>Reviewer: review_changes(mission_id, file_changes)
    activate Reviewer
    Reviewer->>MCP: call_tool("security_review", {diff})
    MCP-->>Reviewer: review analysis
    Reviewer-->>Agg: ReviewResult
    deactivate Reviewer
    Agg-->>Hatchet: MissionOutput(status, summary)
    deactivate Agg

    Hatchet->>DocStep: Step 4: document_mission()
    activate DocStep
    DocStep->>DocAgent: generate_docs(mission_id, context)
    activate DocAgent
    DocAgent->>MCP: call_tool("generate_mission_docs", {context})
    MCP-->>DocAgent: diagrams & docs
    DocAgent-->>DocStep: doc_results
    deactivate DocAgent
    DocStep-->>Hatchet: MissionOutput(updated summary)
    deactivate DocStep

    Hatchet-->>Dev: Mission Complete
    deactivate Hatchet
```

## 2. Kafka Real-Time Prediction Flow

The `FastAPIKafkaService` (`src/autogen_team/infrastructure/messaging/kafka_app.py:L86-L234`) provides a dual-interface prediction service.

```mermaid
sequenceDiagram
    participant Client as External Client
    participant FastAPI as FastAPI Server
    participant KConsumer as Kafka Consumer Thread
    participant KProducer as Kafka Producer
    participant Model as BaselineAutogenModel
    participant MLflow as MLflow Registry

    Note over FastAPI, KConsumer: Service startup sequence

    FastAPI->>MLflow: load_model(model_uri)
    activate MLflow
    MLflow-->>FastAPI: PyFunc Model
    deactivate MLflow

    FastAPI->>KConsumer: Start consumer thread (daemon)

    Note over Client, KProducer: Message processing loop

    Client->>KConsumer: Produce to input_topic
    activate KConsumer
    KConsumer->>KConsumer: _poll_message()
    KConsumer->>KConsumer: _process_message(msg)
    KConsumer->>Model: prediction_callback(PredictionRequest)
    activate Model
    Model-->>KConsumer: PredictionResponse
    deactivate Model
    KConsumer->>KProducer: produce(output_topic, result)
    KProducer->>KConsumer: delivery_report(err, msg)
    KConsumer->>KConsumer: consumer.commit(msg)
    deactivate KConsumer
```

## 3. MCP Tool Invocation Pattern

All agents follow a consistent connect → call_tool → disconnect pattern via `MCPClient` (`src/autogen_team/infrastructure/client/mcp_client.py`).

```mermaid
sequenceDiagram
    participant Agent as Agent (Coder/Planner/...)
    participant Client as MCPClient
    participant Server as MCP Server (stdio)
    participant Tool as MCP Tool Function
    participant LiteLLM as LiteLLM Proxy
    participant R2R as R2R RAG

    Agent->>Client: connect()
    activate Client
    Client->>Server: Initialize stdio session

    Agent->>Client: call_tool(tool_name, args)
    Client->>Server: JSON-RPC request
    Server->>Tool: Dispatch to tool function

    alt plan_mission / execute_code / generate_mission_docs
        Tool->>LiteLLM: acompletion(model, messages)
        LiteLLM-->>Tool: LLM response
    else retrieve_context / index_code
        Tool->>R2R: HTTP request to RAG API
        R2R-->>Tool: Search results / index confirmation
    else security_review
        Tool->>Tool: _scan_owasp_patterns(diff)
        Tool->>R2R: _query_r2r_security(diff)
        R2R-->>Tool: Security knowledge
    end

    Tool-->>Server: Tool result
    Server-->>Client: JSON-RPC response
    Client-->>Agent: Result dict
    deactivate Client

    Agent->>Client: disconnect()
```

## 4. Legacy Batch Job Execution

All batch jobs use a context-manager pattern with automatic service lifecycle management (`src/autogen_team/application/jobs/base.py:L21-L86`).

```mermaid
sequenceDiagram
    participant CLI as CLI (scripts.py)
    participant Settings as MainSettings
    participant Job as Job (Training/Eval/...)
    participant Logger as LoggerService
    participant Alerts as AlertsService
    participant MLflow as MlflowService

    CLI->>Settings: Parse YAML config
    CLI->>Job: Instantiate from config

    Job->>Job: __enter__()
    activate Job
    Job->>Logger: start()
    Job->>Alerts: start()
    Job->>MLflow: start()

    Job->>Job: run()
    Note right of Job: Execute domain logic (train/eval/infer/...)

    Job->>Job: __exit__()
    Job->>MLflow: stop()
    Job->>Alerts: stop()
    Job->>Logger: stop()
    deactivate Job
```
