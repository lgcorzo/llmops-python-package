<<<<<<< HEAD
## 2026-02-03 - [Hardcoded Secrets in MLflow Adapters]
**Vulnerability:** Found a hardcoded fallback API key and internal cluster URL in `mlflow_adapter.py`.
**Learning:** Custom MLflow adapters (`PythonModel` subclasses) might contain copy-pasted debugging configurations or hardcoded environments that were accidentally committed.
**Prevention:** Ensure all `PythonModel` implementations load configuration strictly from artifacts or environment variables, never from hardcoded dictionaries in `__init__`.
=======
## 2026-02-04 - Information Exposure in Kafka Service
**Vulnerability:** The Kafka consumer service (`kafka_app.py`) was logging raw input messages which could contain PII, and returning raw exception messages to the output topic which could leak internal implementation details.
**Learning:** In event-driven architectures like Kafka, error handling often involves producing to an error topic or the same output topic. Great care must be taken to sanitize these error messages. Also, logging "raw" messages for debugging is a common privacy trap.
**Prevention:** Always catch exceptions at the top level of the message processor, log the full stack trace securely (server-side), but return/produce only generic error codes or messages to the downstream systems. Sanitize input logs to exclude data fields.
>>>>>>> 36194fc (feat: Sanitize Kafka service logs and error responses)

## 2026-02-20 - [Path Traversal in MCP Tools]
**Vulnerability:** The `execute_code` and `run_tests` MCP tools allowed arbitrary file writes outside the sandbox directory via path traversal payloads (e.g., `../../etc/passwd` or absolute paths).
**Learning:** `os.path.join` is unsafe for untrusted input as it allows absolute paths to override the base directory and does not resolve `..` segments.
**Prevention:** Always use `os.path.abspath` to resolve paths and verify that the resulting path starts with the intended base directory (using `os.path.commonpath` or `startswith`). Implemented `safe_join` utility in `core/security.py`.
