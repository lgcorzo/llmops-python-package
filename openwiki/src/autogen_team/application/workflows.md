---
type: "module-architecture"
title: "Workflows Architecture: src/autogen_team/application/workflows"
description: "Technical architecture for multi-agent autonomous mission workflows"
tags: ["architecture", "workflows", "autogen", "mission", "openwiki"]
timestamp: "2026-07-30T00:00:00Z"
---

# Module Name: application/workflows

* **Source Directory Reference:** `src/autogen_team/application/workflows/`
* **Package Dependency:** Upstream: `src/autogen_team/application/agents/`. Downstream: CLI scripts, Hatchet workflows (`src/autogen_team/infrastructure/orchestration/`).

## 1. Executive Summary & Purpose

The `application/workflows` module orchestrates multi-agent interaction loops for complex software engineering missions (`autonomous_mission.py`). It coordinates execution state transitions between `PlannerAgent`, `CoderAgent`, `ReviewerAgent`, `TesterAgent`, and `DocumentationAgent`.

## 2. UML 2.0 Class & Execution Architecture

```mermaid
classDiagram
    direction BT
    class AutonomousMissionWorkflow {
        -planner: PlannerAgent
        -coder: CoderAgent
        -reviewer: ReviewerAgent
        -tester: TesterAgent
        -doc_agent: DocumentationAgent
        +execute_mission(mission_spec: dict) dict
    }

    AutonomousMissionWorkflow --> PlannerAgent : Step 1 - Plan
    AutonomousMissionWorkflow --> CoderAgent : Step 2 - Code Implementation
    AutonomousMissionWorkflow --> ReviewerAgent : Step 3 - Security Review
    AutonomousMissionWorkflow --> TesterAgent : Step 4 - Test Verification
    AutonomousMissionWorkflow --> DocumentationAgent : Step 5 - Doc Generation
```

## 3. Package & Class Relations

* **Workflow Orchestration:** `AutonomousMissionWorkflow` handles sequential and iterative feedback loops. If `ReviewerAgent` or `TesterAgent` reports failures, the mission returns control back to `CoderAgent` for automated patch generation.

## 4. Execution Flow & Runtime Behavior

```mermaid
sequenceDiagram
    autonumber
    participant Client as Application / Trigger
    participant WF as AutonomousMissionWorkflow
    participant Planner as PlannerAgent
    participant Coder as CoderAgent
    participant Reviewer as ReviewerAgent
    participant Tester as TesterAgent

    Client->>WF: execute_mission(spec)
    WF->>Planner: execute_task(spec)
    Planner-->>WF: Plan Created
    loop Execution & Verification Cycle
        WF->>Coder: execute_task(plan_step)
        Coder-->>WF: Code Implemented
        WF->>Reviewer: execute_task(code)
        Reviewer-->>WF: Security Feedback
        WF->>Tester: execute_task(test_suite)
        Tester-->>WF: Test Results (Pass/Fail)
    end
    WF-->>Client: Final Mission Artifacts & Status
```

---

* **Source Citations:**
  * Autonomous Mission Workflow: `src/autogen_team/application/workflows/autonomous_mission.py:1-35`
