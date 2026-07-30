---
type: "module-architecture"
title: "Agents Architecture: src/autogen_team/application/agents"
description: "Technical architecture and class hierarchy for multi-agent execution components"
tags: ["architecture", "agents", "autogen", "mcp", "openwiki"]
timestamp: "2026-07-30T00:00:00Z"
---

# Module Name: application/agents

* **Source Directory Reference:** `src/autogen_team/application/agents/`
* **Package Dependency:** Upstream: `src/autogen_team/infrastructure/client/mcp_client.py`. Downstream: `src/autogen_team/application/workflows/`.

## 1. Executive Summary & Purpose

The `application/agents` module implements specialized multi-agent roles (`CoderAgent`, `PlannerAgent`, `ReviewerAgent`, `TesterAgent`, `DocumentationAgent`). Each agent encapsulates a specialized responsibility within the multi-agent development lifecycle, communicating asynchronously with the underlying tool ecosystem via `MCPClient`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)

```mermaid
classDiagram
    direction BT
    class CoderAgent {
        -client: MCPClient
        +execute_task(task: Dict)* Dict
    }
    class PlannerAgent {
        -client: MCPClient
        +execute_task(task: Dict)* Dict
    }
    class ReviewerAgent {
        -client: MCPClient
        +execute_task(task: Dict)* Dict
    }
    class TesterAgent {
        -client: MCPClient
        +execute_task(task: Dict)* Dict
    }
    class DocumentationAgent {
        -client: MCPClient
        +execute_task(task: Dict)* Dict
    }
    class MCPClient {
        +connect()
        +call_tool(name: str, args: Dict)
        +disconnect()
    }

    CoderAgent --> MCPClient : Uses for code execution
    PlannerAgent --> MCPClient : Uses for mission planning
    ReviewerAgent --> MCPClient : Uses for security review
    TesterAgent --> MCPClient : Uses for test execution
    DocumentationAgent --> MCPClient : Uses for doc generation
```

## 3. Package & Class Relations

* **Agent Role Specialization:**
  * `CoderAgent`: Dispatches code execution tasks via MCP tool `execute_code`.
  * `PlannerAgent`: Formulates high-level breakdown plans via MCP tool `plan_mission`.
  * `ReviewerAgent`: Analyzes code vulnerability and quality via MCP tool `security_review`.
  * `TesterAgent`: Executes unit and integration test suites via MCP tool `run_tests`.
  * `DocumentationAgent`: Generates structured markdown specifications via MCP tool `generate_mission_docs`.
* **Lifecycle Management:** All agents initiate an asynchronous MCP session (`connect()`), issue tool requests (`call_tool()`), and release network resources in a `finally` block (`disconnect()`).

## 4. Execution Flow & Runtime Behavior

```mermaid
sequenceDiagram
    autonumber
    participant Workflow as Autonomous Mission Workflow
    participant Agent as CoderAgent / PlannerAgent
    participant Client as MCPClient
    participant Tool as MCP Server Tool

    Workflow->>Agent: execute_task(task_definition)
    Agent->>Client: connect()
    Client-->>Agent: Connection Established
    Agent->>Client: call_tool("execute_code", {"task": task_definition})
    Client->>Tool: Execute tool command over RPC
    Tool-->>Client: Return execution payload / stdout
    Client-->>Agent: Return parsed dictionary
    Agent->>Client: disconnect()
    Agent-->>Workflow: Return task completion result
```

---

* **Source Citations:**
  * Coder Agent: `src/autogen_team/application/agents/coder_agent.py:6-23`
  * Planner Agent: `src/autogen_team/application/agents/planner_agent.py:6-23`
  * Reviewer Agent: `src/autogen_team/application/agents/reviewer_agent.py:6-23`
  * Tester Agent: `src/autogen_team/application/agents/tester_agent.py:6-23`
  * Documentation Agent: `src/autogen_team/application/agents/documentation_agent.py:6-23`
