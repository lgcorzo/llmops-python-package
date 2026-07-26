---
type: class
title: "PlannerAgent"
source_path: "src/autogen_team/application/agents/planner_agent.py"
description: "Agent responsible for decomposing a high-level goal into a detailed plan. Uses the MCP 'plan_mission' tool."
tags: [class]
last_verified_commit: "dc137c3"
---

# PlannerAgent

Source File: `src/autogen_team/application/agents/planner_agent.py`

Agent responsible for decomposing a high-level goal into a detailed plan. Uses the MCP 'plan_mission' tool.

## Architecture Visualization

```mermaid
classDiagram
    class PlannerAgent {
        +client
        -__init__()
        +create_plan(goal, repository_path)
    }
```
