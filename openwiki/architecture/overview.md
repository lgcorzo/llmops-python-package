# Architecture Overview: `src` Directory

This document provides a comprehensive overview of the codebase structure within the `src/` directory, focusing on the `autogen_team` package.

## 1. System Structure (File Hierarchy)
The following diagram represents the physical layout of the source code. Each folder reflects a specific layer or domain in the application's architecture.

```mermaid
graph TD
    Root[src/] --> AT[autogen_team/]
    
    subgraph Core Logic
    AT --> Core[core/]
    Core --> Schemas[schemas.py]
    Core --> Security[security.py]
    end

    subgraph Application Layer
    AT --> App[application/]
    App --> Agents[agents/ - Coder, Doc, Planner, Reviewer, Tester]
    App --> Workflows[workflows/]
    App --> MCP[mcp/]
    App --> Jobs[jobs/]
    end

    subgraph Data & Infrastructure
    AT --> Models[models/]
    Models --> Entities[entities.py - Base Model Definitions]
    Models --> Repos[repositories.py - Persistence Logic]
    AT --> DataAccess[data__access/]
    AT --> Infra[infrastructure/]
    end

    subgraph Support & Ops
    AT --> Eval[evaluation/]
    AT --> Registry[registry/]
    AT --> Tools[tools/]
    AT --> Scripts[scripts.py]
    AT --> Settings[settings.py]
    end
```

## 2. Model Inheritance (Core Entities)
The system uses a strict inheritance pattern for ML models to ensure consistency when swapping backend providers or model types. The base `Model` class defines the required interface.

```mermaid
classDiagram
    class Model {
        <<Abstract>>
        +String KIND
        +get_params() \nUsage: Extract internal parameters
        +set_params() \nUsage: Update attributes in-place
        +load_context(config) \nUsage: Load assets/weights from disk
        +fit(inputs, targets) \nUsage: Training logic
        +predict(inputs) \nUsage: Inference logic
        +explain_model() \nUsage: Explain internal structure
    }

    note for Model "Abstract class using Pydantic & ABC\nto ensure uniform interface across all models."
```

## 3. Module Deep Dive

### `autogen_team/core/`
Contains the foundational logic used across the entire system.
- **schemas.py**: Defines common data shapes (Inputs, Outputs, etc.).
- **security.py**: Handles authentication and authorization helpers.

### `autogen_team/models/`
Defines the "objects" of the system.
- **entities.py**: Contains the `Model` base class. All specific implementations (e.g., GPT models, Llama models) must inherit from this to ensure compatibility with the `application/` layer.
- **repositories.py**: Defines the abstraction for how models are saved and loaded from storage.

### `autogen_team/application/`
The heart of the system where logic flows into actions.
- **agents/**: Individual agents (Coder, Planner, etc.) that perform specific roles.
- **workflows/**: Orchestration of multiple agent actions.
- **mcp/**: Integration with Model Context Protocol.

### `autogen_team/infrastructure/` & `data_access/`
Handles the "outside world".
- **infrastructure**: Low-level API clients, database drivers, and integration logic.
- **data_access**: High-level data retrieval methods used by the application layer.

## 4. Integration Points
To move from a script to a production agent system:
1.  New features should start in `core/` if they involve new data structures.
2.  New capabilities are implemented as `agents/`.
3.  Persistent storage is handled via the Repository pattern in `models/`.

---
*Last Updated: $(date)*
