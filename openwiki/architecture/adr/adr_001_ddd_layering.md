---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDecision"
type: "adr"
title: "ADR 001: Strict DDD Layering with Bounded Contexts"
description: "Decision record documenting the choice of strict Domain-Driven Design layering with bounded contexts for autonomous agent orchestration."
tags: ["adr", "iso42010", "ddd", "architecture", "decision"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Architecture Decision Record (ADR 001)

## 1. Status

**ACCEPTED** (Date: 2026-08-01)

## 2. Context & Stakeholder Concern

* **Addressed Concern:** The system must support both autonomous multi-agent orchestration (Hatchet workflows, MCP tools) and legacy MLOps batch pipelines (training, evaluation, inference) within a single codebase, while maintaining long-term maintainability and clear separation of concerns.
* **Framing Viewpoint:** Component View & Maintainability.
* **Stakeholders:** System Architect, Lead Developer, ML Engineer.

## 3. Decision

Adopt strict **Domain-Driven Design (DDD)** with the following architectural layers and bounded contexts:

### Layers (Dependency Direction: Inward Only)
1. **Core Layer** (`core/`): Shared kernel — schemas, security utilities. No external dependencies.
2. **Application Layer** (`application/`): Use-case orchestration — agents, workflows, MCP tools, jobs. Depends on Core and Bounded Contexts.
3. **Infrastructure Layer** (`infrastructure/`): External world connections — services, messaging, config parsing. Depends on Core only.

### Bounded Contexts (Independent Domains)
- **Models** (`models/`): ML model entities and repository
- **Data Access** (`data_access/`): Dataset reading, writing, and lineage
- **Evaluation** (`evaluation/`): Metrics, thresholds, and model validation
- **Registry** (`registry/`): Model serialization, deserialization, and registration via MLflow

Each bounded context owns its own entities, adapters, and repositories using the **Repository** and **Adapter** patterns.

## 4. Rationale & Alternatives Evaluated

| Alternative Evaluated | Trade-Off / Failure Mode | Evaluation Result |
| :--- | :--- | :--- |
| **Monolithic flat package** | No separation of concerns; agents and infrastructure code interleaved; impossible to test in isolation | Rejected |
| **Microservices per agent** | Excessive operational complexity for a package-level library; cross-service transactions for missions | Rejected |
| **Hexagonal Architecture (Ports & Adapters)** | Good fit but overkill for bounded contexts that share a common core schema; DDD provides clearer domain boundaries | Considered but DDD selected |
| **Strict DDD with Bounded Contexts** | Clear layer boundaries enforce dependency inversion; each context independently evolvable; jobs and agents coexist cleanly | **Selected** |

## 5. Consequences

### Positive
- **Testability:** Each layer and bounded context can be tested in isolation with mocks at boundaries.
- **Extensibility:** New agents, tools, or jobs can be added to the Application layer without modifying Core or Infrastructure.
- **Swappability:** Infrastructure services (e.g., switching from E2B to local Firecracker) require changes only in `infrastructure/services/`.
- **Clarity:** New contributors can navigate the codebase via layer boundaries.

### Negative
- **Initial complexity:** More packages and files than a flat structure.
- **Cross-context coordination:** Some jobs (e.g., `TrainingJob`) need entities from multiple bounded contexts, requiring careful import management.

## 6. Affected System Artifacts

- `src/autogen_team/core/` — Shared kernel (schemas, security)
- `src/autogen_team/application/` — Agents, workflows, MCP tools, jobs
- `src/autogen_team/infrastructure/` — Services, messaging, IO, utils
- `src/autogen_team/models/` — Models bounded context
- `src/autogen_team/data_access/` — Data access bounded context
- `src/autogen_team/evaluation/` — Evaluation bounded context
- `src/autogen_team/registry/` — Registry bounded context
- Links to [[Architecture/ComponentStructure]]
