---
type: "module-architecture"
title: "Infrastructure Client Architecture: src/autogen_team/infrastructure/client"
description: "Technical specification for Model Context Protocol (MCP) client communication"
tags: ["architecture", "infrastructure", "mcp_client", "rpc", "openwiki"]
timestamp: "2026-07-30T00:00:00Z"
---

# Module Name: infrastructure/client

* **Source Reference:** `src/autogen_team/infrastructure/client/mcp_client.py`
* **Package Dependency:** Upstream: `asyncio`, `httpx` / `mcp_sdk`. Downstream: `src/autogen_team/application/agents/`.

## 1. Executive Summary & Purpose

The `infrastructure/client` module houses the `MCPClient` class, providing an asynchronous client interface to connect to Model Context Protocol (MCP) servers, inspect tool availability, and execute remote tool calls over JSON-RPC.

## 2. UML 2.0 Class & Client Architecture (Deterministic)

```mermaid
classDiagram
    direction BT
    class MCPClient {
        -server_url: str
        -session: Any
        +connect() None
        +disconnect() None
        +call_tool(tool_name: str, arguments: dict) dict
        +list_tools() list
    }
```

## 3. Package & Class Relations

* **Agent Client Binding:** Instantiated by `CoderAgent`, `PlannerAgent`, `ReviewerAgent`, `TesterAgent`, and `DocumentationAgent` to invoke remote MCP tools asynchronously (`connect`, `call_tool`, `disconnect`).

## 4. Execution Flow & Runtime Behavior

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Application Agent
    participant Client as MCPClient
    participant Server as Remote MCP Server Endpoint

    Agent->>Client: connect()
    Client->>Server: Initialize RPC Transport Session
    Server-->>Client: Session Active
    Agent->>Client: call_tool("execute_code", {"code": "print('hello')"})
    Client->>Server: Send RPC Request {method: "tools/call", params: ...}
    Server-->>Client: Send RPC Response {result: ...}
    Client-->>Agent: Parsed Result Dictionary
    Agent->>Client: disconnect()
    Client->>Server: Close RPC Session
```

---

* **Source Citations:**
  * MCP Client Implementation: `src/autogen_team/infrastructure/client/mcp_client.py:1-40`
