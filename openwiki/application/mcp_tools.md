# Application Layer: Model Context Protocol (MCP)

The **Model Context Protocol (MCP)** provides a standardized interface for LLMs to interact with external systems and tools. In Autogen Team, MCP serves as the standard "capabilities" layer for agents.

## Core Tools
The system implements several critical tool categories via the MCP server (`src/autogen_team/application/mcp/`):

### 1. Reasoning & Planning Tools
- **plan_mission**: Enables a Planner Agent to decompose high-level goals into actionable tasks within a Hatchet workflow.
- **generate_mission_docs**: Automates the creation of documentation based on changes made during a mission.

### 2. Development Tools
- **execute_code**: Allows the Coder agent to run scripts, tests, or commands in an isolated environment.
- **run_tests**: Specialized tool for verifying that specific code changes don't break existing functionality.

### 3. Knowledge & Context Tools
- **retrieve_context**: Uses R2R and potentially other retrieval methods to pull relevant codebase information into the context window.
- **index_code**: Updates the local knowledge base (e.g., vector index) with recently modified files.

## Integration Logic
MCP tools are exposed through an API that agents can call directly. By using a standardized protocol, it is easy to swap out the underlying implementation (e.g., changing how `execute_code` manages sandboxes) without rewriting the agent logic.

---
See also:
- [Agent Roles](/application/agents.md)
- [Workflows Overview](/application/workflows.md)
- [Quickstart](/quickstart.md)
