---
iso_doc_type: "Description"
iso_viewpoint: "DeploymentView"
type: "architecture"
title: "ISO 42010 Deployment View: Package Topologies & Containerization"
description: "Deployment View outlining Poetry packaging, Docker build stages, MLflow server connections, and CLI tools."
tags: ["iso42010", "deployment_view", "poetry", "docker", "mlflow"]
timestamp: "2026-07-31T16:40:00Z"
---

# ISO 42010 Deployment View: Package Topologies & Containerization

## 1. Poetry Packaging & Environment Topology

The `llmops-python-package` is managed via **Poetry** (`pyproject.toml`):

```mermaid
graph TB
    subgraph Host_Environment["Local Host / Kubernetes Cluster"]
        VENV[".venv Virtualenv (Python 3.12)"]
        CLI_BIN["autogen_team CLI Command"]
    end

    subgraph External_Services["MLOps Infrastructure"]
        MLFLOW_SVR["MLflow Server (:5000)"]
        FASTMCP_SVR["FastMCP Gateway Gateway"]
    end

    VENV --> CLI_BIN
    CLI_BIN <--> MLFLOW_SVR
    CLI_BIN <--> FASTMCP_SVR
```

---

## 2. Docker & Multi-Stage Deployment

- **`Dockerfile`**: Builds lightweight production wheels (`poetry build`) and installs runtime dependencies.
- **`docker-compose.yml`**: Provisions local development infrastructure (MLflow server, FastMCP gateway, local storage volumes).
