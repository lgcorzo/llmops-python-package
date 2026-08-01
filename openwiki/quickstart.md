---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "index"
title: "Quickstart"
source_path: "src/autogen_team/"
description: "A high-level entry point and overview of the Autogen Team project."
tags: ["onboarding", "overview", "core"]
timestamp: "2024-05-22T12:00:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: ""
---

## Overview
Autogen Team is a robust **Long-Term Agentic System** designed as the intelligence core for autonomous workflows. It provides a standardized framework to move from simple LLM calls to complex, multi-step agentic operations involving code execution, testing, and automated deployment.

The system is built on:
1.  **Domain-Driven Design (DDD)**: Ensuring strict separation between domain logic, application orchestration, and infrastructure.
2.  **LLMOps Best Practices**: Supporting advanced features like asynchronous inference, RAG context management via **R2R**, and integrated evaluation pipelines.
3.  **Model Context Protocol (MCP)**: Standardizing how agents interact with external tools (e.g., file systems, compilers, web search).

## Key Architecture Pillars

### 1. Domain-Driven Design (DDD) Layering
The project structure strictly follows a layered approach to manage complexity:
- **Core**: The "kernel" of the application. Contains pure business logic (models), common schemas, and core security protocols independent of external technologies.
- **Application**: The orchestration layer. This is where autonomous workflows are defined, agents are instantiated with specific roles, and MCP tools are integrated into the service flow.
- **Infrastructure**: The outer edge. Handles all "real world" integrations including Kafka messaging, Hatchet API communication, and OpenZiti secured networking.

### 2. Agentic Workflows & Orchestration
The system utilizes a sophisticated state-management layer to drive multi-step missions:
- **Hatchet Integration**: Used for durable workflow execution. It handles "fan-out" operations where multiple tasks (e.g., coding different modules) can run in parallel with consistent retry logic and state persistence.
- **Automated Missions**: The primary use case is the `AutonomousMissionWorkflow`, which takes a raw requirement and orchestrates a multi-agent team to produce production-ready code via:
    - **Planner Agent**: Analyzes goals and generates task DAGs.
    - **Coder Agent**: Implements changes in isolated environments.
    - **Tester Agent**: Validates changes through automated test suites.
    - **Reviewer Agent**: Performs security scans and quality audits.

### 3. Infrastructure & Security
To ensure reliability in distributed agentic systems:
- **Messaging**: Kafka-based A2A (Agent-to-Agent) communication for asynchronous scaling.
- **Zero Trust Networking**: Integration with OpenZiti to secure all cross-agent communications.
- **Sandboxing**: Secure execution of untrusted code using micro-VM technologies or isolated containers.

## Quick Links
- [Architecture & DDD Overview](/architecture/overview.md)
- [Agent Definitions](/application/agents.md)
- [Workflow Orchestration](/application/workflows.md)
- [MCP Tools & Integrations](/application/mcp_tools.md)
- [Infrastructure Components](/infrastructure/overview.md)
- [Development & Runbook](/operations/runbook.md)

## Getting Started
To explore the codebase or contribute, begin with:
1.  **Architecture Overview**: Read `/architecture/overview.md` to understand how core modules interact.
2.  **Running Locally**: See `/operations/runbook.md` for steps to launch the MCP server and local workflows.
3.  **Source Map**: Consult `source_map.md` to see which files correspond to specific high-level features.

## Roadmap & Backlog
- [ ] Expand documentation on R2R integration details.
- [ ] Document specific Kafka consumer/producer configurations in detail.
