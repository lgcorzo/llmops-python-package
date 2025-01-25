# %% IMPORTS
import pytest
from unittest.mock import MagicMock, patch
import pandas as pd
import typing as T

from autogen_agentchat.base import TaskResult
from autogen_team.core.models import BaselineAutogenModel, Model
from autogen_team.core import schemas


@pytest.fixture
def baseline_model():
    """Fixture to create an instance of BaselineAutogenModel."""
    return BaselineAutogenModel()


def test_get_params(baseline_model):
    """Test the get_params method."""
    # Setup
    baseline_model.assistant_agent = "MockAssistantAgent"
    baseline_model.team = "MockTeam"

    # Execute
    params = baseline_model.get_params()

    # Verify
    assert "assistant_agent" in params
    assert "team" in params
    assert params["assistant_agent"] == "MockAssistantAgent"
    assert params["team"] == "MockTeam"


def test_set_params(baseline_model):
    """Test the set_params method."""
    # Setup
    new_params = {"assistant_agent": "NewAgent", "team": "NewTeam"}

    # Execute
    baseline_model.set_params(**new_params)

    # Verify
    assert baseline_model.assistant_agent == "NewAgent"
    assert baseline_model.team == "NewTeam"


def test_predict(baseline_model):
    """Test the predict method of BaselineAutogenModel."""
    # Setup
    input_data = pd.DataFrame({"input": ["Some large input string"]})
    inputs = schemas.Inputs(input_data)


    with patch("autogen_team.core.models.RoundRobinGroupChat") as MockRun:
        # Mocking the response stream
        mock_task_result = MagicMock()


        MockRun.run.return_value = [
            MagicMock(content="Message 1"),
            MagicMock(content="Message 2"),
            MagicMock(spec=TaskResult, result="Result 1")
        ]

        # Ensure the baseline model's `team` uses the mock
        baseline_model.team = MockRun

        # Execute
        outputs = baseline_model.predict(inputs)

        # Verify
        assert outputs is not None
        assert "Message 1" in outputs["response"][0]
        assert "Message 2" in outputs["response"][0]
        assert "Task Result: Result 1" in outputs["response"][0]

        # Additional metadata validation (optional)
        assert isinstance(outputs["metadata"][0], dict), "Metadata should be a dictionary"
        assert "timestamp" in outputs["metadata"][0], "Metadata timestamp is missing"
        assert "model_version" in outputs["metadata"][0], "Metadata model_version is missing"


def test_explain_model_not_implemented(baseline_model):
    """Test explain_model raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        baseline_model.explain_model()


def test_explain_samples_not_implemented(baseline_model):
    """Test explain_samples raises NotImplementedError."""
    input_data = pd.DataFrame({"input": ["Some large input string"]})
    inputs = schemas.Inputs(input_data)
    with pytest.raises(NotImplementedError):
        baseline_model.explain_samples(inputs)


def test_get_internal_model(baseline_model):
    """Test get_internal_model returns the team."""
    # Setup
    mock_team = MagicMock()
    baseline_model.team = mock_team

    # Execute
    internal_model = baseline_model.get_internal_model()

    # Verify
    assert internal_model == mock_team, "get_internal_model should return the team attribute"


def test_model_class_config():
    """Test the Config settings for the Model class."""

    class CustomModel(Model):
        KIND: T.Literal["CustomModel"] = "CustomModel"
        @T.override
        def load_context(self, model_config):
            pass

    # Verify Config
    assert CustomModel.Config.arbitrary_types_allowed is True


def test_load_context(baseline_model):
    # Setup
    model_config = {}  # Provide your model config as necessary
    with (
        patch("autogen_team.core.models.AssistantAgent") as MockAgent,
        patch("autogen_team.core.models.RoundRobinGroupChat") as MockGroupChat,
        patch("autogen_team.core.models.OpenAIChatCompletionClient") as MockOpenAIChatCompletionClient,
        patch("autogen_team.core.models.TextMentionTermination") as MockTextMentionTermination,
    ):
        MockAgent.return_value = MagicMock()
        MockGroupChat.return_value = MagicMock()
        MockOpenAIChatCompletionClient.return_value = MagicMock()
        MockTextMentionTermination.return_value = MagicMock()

        # Execute
        baseline_model.load_context(model_config)

        # Verify
        MockAgent.assert_called_once()  # Verify AssistantAgent was called
        MockGroupChat.assert_called_once()  # Verify RoundRobinGroupChat was called
        MockOpenAIChatCompletionClient.assert_called_once()  # Verify AssistantAgent was called
        MockTextMentionTermination.assert_called_once()  # Verify RoundRobinGroupChat was called
