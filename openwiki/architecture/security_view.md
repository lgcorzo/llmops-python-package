---
iso_doc_type: "Description"
iso_viewpoint: "SecurityView"
type: "architecture"
title: "Security View"
description: "ISO 42010 Security View: path traversal guards, sandbox isolation, OWASP scanning, and secret management."
tags: ["iso42010", "security", "sandbox", "owasp", "path-traversal"]
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "686fdc0"
timestamp: "2026-08-01T13:16:00Z"
---

# Security View: Autogen Team

## 1. Security Architecture Overview

```mermaid
flowchart TB
    subgraph SecurityBoundary["Security Boundary"]
        subgraph PathGuard["Path Traversal Protection"]
            safe_join["safe_join() — core/security.py:L6-L27"]
        end
        subgraph SandboxIsolation["Sandbox Isolation"]
            E2B["E2B Code Interpreter (Firecracker MicroVM)"]
            Subprocess["SubprocessSandbox (Local Fallback)"]
        end
        subgraph CodeReview["Automated Code Review"]
            OWASP["OWASP Pattern Scanner"]
            R2RRAG["R2R RAG Security KB"]
        end
        subgraph SecretMgmt["Secret Management"]
            EnvVars["Pydantic Settings Env Singleton"]
            DotEnv[".env file (local)"]
            K8sSecrets["K8s Sealed Secrets (production)"]
        end
    end
```

## 2. Path Traversal Protection

**Module:** `src/autogen_team/core/security.py:L6-L27`

The `safe_join()` function prevents path traversal attacks by resolving symlinks and validating the final path stays within the base directory:

```python
def safe_join(base: str, *paths: str) -> str:
    base_dir = os.path.realpath(base)
    final_path = os.path.realpath(os.path.join(base_dir, *paths))
    if os.path.commonpath([base_dir, final_path]) != base_dir:
        raise ValueError(f"Path traversal detected: {final_path} is not within {base_dir}")
    return final_path
```

**Usage Points:**
- `infrastructure/services/sandbox_service.py:L162-L168` — Validates artifact upload paths
- `application/mcp/tools/run_tests.py` — Validates workspace directories for test execution

## 3. Sandbox Isolation

**Module:** `src/autogen_team/infrastructure/services/sandbox_service.py:L39-L189`

```mermaid
classDiagram
    class SandboxService {
        -use_e2b_fallback: bool
        -active_sandboxes: Dict
        -_execution_timeout: int
        +create_sandbox(metadata: Dict) str
        +execute(sandbox_id: str, command: str) SandboxExecutionResult
        +run_python_tests(sandbox_id: str, workspace_dir: str) SandboxExecutionResult
        +destroy(sandbox_id: str) void
        +upload_artifact(sandbox_id: str, file_path: str, bucket_name: str) str
    }
    class SandboxExecutionResult {
        +exit_code: int
        +stdout: str
        +stderr: str
        +artifacts: List~str~
    }
    SandboxService --> SandboxExecutionResult : produces
```

| Security Feature | Implementation | Location |
| :--- | :--- | :--- |
| **MicroVM Isolation** | E2B Code Interpreter (Firecracker-based) | `sandbox_service.py:L62-L71` |
| **Execution Timeout** | Configurable via `SANDBOX_TIMEOUT_SECONDS` (default: 300s) | `sandbox_service.py:L45` |
| **Artifact Path Validation** | `safe_join()` before S3 upload | `sandbox_service.py:L161-L168` |
| **Command Sanitization** | `shlex.quote()` for workspace directories | `sandbox_service.py:L126` |
| **Resource Cleanup** | Automatic sandbox destruction via `destroy()` | `sandbox_service.py:L129-L142` |

## 4. OWASP & Security Review

**Module:** `src/autogen_team/application/mcp/tools/security_review.py`

The `security_review` MCP tool performs automated security analysis on code diffs:

1. **OWASP Pattern Scanning** (`_scan_owasp_patterns`): Regex-based detection of common vulnerability patterns.
2. **RAG Security Knowledge** (`_query_r2r_security`): Queries R2R knowledge graph for security best practices relevant to the diff context.

```mermaid
sequenceDiagram
    participant Agent as ReviewerAgent
    participant Tool as security_review()
    participant OWASP as _scan_owasp_patterns()
    participant R2R as R2R RAG API

    Agent->>Tool: security_review(diff)
    activate Tool
    Tool->>OWASP: Scan diff against patterns
    OWASP-->>Tool: Pattern matches
    Tool->>R2R: Query security best practices
    R2R-->>Tool: Relevant security knowledge
    Tool->>Tool: Aggregate findings
    Tool-->>Agent: {status, analysis, findings}
    deactivate Tool
```

## 5. Secret Management

| Layer | Mechanism | Scope |
| :--- | :--- | :--- |
| **Local Development** | `.env` file + `Env` Pydantic Settings | `infrastructure/io/osvariables.py:L47-L52` |
| **Production (K8s)** | Kubernetes Sealed Secrets → env vars | GitOps deployment manifests |
| **API Keys** | `LITELLM_API_KEY`, `HATCHET_CLIENT_TOKEN`, `AWS_*` | Never hardcoded in source |
| **MLflow Config** | Environment-variable expansion in model configs | `models/entities.py:L200-L208` (`expand_env()`) |

### Environment Variable Expansion

The `BaselineAutogenModel.load_context()` method supports `${VAR_NAME}` syntax for resolving secrets at runtime:

```python
def expand_env(value: Any) -> Any:
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        env_var = value[2:-1]
        return os.getenv(env_var, value)
    return value
```

## 6. Known Security Considerations

Based on the security sentinel log (`wiki/sentinel.md`):

| Date | Issue | Status |
| :--- | :--- | :--- |
| 2024-05-15 | Path Traversal in MCP Tools | Fixed (`safe_join`) |
| 2024-10-24 | Insecure Default Bind Address in MCP Server | Mitigated (configurable via `MCP_HOST`) |
| 2026-02-03 | Hardcoded Secrets in MLflow Adapters | Fixed (env var expansion) |
| 2026-02-04 | Information Exposure in Kafka Service | Fixed (error message sanitization) |
| 2026-02-05 | Path Traversal in MCP Tools (additional) | Fixed (`safe_join` hardening) |
