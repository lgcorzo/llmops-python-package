# %% IMPORTS
import pytest
from unittest.mock import MagicMock, patch


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
    """Test the predict method."""
    # Setup
    inputs = schemas.Inputs(index=0, data={"input_data": "test"})
    outputs_schema_mock = schemas.OutputsSchema(prediction="mock_prediction")

    with patch("autogen_team.core.models.RoundRobinGroupChat.run") as MockRun:
        # Mocking the response stream
        task_result = MagicMock(spec=schemas.TaskResult)
        task_result.result = "mock_result"

        MockRun.return_value = [
            MagicMock(content="Message 1"),
            MagicMock(content="Message 2"),
            task_result,
        ]

        baseline_model.team = MagicMock()
        baseline_model.team.run = MockRun

        # Execute
        outputs = baseline_model.predict(inputs)

        # Verify
        assert outputs is not None
        assert outputs.schema[outputs_schema_mock.prediction] == "Message 1\nMessage 2\nTask Result: mock_result"


def test_explain_model_not_implemented(baseline_model):
    """Test explain_model raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        baseline_model.explain_model()


def test_explain_samples_not_implemented(baseline_model):
    """Test explain_samples raises NotImplementedError."""
    inputs = schemas.Inputs(index=0, data={"input_data": "test"})
    with pytest.raises(NotImplementedError):
        baseline_model.explain_samples(inputs)


def test_get_internal_model_not_implemented(baseline_model):
    """Test get_internal_model raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        baseline_model.get_internal_model()


def test_model_class_config():
    """Test the Config settings for the Model class."""

    class CustomModel(Model):
        KIND = "CustomModel"

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