---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "hub"
title: "OpenWiki Master Knowledge Hub: autogen_team"
description: "Central navigation hub and ISO 15289 Description artifact for the llmops-python-package (autogen_team) project."
tags: ["index", "iso15289", "openwiki", "okf", "autogen_team", "llmops"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# 🌐 OpenWiki Master Knowledge Hub: `autogen_team`

Welcome to the ISO-compliant **DeepWiki / CodeWiki Architecture Documentation** for the `autogen_team` package (`llmops-python-package`). This system is a **Long-Term Agentic System** serving as the intelligence core for the **Dark Gravity CA/CD Autonomous Agent Factory**, built upon strict **Domain-Driven Design (DDD)** and solid **LLMOps principles**.

This documentation suite is generated strictly under international systems and software engineering standards (**ISO/IEC/IEEE 42010**, **ISO/IEC/IEEE 15289**, **ISO/IEC 25010**, and **ISO/IEC/IEEE 26514**) and formatted using the **Open Knowledge Format (OKF)** standard.

---

## 🏛️ ISO/IEC/IEEE 42010 Architecture Description Framework

The architecture description is organized into standardized architectural viewpoints:

- 📋 [[Architecture/Overview|ISO 42010 Architecture Overview]] — Master Architecture Description (AD) framework, Entity of Interest (EoI), and Stakeholder Concerns matrix.
- 🌐 [[Architecture/SystemContext|System Context View]] — System boundaries, external integrations (Kafka, MLflow, LiteLLM, R2R RAG, Hatchet, MinIO/S3, E2B/Firecracker, OpenZiti).
- 📦 [[Architecture/ComponentStructure|Component & Structural View]] — DDD layer decomposition (`core`, `application`, `infrastructure`) and bounded contexts (`models`, `data_access`, `evaluation`, `registry`) with UML 2.0 diagrams.
- 🔄 [[Architecture/RuntimeSequences|Runtime Sequence View]] — Autonomous Mission lifecycle (Plan → Fan-Out → Review → Document), Kafka prediction flow, MCP tool invocations.
- 🐳 [[Architecture/DeploymentView|Deployment View]] — Docker, docker-compose, Kubernetes (KEDA-scaled OpenCode workers), Poetry packaging.
- 🔐 [[Architecture/SecurityView|Security View]] — `safe_join` path traversal guards, sandbox isolation (E2B/Firecracker), OWASP scanning, environment-variable secret management.
- 📝 [[Architecture/ADR/ADR_001_DDD_Layering|ADR 001: DDD Layering]] — Architecture Decision Record for strict DDD layering with bounded contexts.

---

## 📑 ISO/IEC/IEEE 15289 Specifications & Reports

- 📜 [[Specifications/SRSRequirements|Software Requirements Specification (SRS)]] — Functional and non-functional requirements across DDD layers and bounded contexts.
- 🔌 [[Specifications/APIContracts|API & Interface Contracts]] — MCP tool schemas, Kafka message formats, FastAPI endpoints, Pydantic model contracts, abstract class interfaces.
- 📊 [[Quality/ISO25010Quality|ISO 25010 Quality Model Matrix]] — Quality attribute evaluation (Functional Suitability, Security, Maintainability, Performance, Portability).
- 🛠️ [[UserGuides/DeveloperGuide|Developer & System User Guide]] — ISO 26514 guide for installation, development workflow, MCP server, Kafka deployment.
- 🪵 [[Logs|Audit Log & Git History]] — ISO 15289 audit log tracking commit SHAs, AST graph metrics, and documentation revisions.

---

## 🧱 Granular OKF Module Specifications (1:1 Mirrored)

Explore individual module specifications with exact line-level source code citations:

### ⚙️ `core/` — Shared Kernel
- [[Modules/Core/Schemas|core::schemas]] — Pandera `DataFrameModel` hierarchy: `Schema`, `InputsSchema`, `OutputsSchema`, `TargetsSchema`, `SHAPValuesSchema`, `FeatureImportancesSchema` (`src/autogen_team/core/schemas.py:L1-L114`).
- [[Modules/Core/Security|core::security]] — `safe_join` path traversal guard utility (`src/autogen_team/core/security.py:L1-L27`).

### 🤖 `application/` — Application Layer
- [[Modules/Application/Agents|application::agents]] — Autonomous agents: `CoderAgent`, `PlannerAgent`, `ReviewerAgent`, `TesterAgent`, `DocumentationAgent` (`src/autogen_team/application/agents/`).
- [[Modules/Application/Workflows|application::workflows]] — `AutonomousMissionWorkflow` Hatchet DSL with Plan → Fan-Out → Review → Document steps (`src/autogen_team/application/workflows/autonomous_mission.py:L1-L214`).
- [[Modules/Application/MCPTools|application::mcp_tools]] — MCP Server tools: `plan_mission`, `execute_code`, `run_tests`, `security_review`, `retrieve_context`, `index_code`, `generate_mission_docs` (`src/autogen_team/application/mcp/tools/`).
- [[Modules/Application/Jobs|application::jobs]] — Legacy batch jobs: `TrainingJob`, `EvaluationsJob`, `InferenceJob`, `TuningJob`, `PromotionJob`, `ExplanationsJob`, `HatchetInferenceJob` (`src/autogen_team/application/jobs/`).

### 🔌 `infrastructure/` — Infrastructure Layer
- [[Modules/Infrastructure/Services|infrastructure::services]] — `Service` (base), `LoggerService`, `MCPService`, `MlflowService`, `HatchetService`, `AlertsService`, `SandboxService` (`src/autogen_team/infrastructure/services/`).
- [[Modules/Infrastructure/Messaging|infrastructure::messaging]] — `FastAPIKafkaService` real-time prediction pipeline, `A2A Protocol` Pydantic message schemas (`src/autogen_team/infrastructure/messaging/`).
- [[Modules/Infrastructure/IO|infrastructure::io]] — OmegaConf config parsing (`configs.py`), `Env` Pydantic Settings singleton (`osvariables.py`) (`src/autogen_team/infrastructure/io/`).
- [[Modules/Infrastructure/Utils|infrastructure::utils]] — `GridCVSearcher`, `InferSigner`, `TrainTestSplitter`, `TimeSeriesSplitter` (`src/autogen_team/infrastructure/utils/`).

### 🧠 `models/` — Bounded Context
- [[Modules/Models/Entities|models::entities]] — `Model` (abstract), `BaselineAutogenModel` (OpenAI group chat), `DummyModel` (`src/autogen_team/models/entities.py:L1-L413`).

### 💾 `data_access/` — Bounded Context
- [[Modules/DataAccess/Datasets|data_access::datasets]] — `Reader`/`Writer` abstract hierarchy, `ParquetReader`, `ParquetWriter`, `DatasetDescriptor`, `DatasetRepository` (`src/autogen_team/data_access/`).

### 📊 `evaluation/` — Bounded Context
- [[Modules/Evaluation/Metrics|evaluation::metrics]] — `Metric`/`AutogenMetric`/`AutogenConversationMetric`, `Threshold`, MLflow integration (`src/autogen_team/evaluation/metrics/metrics.py:L1-L216`).

### 🗄️ `registry/` — Bounded Context
- [[Modules/Registry/MlflowAdapter|registry::mlflow_adapter]] — `Saver`/`CustomSaver`, `Loader`/`CustomLoader`, `Register`/`MlflowRegister` with PyFunc adapter pattern (`src/autogen_team/registry/adapters/mlflow_adapter.py:L1-L341`).
