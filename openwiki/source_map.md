---
iso_doc_type: "Specification"
iso_viewpoint: "ArchitectureDescription"
type: "mapping"
title: "Source Map"
source_path: "src/autogen_team/"
description: "Mapping of wiki pages to source code files."
tags: ["navigation", "mapping"]
timestamp: "2024-05-22T12:00:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: ""
---

This page maps the high-level features and architecture described in the wiki to their corresponding locations in the source code.

## Core Architecture
| Feature | Source Path | Description |
| :--- | :--- | :--- |
| **Project Entrypoint** | `src/autogen_team/__main__.py` | Main entry point for the application. |
| **Configuration Management** | `src/autogen_team/settings.py` | Centralized configuration and environment loading. |
| **Core Logic & Shared Data** | `src/autogen_team/core/`, `src/autogen_team/models/` | Core domain entities, shared schemas, and business rules. |

## Application Layer
| Feature | Source Path | Description |
| :--- | :--- | :--- |
| **Agent Implementations** | `src/autogen_team/application/agents/` | The primary agents (Planner, Coder, Tester, Reviewer). |
| **Workflow Definitions** | `src/autogen_team/application/workflows/` | Hatchet-based workflows for multi-agent collaboration. |
| **MCP Tools** | `src/autogen_team/application/mcp/tools/` | Implementation of Model Context Protocol tools. |

## Infrastructure Layer
| Feature | Source Path | Description |
| :--- | :--- | :--- |
| **Kafka & A2A Messaging** | `src/autogen_team/infrastructure/messaging/` | Kafka producers, consumers, and communication protocols. |
| **External Service Clients** | `src/autogen_team/infrastructure/services/` | Client wrappers for Hatchet, etc. |
| **Connectivity Logic** | `src/autogen_team/infrastructure/client/` | Network-level connectivity and low-level clients. |

## Supporting Tools
| Feature | Source Path | Description |
| :--- | :--- | :--- |
| **Scripting & Utilities** | `src/autogen_team/scripts.py`, `src/autogen_team/infrastructure/utils/` | Internal scripts and common helper functions. |
| **Tools Integration** | `src/autogen_team/tools/` | Generic utility tools. |

---
See also:
- [Quickstart](/quickstart.md)
- [Architecture Overview](/architecture/overview.md)
