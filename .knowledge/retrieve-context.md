---
type: api
title: "retrieve_context"
source_path: "src/autogen_team/application/mcp/tools/retrieve_context.py"
description: "Query R2R RAG system for relevant codebase patterns via semantic search.  Args:     query: Search query string.     collection_name: Name of the R2R collection to search.  Returns:     Dict with matching documents and graph context."
tags: [api]
last_verified_commit: "dc137c3"
---

# retrieve_context

Source File: `src/autogen_team/application/mcp/tools/retrieve_context.py`

Query R2R RAG system for relevant codebase patterns via semantic search.  Args:     query: Search query string.     collection_name: Name of the R2R collection to search.  Returns:     Dict with matching documents and graph context.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[Env]
    call_0 --> call_1[get]
    call_1 --> call_2[get]
    call_2 --> call_3[get]
    call_3 --> call_4[strip]
    call_4 --> call_5[AsyncClient]
    call_5 --> call_6[raise_for_status]
    call_6 --> call_7[json]
    call_7 --> call_8[error]
    call_8 --> call_9[error]
    call_9 --> call_10[get]
    call_10 --> call_11[get]
    call_11 --> call_12[get]
    call_12 --> call_13[get]
    call_13 --> call_14[post]
    call_14 --> call_15[Timeout]
    call_15 --> call_16[type]
    call_16 --> End
```
