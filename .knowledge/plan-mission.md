---
type: api
title: "plan_mission"
source_path: "src/autogen_team/application/mcp/tools/plan_mission.py"
description: "Decompose a high-level goal into a task DAG.  Args:     goal: A high-level goal string to decompose.  Returns:     A dict representing the task DAG with parallel_tasks array."
tags: [api]
last_verified_commit: "dc137c3"
---

# plan_mission

Source File: `src/autogen_team/application/mcp/tools/plan_mission.py`

Decompose a high-level goal into a task DAG.  Args:     goal: A high-level goal string to decompose.  Returns:     A dict representing the task DAG with parallel_tasks array.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[MCPService]
    call_0 --> call_1[get_prompt]
    call_1 --> call_2[cast]
    call_2 --> call_3[acompletion]
    call_3 --> call_4[loads]
    call_4 --> call_5[strip]
    call_5 --> End
```
