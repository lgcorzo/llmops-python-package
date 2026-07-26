---
type: class
title: "DocumentationAgent"
source_path: "src/autogen_team/application/agents/documentation_agent.py"
description: "Agent responsible for generating mission documentation and diagrams. Uses the MCP 'generate_mission_docs' tool."
tags: [class]
last_verified_commit: "dc137c3"
---

# DocumentationAgent

Source File: `src/autogen_team/application/agents/documentation_agent.py`

Agent responsible for generating mission documentation and diagrams. Uses the MCP 'generate_mission_docs' tool.

## Architecture Visualization

```mermaid
classDiagram
    class DocumentationAgent {
        +client
        -__init__()
        +generate_docs(mission_id, mission_context)
    }
```
