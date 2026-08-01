# Operations & Runbook

This page provides practical guidance for setting up, running, and developing on the Autogen Team platform locally.

## Local Development Setup

### Prerequisites
- Python 3.10+
- Poetry (>= 1.8.2)

### Initial Setup
1.  **Install Dependencies**:
    ```bash
    poetry install
    ```
2.  **Configuration**: Update the configuration files located in `confs/` to reflect your local environment for Kafka, Hatchet, and other services.

## Running the System

### 1. Start the MCP Server
The Model Context Protocol (MCP) server provides the tools that agents use to interact with the world. To start it locally:
```bash
poetry run invoke projects.mcp
# Or with specific prompt configurations:
poetry run invoke projects.mcp --prompts=confs/mcp_prompts.yaml
```

### 2. Executing Workflows
Workflows can be triggered via the CLI or through internal system interactions (e.g., from a web front-end or other agents).
- To run manually, you can often use entry points defined in `pyproject.toml` or by calling scripts directly within the `src/autogen_team/application/workflows/` directory.

## Common Tasks & Troubleshooting
- **Database Issues**: If connectivity to your local database (for R2R or standard metadata) fails, check the credentials in your local environment variables and the configuration in `confs/`.
- **Kafka Messaging**: Ensure your local Kafka broker is running if you are trying to run multi-agent workflows involving distributed workers.
- **Port Conflicts**: The MCP server typically runs on a specific port; ensure it isn't occupied by other services like `.py` servers or standard web projects.

## Development Workflow
1.  **Feature Branch**: Create a new branch from `main`.
2.  **Test Changes**: Run existing tests to ensure no regressions in core logic:
    ```bash
    poetry run pytest
    ```
3.  **Validate Documentation**: Use the provided tools (if applicable) or manual review to ensure that documentation updates align with code changes.

---
See also:
- [Quickstart](/quickstart.md)
- [Architecture Overview](/architecture/overview.md)
