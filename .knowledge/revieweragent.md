---
type: class
title: "ReviewerAgent"
source_path: "src/autogen_team/application/agents/reviewer_agent.py"
description: "Agent responsible for reviewing code changes. Uses the MCP 'security_review' tool."
tags: [class]
last_verified_commit: "dc137c3"
---

# ReviewerAgent

Source File: `src/autogen_team/application/agents/reviewer_agent.py`

Agent responsible for reviewing code changes. Uses the MCP 'security_review' tool.

## Architecture Visualization

```mermaid
classDiagram
    class ReviewerAgent {
        +client
        -__init__()
        +review_changes(mission_id, file_changes)
    }
```
