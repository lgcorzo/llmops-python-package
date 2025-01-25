# test_metrics.py

import pytest
from unittest.mock import MagicMock, patch
import pandas as pd


# Assuming the metrics are in a module named 'metrics.py'
from autogen_team.core.metrics import (
    AutogenMetric,
    AutogenConversationMetric,
    Threshold,
)


# Mock schemas to avoid dependencies
@pytest.fixture(autouse=True)
def mock_schemas():
    with patch("autogen_team.core.metrics.schemas") as mock_schemas:
        mock_schemas.TargetsSchema.response = "response"
        mock_schemas.OutputsSchema.response = "response"
        mock_schemas.OutputsSchema.metadata = "metadata"
        yield mock_schemas


# Test AutogenMetric
class TestAutogenTextMetric:
    @pytest.mark.parametrize(
        "metric_type, y_true, y_pred, expected, threshold",
        [
            # Exact match cases
            (
                "exact_match",
                ["cat", "dog", "bird"],
                ["cat", "dog", "bird"],
                1.0,
                None,
            ),
            (
                "exact_match",
                ["apple", "banana", "cherry"],
                ["apple", "berry", "cherry"],
                0.666,
                0.7,
            ),
            # Similarity threshold cases
            (
                "similarity",
                ["apple", "banana"],
                ["app", "bananna"],
                1.0,  # Both above 0.7 threshold
                0.7,
            ),
            (
                "similarity",
                ["hello world", "foo bar"],
                ["helo world", "foo baz"],
                0.5,  # One above, one below threshold
                0.8,
            ),
            # Length ratio cases
            (
                "length_ratio",
                ["short", "medium text", "longer text"],
                ["shorter", "medium", "longer"],
                (7 / 5 + 6 / 11 + 6 / 12) / 3,
                None,
            ),
        ],
    )
    def test_score(self, metric_type, y_true, y_pred, expected, threshold):
        # Mock targets and outputs
        targets = MagicMock()
        targets.__getitem__.return_value = pd.Series(y_true)
        outputs = MagicMock()
        outputs.__getitem__.return_value = pd.Series(y_pred)

        # Initialize metric
        metric = AutogenMetric(
            name="test_metric",
            metric_type=metric_type,
            similarity_threshold=threshold or 0.7,
        )

        # Calculate and verify score
        assert pytest.approx(metric.score(targets, outputs), rel=0.01) == expected


# Test AutogenConversationMetric
class TestAutogenConversationMetric:
    @pytest.mark.parametrize(
        "metadata, check_term, check_err, expected",
        [
            # Perfect case
            (
                [{"terminated": True, "messages": []}] * 3,
                True,
                True,
                1.0,
            ),
            # Mixed quality case
            (
                [
                    {"terminated": True, "messages": []},
                    {"terminated": False, "messages": ["error"]},
                    {"terminated": True, "messages": ["error"]},
                ],
                True,
                True,
                (2 / 3) * (1 - 2 / 3),  # 0.222
            ),
            # Only check termination
            (
                [{"terminated": False}] * 4,
                True,
                False,
                0.0,
            ),
        ],
    )
    def test_score(self, metadata, check_term, check_err, expected):
        # Mock outputs
        outputs = MagicMock()
        outputs.__getitem__.return_value = pd.Series(metadata)

        metric = AutogenConversationMetric(
            name="conv_metric",
            check_termination=check_term,
            check_error_messages=check_err,
        )

        # Mock targets (not used)
        targets = MagicMock()

        assert pytest.approx(metric.score(targets, outputs), rel=0.01) == expected


# Test Threshold
class TestThreshold:
    @pytest.mark.parametrize(
        "threshold, greater_is_better",
        [
            (0.85, True),
            (10.0, False),
        ],
    )
    def test_to_mlflow(self, threshold, greater_is_better):
        thresh = Threshold(
            threshold=threshold,
            greater_is_better=greater_is_better,
        )
        mlflow_thresh = thresh.to_mlflow()

        assert mlflow_thresh.threshold == threshold
        assert mlflow_thresh.greater_is_better == greater_is_better


# Test Metric Integration
class TestMetricIntegration:
    def test_scorer_flow(self):
        # Mock dependencies
        mock_model = MagicMock()
        mock_inputs = MagicMock()
        mock_targets = MagicMock()
        mock_outputs = MagicMock()

        # Configure model to return outputs
        mock_model.predict.return_value = mock_outputs

        # Create metric with mocked score method
        metric = AutogenMetric(name="integration_test", metric_type="exact_match")
        metric.score = MagicMock(return_value=0.85)

        # Execute scorer
        result = metric.scorer(mock_model, mock_inputs, mock_targets)

        # Verify calls
        mock_model.predict.assert_called_once_with(inputs=mock_inputs)
        metric.score.assert_called_once_with(targets=mock_targets, outputs=mock_outputs)
        assert result == 0.85


if __name__ == "__main__":
    pytest.main(["-v", "test_metrics.py"])
