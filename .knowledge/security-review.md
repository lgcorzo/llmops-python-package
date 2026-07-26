---
type: api
title: "security_review"
source_path: "src/autogen_team/application/mcp/tools/security_review.py"
description: "Analyze code diffs against OWASP patterns and R2R RAG security knowledge.  Args:     diff: The code diff string to review.  Returns:     Dict with status (approved/rejected) and findings list."
tags: [api]
last_verified_commit: "dc137c3"
---

# security_review

Source File: `src/autogen_team/application/mcp/tools/security_review.py`

Analyze code diffs against OWASP patterns and R2R RAG security knowledge.  Args:     diff: The code diff string to review.  Returns:     Dict with status (approved/rejected) and findings list.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[MCPService]
    call_0 --> call_1[get_prompt]
    call_1 --> call_2[get_prompt]
    call_2 --> call_3[_scan_owasp_patterns]
    call_3 --> call_4[join]
    call_4 --> call_5[format]
    call_5 --> call_6[any]
    call_6 --> call_7[_query_r2r_security]
    call_7 --> call_8[loads]
    call_8 --> call_9[get]
    call_9 --> call_10[get]
    call_10 --> call_11[strip]
    call_11 --> call_12[dumps]
    call_12 --> call_13[acompletion]
    call_13 --> call_14[exception]
    call_14 --> call_15[get]
    call_15 --> call_16[any]
    call_16 --> End
```
