# Application Layer: Agents & Roles

The Autogen Team framework defines several specialized agents, each with a specific responsibility within an autonomous mission. These roles are designed to work in tandem, often orchestrated by the Hatchet workflow engine.

## Core Agent Roles

### 1. Planner Agent
- **Source**: `src/autogen_team/application/agents/planner_agent.py`
- **Role**: The architect of the mission. It takes a high-level goal and breaks it down into a granular Task DAG (Directed Acyclic Graph).
- **Capabilities**: Contextual awareness, task decomposition, dependency mapping.

### 2. Coder Agent
- **Source**: `src/autogen_team/application/agents/coder_agent.py`
- **Role**: The executor of technical changes. It operates on specific file contents to implement functionality or bug fixes.
- **Capabilities**: Code generation, refactoring, tool usage via MCP.

### 3. Tester Agent
- **Source**: `src/autogen_team/application/agents/tester_agent.py`
- **Role**: The quality gatekeeper. It validates that the changes implemented by the Coder agent pass all relevant tests.
- **Capabilities**: Test suite execution, failure analysis, verification loop.

### 4. Reviewer Agent
- **Source**: `src/autogen_team/application/agents/reviewer_agent.py`
- **Role**: The gatekeeper for security and quality. It performs static analysis and RAG-backed security reviews.
- **Capabilities**: Security scanning (OWASP), compliance checking, peer review logic.

### 5. Documentation Agent
- **Source**: `src/autogen_team/application/agents/documentation_agent.py`
- **Role**: Responsible for generating clear and accurate documentation for the modified modules.
- **Capabilities**: Technical writing, docstring generation, overview synthesis.

## Integration with Workflows
Agents are typically instantiated within the application layer and injected into Hatchet tasks to provide specialized reasoning during autonomous missions.

---
See also:
- [Workflows Overview](/application/workflows.md)
- [MCP Tools](#)
- [Quickstart](/quickstart.md)
