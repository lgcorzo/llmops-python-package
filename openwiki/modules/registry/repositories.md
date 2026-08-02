---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Repositories"
source_path: "src/autogen_team/registry/repositories.py"
description: "Exhaustive functional summary for Repositories."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---

# Module Specification: Repositories

* **Source Reference:** `src/autogen_team/registry/repositories.py`

## UML Diagrams

```mermaid
classDiagram
    class RegistryRepository {
        +promote(name: str, version: str, stage: str): None
        +register(name: str, model_uri: str): T.Any
    }
```
