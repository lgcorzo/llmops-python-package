---
type: "module-architecture"
title: "Evaluation Architecture: src/autogen_team/evaluation"
description: "Technical architecture for evaluation metrics and entities"
tags: ["architecture", "evaluation", "metrics", "openwiki"]
timestamp: "2026-07-30T00:00:00Z"
---

# Module Name: evaluation

* **Source Directory Reference:** `src/autogen_team/evaluation/`
* **Package Dependency:** Upstream: `pandas`, `pydantic`. Downstream: `src/autogen_team/application/jobs/evaluations.py`.

## 1. Executive Summary & Purpose

The `evaluation` module provides metric evaluation calculation logic and result container structures. It measures prediction accuracy, similarity, token usage, latency, and quality benchmarks for LLM responses.

## 2. UML 2.0 Class & Metrics Architecture (Deterministic)

```mermaid
classDiagram
    direction BT
    class EvaluationMetric {
        <<interface>>
        +compute(predictions, targets)* MetricResult
    }
    class AccuracyMetric {
        +compute(predictions, targets) MetricResult
    }
    class SimilarityMetric {
        +compute(predictions, targets) MetricResult
    }
    class EvaluationResult {
        +metrics: Dict[str, float]
        +passed: bool
    }

    EvaluationMetric <|-- AccuracyMetric
    EvaluationMetric <|-- SimilarityMetric
    EvaluationResult --> EvaluationMetric : Aggregates
```

## 3. Package & Class Relations

* **Metric Computing:** Calculates evaluation benchmarks between model output predictions (`OutputsSchema`) and expected ground truth targets (`TargetsSchema`).
* **Result Aggregation:** `EvaluationResult` packages numeric metrics and Boolean assertion checks used by `Evaluations` job and `Promotion` job.

## 4. Execution Flow & Runtime Behavior

```mermaid
sequenceDiagram
    autonumber
    participant Job as Evaluation Job
    participant Metric as EvaluationMetric
    participant Result as EvaluationResult

    Job->>Metric: compute(predictions, targets)
    Metric-->>Job: MetricResult (e.g. score=0.92)
    Job->>Result: EvaluationResult(metrics={"accuracy": 0.92}, passed=True)
    Result-->>Job: Aggregated Result
```

---

* **Source Citations:**
  * Evaluation Entities: `src/autogen_team/evaluation/entities.py:1-25`
  * Metrics Implementations: `src/autogen_team/evaluation/metrics/metrics.py:1-35`
