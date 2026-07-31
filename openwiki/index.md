---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "hub"
title: "OpenWiki Master Knowledge Hub: llmops-python-package"
description: "Central navigation hub and ISO 15289 Description artifact for the llmops-python-package codebase."
tags: ["index", "iso15289", "openwiki", "okf", "llmops"]
timestamp: "2026-07-31T16:40:00Z"
---

# 🌐 OpenWiki Master Knowledge Hub: `llmops-python-package`

Welcome to the ISO-compliant **DeepWiki / CodeWiki Architecture Documentation** for the `llmops-python-package` ecosystem. This project provides an enterprise LLMOps and multi-agent workflow framework in Python (`src/autogen_team`), integrating Pandera dataframe schema validation, Pydantic settings, model registry adapters, evaluation metrics, FastMCP server drivers, and MLflow/Ray orchestration.

This documentation suite is generated strictly under international systems and software engineering standards (**ISO/IEC/IEEE 42010**, **ISO/IEC/IEEE 15289**, **ISO/IEC 25010**, and **ISO/IEC/IEEE 26514**) and formatted using the **Open Knowledge Format (OKF)** standard.

---

## 🏛️ ISO/IEC/IEEE 42010 Architecture Description Framework

- 📋 [[Architecture/Overview|ISO 42010 Architecture Overview]] — Master Architecture Description (AD) framework, Entity of Interest (EoI), and Stakeholder Concerns matrix.
- 🌐 [[Architecture/SystemContext|System Context View]] — System boundaries, external integrations (OpenAI/Ollama, MLflow, FastMCP, Ray, Hydra, Airflow).
- 📦 [[Architecture/ComponentStructure|Component & Structural View]] — Package structure breakdown (`core`, `application`, `infrastructure`, `data_access`, `evaluation`, `models`, `registry`) and UML 2.0 Class Diagrams.
- 🔄 [[Architecture/RuntimeSequences|Runtime Sequence View]] — Dynamic interaction flows for job execution, workflow orchestration, model evaluation, and FastMCP tool dispatches.
- 🐳 [[Architecture/DeploymentView|Deployment View]] — Docker containerization, Poetry environment configuration, MLflow tracking server, and CLI commands.
- 🔐 [[Architecture/SecurityView|Security View]] — Secret management, Pandera strict dataframe coercion, Pydantic validation bounds, and input sanitization.
- 📝 [[Architecture/ADR/ADR_001_AST_Engine|ADR 001: Local AST Engine]] — Architecture Decision Record for local AST parsing without external LLM embedding server dependencies.

---

## 📑 ISO/IEC/IEEE 15289 Specifications & Reports

- 📜 [[Specifications/SRSRequirements|Software Requirements Specification (SRS)]] — Functional and non-functional requirements traceable across Python modules.
- 🔌 [[Specifications/APIContracts|API & Interface Contracts]] — Python class contracts, Pandera schemas (`InputsSchema`, `OutputsSchema`), Pydantic settings, and CLI entry points.
- 📊 [[Quality/ISO25010Quality|ISO 25010 Quality Model Matrix]] — Evaluation of software quality attributes (Functional Suitability, Performance Efficiency, Maintainability, Reliability).
- 🛠️ [[UserGuides/DeveloperGuide|Developer & System User Guide]] — ISO 26514 guide for installation via Poetry, test execution (`pytest`), linting (`ruff`/`mypy`), and job configurations.
- 🪵 [[Logs|Audit Log & Git History]] — ISO 15289 audit log tracking commit SHAs, AST graph metrics, and documentation revisions.

---

## 🧱 Granular OKF Module Specifications (1:1 Mirrored)

- [[Modules/Core|autogen_team::core]] — Schema definitions (`InputsSchema`, `OutputsSchema`, `SHAPValuesSchema`, `FeatureImportancesSchema`) & security validators (`src/autogen_team/core/schemas.py:L1-L114`).
- [[Modules/Application|autogen_team::application]] — Application agent roles, job kinds, MCP handlers, and workflow orchestrators (`src/autogen_team/application/__init__.py:L1-L50`).
- [[Modules/Infrastructure|autogen_team::infrastructure]] — Client abstractions, IO adapters, messaging layers, and orchestration wrappers (`src/autogen_team/infrastructure/__init__.py:L1-L50`).
- [[Modules/DataAccess|autogen_team::data_access]] — Data access entities, repositories, and data adapters (`src/autogen_team/data_access/entities.py:L1-L60`).
- [[Modules/Evaluation|autogen_team::evaluation]] — Model evaluation metrics, entities, and evaluation services (`src/autogen_team/evaluation/entities.py:L1-L60`).
- [[Modules/Models|autogen_team::models]] — Model domain entities and repository implementations (`src/autogen_team/models/entities.py:L1-L60`).
- [[Modules/Registry|autogen_team::registry]] — Model registry adapters and entity management (`src/autogen_team/registry/entities.py:L1-L60`).
