---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Application Workflows"
source_path: "src/autogen_team/application/workflows/autonomous_mission.py"
description: "Hatchet Workflow DSL for the Autonomous Mission lifecycle: Plan → Fan-Out → Review → Document."
tags: ["application", "workflows", "hatchet", "mission", "orchestration"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Module Specification: Application Workflows

* **Source Reference:** `src/autogen_team/application/workflows/autonomous_mission.py` (Lines: L1-L214)
* **Upstream Dependencies:** [[Modules/Application/Agents]], [[Modules/Infrastructure/Services]] (`HatchetService`)

## 1. Architectural Role & Responsibilities

This module defines the flagship **Autonomous Mission Workflow** using Hatchet's Workflow DSL. It orchestrates the complete mission lifecycle from goal decomposition through parallel code execution, security review, and documentation generation — all with durable execution state.

## 2. Workflow Architecture

```mermaid
flowchart LR
    subgraph Parent["AutonomousMissionWorkflow"]
        plan["1. plan()"]
        fanout["2. fan_out_tasks()"]
        review["3. aggregate_and_review()"]
        docs["4. document_mission()"]
    end

    subgraph Children["DevelopTaskWorkflow × N"]
        task1["execute_coding_task(task_1)"]
        task2["execute_coding_task(task_2)"]
        taskN["execute_coding_task(task_N)"]
    end

    plan -->|"task DAG"| fanout
    fanout -->|"aio_run_many"| task1
    fanout -->|"aio_run_many"| task2
    fanout -->|"aio_run_many"| taskN
    task1 -->|"results"| review
    task2 -->|"results"| review
    taskN -->|"results"| review
    review -->|"MissionOutput"| docs
```

## 3. Workflow Steps

### Step 1: `plan()` (L92-L103)
- **Timeout:** 5 minutes
- **Agent:** `PlannerAgent`
- **Action:** Decomposes goal into a task DAG via `plan_mission` MCP tool
- **Output:** `{plan: mission_plan}`

### Step 2: `fan_out_tasks()` (L105-L135)
- **Timeout:** 30 minutes
- **Parent:** `plan`
- **Action:** Spawns parallel `DevelopTaskWorkflow` instances via `aio_run_many`
- **Concurrency:** True parallel fan-out across Hatchet worker pool
- **Output:** `{results: [...]}`

### Step 3: `aggregate_and_review()` (L138-L174)
- **Timeout:** 15 minutes
- **Parent:** `fan_out_tasks`
- **Agents:** `TesterAgent` (run tests), `ReviewerAgent` (security review)
- **Output:** `MissionOutput(status, pull_request_url, summary)`

### Step 4: `document_mission()` (L177-L214)
- **Timeout:** 10 minutes
- **Parent:** `aggregate_and_review`
- **Agent:** `DocumentationAgent`
- **Action:** Generate Mermaid diagrams and documentation
- **Output:** `MissionOutput` with updated summary

## 4. Data Models

```mermaid
classDiagram
    class MissionInput {
        +goal: str
        +repository_path: str
    }
    class TaskInput {
        +task_id: str
        +description: str
        +relevant_files: List~str~
        +constraints: str?
    }
    class MissionOutput {
        +status: str
        +pull_request_url: str
        +summary: str
    }
```
