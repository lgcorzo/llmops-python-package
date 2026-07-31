---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: autogen_team.application"
source_path: "src/autogen_team/application/"
description: "Application layer managing agent roles, job executions, MCP servers, and workflows."
tags: ["application", "agents", "jobs", "mcp", "workflows"]
last_verified_commit: "main"
timestamp: "2026-07-31T16:40:00Z"
---

# Module Specification: `autogen_team.application`

* **Source File Reference:** `src/autogen_team/application/__init__.py` (Lines: L1-L50)
* **Upstream Dependencies:** [[Modules/Core|autogen_team.core]]
* **Downstream Consumers:** `autogen_team.scripts`

---

## 1. Architectural Role & Responsibilities

Encapsulates application orchestration services:
- `agents`: AutoGen multi-agent roles and prompt definitions.
- `jobs`: Autonomous job runners and execution handlers.
- `mcp`: FastMCP tool wrappers and server endpoints.
- `workflows`: Multi-agent DAG workflow orchestrators.
