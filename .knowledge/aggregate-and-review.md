---
type: api
title: "aggregate_and_review"
source_path: "src/autogen_team/application/workflows/autonomous_mission.py"
description: "Step 3: Aggregate child results, run tests, and perform security review."
tags: [api]
last_verified_commit: "dc137c3"
---

# aggregate_and_review

Source File: `src/autogen_team/application/workflows/autonomous_mission.py`

Step 3: Aggregate child results, run tests, and perform security review.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[task]
    call_0 --> call_1[task_output]
    call_1 --> call_2[log]
    call_2 --> call_3[TesterAgent]
    call_3 --> call_4[ReviewerAgent]
    call_4 --> call_5[MissionOutput]
    call_5 --> call_6[run_tests]
    call_6 --> call_7[extend]
    call_7 --> call_8[review_changes]
    call_8 --> call_9[get]
    call_9 --> call_10[get]
    call_10 --> call_11[join]
    call_11 --> call_12[get]
    call_12 --> End
```
