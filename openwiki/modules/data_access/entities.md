---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "module"
title: "Entities"
source_path: "src/autogen_team/data_access/entities.py"
description: "Exhaustive functional summary for Entities."
tags: ["core", "okf"]
timestamp: "2026-08-02T05:30:56.472172Z"
generated: "agent:okf-professional-documenter"
verified: "true"
last_verified_commit: "e2acd53"
---
# Module Specification: Entities

* **Source Reference:** `src/autogen_team/data_access/entities.py`

## Overview
This module provides data access functionality for Entities.

## UML Diagrams

```mermaid
classDiagram
    class DatasetDescriptor {
        +Optional[list[str]] columns
        +str format
        +str name
        +str path
    }
```
