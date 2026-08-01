# Application Layer: Workflows

The project uses the Hatchet Workflow DSL to manage complex, stateful orchestrations for autonomous agents. This layer ensures that even if a long-running mission (like building a whole feature) hits an error or needs more time, it can be resumed or retried successfully.

## Core Workflows

### 1. Autonomous Mission Workflow
**Source**: `src/autogen_team/application/workflows/autonomous_mission.py`

This is the primary high-level orchestrator for autonomous development missions. It implements a "Plan -> Fan-Out -> Review" pattern:

*   **Planning Phase**: A Planner agent analyzes the goal and creates a sequence of tasks.
*   **Fan-Out Execution**: The `aio_run_many` logic (leveraging Hatchet's ability to handle parallel child workflows) allows multiple Coder agents to work on different parts of the codebase simultaneously.
*   **Review Phase**: A Reviewer agent inspects all changes before concluding the mission.

## Implementation Details
- **Durability**: Every state change is managed by Hatchet, ensuring that complex multi-step tasks are not lost if a worker crashes.
- **Data Models**: Uses Pydantic models (e.g., `MissionInput`, `TaskInput`) to strictly validate input data at every transition point between agents and workflows.

## Key Components
- **HatchetService**: The primary bridge to the Hatchet API for orchestration.
- **Task DAGs**: The internal representation of what needs to be done during a mission.

---
See also:
- [Agent Roles](/application/agents.md)
- [MCP Tools](/application/mcp_tools.md)
- [Quickstart](/quickstart.md)
