# Architecture: `llmops-python-package` in Dark Gravity

## Ecosystem Role & Tier

- **Tier**: `owned_domain`
- **Role**: Domain-driven enterprise LLMOps standard package providing Hatchet workflow patterns, prompt evaluations, MCP tool conventions, and ISO/IEC/IEEE 42010 / 15289 documentation templates within Dark Gravity.
- **Visibility**: `public`

## Internal Component Design

- `confs/`, `MLproject`, `notebooks/`, `pyproject.toml` / `poetry.lock`: Standardized LLMOps configuration, evaluation workflows, and reproducible Python dependency locks.
- `k8s/`, `Dockerfile`, `docker-compose.yml`: Containerized deployment definitions integrated with Dark-LiteLLM and R2R endpoints.
- `docs/`, `graphify-out/`: Architecture documentation and AST/semantic graph outputs consumed during Dark Gravity knowledge indexing.

## Upstream & Downstream Ecosystem Interfaces

```text
llmops-python-package ──► Dark-LiteLLM Gateway (multi-model routing & evaluation)
                     ──► R2R v3 Engine & Hatchet Workflows
                     ◄── rust_CACD_autonomous_factory (mission orchestration & OKF synthesis)
```

## Security Boundary & Governance

- **Vertex 4 HITL**: Autonomous and manual updates land strictly through feature-branch PRs and CI gates.
- **No Unqualified Compliance Claims**: References to ISO/IEC/IEEE 42010 & 15289 reflect structural documentation conventions, not third-party regulatory certification (`DOC-011` compliant).

## Canonical Cross-Links

- [DARK_GRAVITY_MANIFEST.md](./DARK_GRAVITY_MANIFEST.md)
- [REPOSITORIES.md](./REPOSITORIES.md)
- [Global Architecture Portal](https://lgcorzo.github.io/architecture.html)
- [Unified Start-Here Portal](https://lgcorzo.github.io/start-here)
- [AI Auditor Pack](https://lgcorzo.github.io/docs/auditor/)
