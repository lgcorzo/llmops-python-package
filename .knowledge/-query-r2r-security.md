---
type: api
title: "_query_r2r_security"
source_path: "src/autogen_team/application/mcp/tools/security_review.py"
description: "Query R2R RAG for security best practices relevant to the diff.  Args:     diff: Code diff to find context for.     r2r_base_url: R2R API base URL.  Returns:     List of relevant security documents."
tags: [api]
last_verified_commit: "dc137c3"
---

# _query_r2r_security

Source File: `src/autogen_team/application/mcp/tools/security_review.py`

Query R2R RAG for security best practices relevant to the diff.  Args:     diff: Code diff to find context for.     r2r_base_url: R2R API base URL.  Returns:     List of relevant security documents.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[AsyncClient]
    call_0 --> call_1[raise_for_status]
    call_1 --> call_2[json]
    call_2 --> call_3[get]
    call_3 --> call_4[cast]
    call_4 --> call_5[post]
    call_5 --> call_6[get]
    call_6 --> call_7[Timeout]
    call_7 --> End
```
