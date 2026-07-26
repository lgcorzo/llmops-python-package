---
type: class
title: "Job"
source_path: "src/autogen_team/application/jobs/base.py"
description: "Base class for a job.  use a job to execute runs in  context. e.g., to define common services like logger  Parameters:     logger_service (services.LoggerService): manage the logger system.     alerts_service (services.AlertsService): manage the alerts system.     mlflow_service (services.MlflowService): manage the mlflow system."
tags: [class]
last_verified_commit: "dc137c3"
---

# Job

Source File: `src/autogen_team/application/jobs/base.py`

Base class for a job.  use a job to execute runs in  context. e.g., to define common services like logger  Parameters:     logger_service (services.LoggerService): manage the logger system.     alerts_service (services.AlertsService): manage the alerts system.     mlflow_service (services.MlflowService): manage the mlflow system.

## Architecture Visualization

```mermaid
classDiagram
    class Job {
        -__enter__()
        -__exit__(exc_type, exc_value, exc_traceback)
        +run()
    }
```
