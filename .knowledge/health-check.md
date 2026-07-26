---
type: api
title: "health_check"
source_path: "src/autogen_team/infrastructure/messaging/kafka_app.py"
description: "Simple health check endpoint to verify that the service is running."
tags: [api]
last_verified_commit: "dc137c3"
---

# health_check

Source File: `src/autogen_team/infrastructure/messaging/kafka_app.py`

Simple health check endpoint to verify that the service is running.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[get]
    call_0 --> End
```
