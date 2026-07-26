---
type: api
title: "_scan_owasp_patterns"
source_path: "src/autogen_team/application/mcp/tools/security_review.py"
description: "Scan diff against OWASP patterns.  Args:     diff: The code diff string to analyze.  Returns:     List of findings dicts with rule, severity, location, description."
tags: [api]
last_verified_commit: "dc137c3"
---

# _scan_owasp_patterns

Source File: `src/autogen_team/application/mcp/tools/security_review.py`

Scan diff against OWASP patterns.  Args:     diff: The code diff string to analyze.  Returns:     List of findings dicts with rule, severity, location, description.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[split]
    call_0 --> call_1[enumerate]
    call_1 --> call_2[lstrip]
    call_2 --> call_3[search]
    call_3 --> call_4[startswith]
    call_4 --> call_5[startswith]
    call_5 --> call_6[lstrip]
    call_6 --> call_7[append]
    call_7 --> End
```
