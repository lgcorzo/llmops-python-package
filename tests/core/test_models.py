# %% IMPORTS

import typing as T
import pytest
from unittest.mock import MagicMock, patch

import pytest
from autogen_team.core import schemas
from autogen_team.core.models import BaselineAutogenModel  # replace 'your_module' with the actual module name


# %% MODELS


@pytest.fixture
def baseline_model():
    return BaselineAutogenModel()


def test_load_context(baseline_model):
    # Setup
    model_config = {}  # Provide your model config as necessary
    with patch("your_module.AssistantAgent") as MockAgent, patch("your_module.RoundRobinGroupChat") as MockGroupChat:
        MockAgent.return_value = MagicMock()
        MockGroupChat.return_value = MagicMock()

        # Execute
        baseline_model.load_context(model_config)

        # Verify
        MockAgent.assert_called_once()  # Verify AssistantAgent was called
        MockGroupChat.assert_called_once()  # Verify RoundRobinGroupChat was called


def test_predict(baseline_model):
    # Setup
    inputs = MagicMock()  # Define appropriate input for the predict function
    mock_output = MagicMock()

    with (
        patch("your_module.schemas.Outputs", return_value=mock_output),
        patch("your_module.RoundRobinGroupChat") as MockGroupChat,
    ):
        mock_response_stream = [
            MagicMock(content="Test response", type="response"),
            MagicMock(status="success", type="result"),
        ]
        MockGroupChat.return_value.stream.return_value = mock_response_stream

        # Execute
        outputs = baseline_model.predict(inputs)

        # Verify
        assert outputs is mock_output  # Ensure the correct output object is returned
        # Add other assertions related to the content of outputs as needed

    # Optionally check if results have been appended correctly
    # Ensure predictions formatting, indices etc. are tested as necessary.
