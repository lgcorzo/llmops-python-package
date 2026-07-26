---
type: api
title: "generate_mission_docs"
source_path: "src/autogen_team/application/mcp/tools/generate_mission_docs.py"
description: "Generate Mermaid diagrams and documentation for a mission.  Args:     mission_id: Unique identifier for the mission.     mission_context: Context including goal, tasks, results, and file changes.  Returns:     A dict containing generated Mermaid diagrams and documentation."
tags: [api]
last_verified_commit: "dc137c3"
---

# generate_mission_docs

Source File: `src/autogen_team/application/mcp/tools/generate_mission_docs.py`

Generate Mermaid diagrams and documentation for a mission.  Args:     mission_id: Unique identifier for the mission.     mission_context: Context including goal, tasks, results, and file changes.  Returns:     A dict containing generated Mermaid diagrams and documentation.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[MCPService]
    call_0 --> call_1[get_prompt]
    call_1 --> call_2[get_prompt]
    call_2 --> call_3[format]
    call_3 --> call_4[cast]
    call_4 --> call_5[acompletion]
    call_5 --> call_6[loads]
    call_6 --> call_7[get]
    call_7 --> call_8[dumps]
    call_8 --> call_9[dumps]
    call_9 --> call_10[dumps]
    call_10 --> call_11[get]
    call_11 --> call_12[get]
    call_12 --> call_13[get]
    call_13 --> End
```
