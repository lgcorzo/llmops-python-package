---
type: "quickstart-guide"
title: "OpenWiki Quickstart & Repository Overview"
description: "Quickstart developer guide for navigating and maintaining OpenWiki architectural documentation."
tags: ["openwiki", "quickstart", "guide", "llmops"]
timestamp: "2026-07-30T00:00:00Z"
---

# OpenWiki Quickstart Guide

This document provides a quick overview of how to navigate, run, and maintain the OpenWiki technical architecture documentation for `llmops-python-package`.

---

## 🎯 Purpose & Scope

The OpenWiki directory `./openwiki` serves as the living technical documentation for `llmops-python-package`. It maps out the object-oriented class hierarchies, design patterns, dependencies, and execution flows using UML 2.0 Mermaid diagrams derived from AST parsing (`pyreverse`, `graphify`).

---

## 🧭 Key Documentation Sections

1. **[Master Index](index.md):** The primary table of contents linking to every module document.
2. **[Changelog & System Logs](logs.md):** Complete audit trail of wiki generation and updates.
3. **Core & Architecture Modules:**
   - [Core Schemas & Security](src/autogen_team/core.md)
   - [Agents Module](src/autogen_team/application/agents.md)
   - [Jobs Execution Framework](src/autogen_team/application/jobs.md)
   - [MCP Tools Interface](src/autogen_team/application/mcp.md)
   - [ML Models Module](src/autogen_team/models.md)
   - [Data Access Layer](src/autogen_team/data_access.md)
   - [Registry & MLflow Integration](src/autogen_team/registry.md)
   - [Infrastructure Services](src/autogen_team/infrastructure/services.md)

---

## 🛠 Maintenance & Regeneration

The documentation in `openwiki` follows strict rules:
* **Relative Paths Only:** All citations and markdown links use repository-relative paths (`src/autogen_team/...` or `openwiki/...`). Absolute paths are explicitly banned.
* **AST Fidelity:** Do not edit class signatures or diagram connections manually without verifying against actual source code AST output (`pyreverse`).
* **OKF Standard:** Every document contains standard YAML frontmatter metadata.

To regenerate or verify the wiki diagrams locally:
```bash
# Extract AST dot files using pyreverse
pyreverse -o dot -p autogen_team src/autogen_team
```
