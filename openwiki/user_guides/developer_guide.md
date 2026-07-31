---
iso_doc_type: "Procedure"
iso_viewpoint: "QualityView"
type: "user_guide"
title: "ISO 26514 Developer & User Guide"
description: "Step-by-step instructions for environment installation, test execution, linting, and job configuration."
tags: ["iso26514", "developer_guide", "poetry", "pytest"]
timestamp: "2026-07-31T16:40:00Z"
---

# ISO 26514 Developer & User Guide

## 1. Prerequisites & Environment Setup

- **Python**: Python 3.10+ or Python 3.12
- **Poetry**: Package and virtualenv manager (`pip install poetry`)

Install project dependencies:
```bash
poetry install
```

---

## 2. Running Test Suites

Run unit tests using `pytest`:
```bash
poetry run pytest tests/
```

Run test coverage report:
```bash
poetry run pytest --cov=src/autogen_team tests/
```

---

## 3. Code Linting & Static Type Checking

Run `ruff` for linting and formatting checks:
```bash
poetry run ruff check src/ tests/
```

Run `mypy` for static type verification:
```bash
poetry run mypy src/
```

---

## 4. Updating OpenWiki Architecture Documentation

Whenever code changes are made to `src/autogen_team`, update the OpenWiki knowledge graph:
```bash
graphify update .
```
