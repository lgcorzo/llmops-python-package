---
type: api
title: "index_code"
source_path: "src/autogen_team/application/mcp/tools/index_code.py"
description: "Index a code file into R2R knowledge graph for future retrieval.  Args:     file_path: Path of the file being indexed.     content: Full content of the file.     metadata: Optional metadata dict (language, author, etc).  Returns:     Dict with document_id and status."
tags: [api]
last_verified_commit: "dc137c3"
---

# index_code

Source File: `src/autogen_team/application/mcp/tools/index_code.py`

Index a code file into R2R knowledge graph for future retrieval.  Args:     file_path: Path of the file being indexed.     content: Full content of the file.     metadata: Optional metadata dict (language, author, etc).  Returns:     Dict with document_id and status.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[Env]
    call_0 --> call_1[get]
    call_1 --> call_2[get]
    call_2 --> call_3[strip]
    call_3 --> call_4[AsyncClient]
    call_4 --> call_5[raise_for_status]
    call_5 --> call_6[json]
    call_6 --> call_7[error]
    call_7 --> call_8[error]
    call_8 --> call_9[post]
    call_9 --> call_10[Timeout]
    call_10 --> call_11[type]
    call_11 --> End
```
