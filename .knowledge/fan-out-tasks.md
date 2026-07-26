---
type: api
title: "fan_out_tasks"
source_path: "src/autogen_team/application/workflows/autonomous_mission.py"
description: "Step 2: Spawn parallel child workflows for each coding task.  Uses ``develop_task_workflow.aio_run_many`` for true parallel fan-out execution across the Hatchet worker pool."
tags: [api]
last_verified_commit: "dc137c3"
---

# fan_out_tasks

Source File: `src/autogen_team/application/workflows/autonomous_mission.py`

Step 2: Spawn parallel child workflows for each coding task.  Uses ``develop_task_workflow.aio_run_many`` for true parallel fan-out execution across the Hatchet worker pool.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[task]
    call_0 --> call_1[log]
    call_1 --> call_2[task_output]
    call_2 --> call_3[create_bulk_run_item]
    call_3 --> call_4[aio_run_many]
    call_4 --> call_5[len]
    call_5 --> call_6[TaskInput]
    call_6 --> call_7[get]
    call_7 --> call_8[get]
    call_8 --> call_9[get]
    call_9 --> End
```
