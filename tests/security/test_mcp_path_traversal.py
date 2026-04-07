import json
import os
import tempfile
import typing as T
from unittest.mock import MagicMock, patch

import pytest

from autogen_team.application.mcp.tools.execute_code import execute_code
from autogen_team.application.mcp.tools.run_tests import run_tests


@pytest.mark.asyncio
async def test_execute_code_path_traversal() -> None:
    # Setup
    target_file: str = "/tmp/autogen_team_pwned.txt"
    if os.path.exists(target_file):
        os.remove(target_file)

    # The vulnerability: ../../../../../../../../../tmp/autogen_team_pwned.txt
    malicious_path: str = "../../../../../../../../../../tmp/autogen_team_pwned.txt"

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = json.dumps(
        {"files_changed": [{"path": malicious_path, "action": "create", "content": "PWNED"}]}
    )

    with patch("autogen_team.application.mcp.tools.execute_code.MCPService") as MockMCPService:
        MockMCPService.return_value.get_prompt.return_value = "system prompt"
        MockMCPService.return_value.litellm_model = "gpt-4o"
        MockMCPService.return_value.litellm_api_base = "http://localhost"
        MockMCPService.return_value.litellm_api_key = "fake"

        with patch("litellm.acompletion", return_value=mock_response):
            await execute_code({"name": "test task"}, "/tmp")

            if os.path.exists(target_file):
                content = open(target_file).read()
                os.remove(target_file)
                if content == "PWNED":
                    pytest.fail(f"VULNERABILITY EXPLOITED: File written to {target_file}")


@pytest.mark.asyncio
async def test_run_tests_path_traversal() -> None:
    # Setup
    target_file: str = "/tmp/autogen_team_pwned_run_tests.txt"
    if os.path.exists(target_file):
        os.remove(target_file)

    malicious_path: str = "../../../../../../../../../../tmp/autogen_team_pwned_run_tests.txt"

    changes: T.Dict[str, T.Any] = {
        "files_changed": [{"path": malicious_path, "action": "create", "content": "PWNED"}]
    }

    # Use a safe temp dir as workspace
    with tempfile.TemporaryDirectory() as workspace_dir:
        await run_tests(changes, workspace_dir)

    if os.path.exists(target_file):
        content: str = open(target_file).read()
        os.remove(target_file)
        if content == "PWNED":
            pytest.fail(f"VULNERABILITY EXPLOITED: File written to {target_file}")


@pytest.mark.asyncio
async def test_execute_code_workspace_path_traversal() -> None:
    # Test that execute_code rejects workspace_path pointing outside current dir
    malicious_workspace: str = "../../../../../etc"
    task: T.Dict[str, T.Any] = {"name": "test task"}

    with patch("autogen_team.application.mcp.tools.execute_code.os.walk") as mock_walk:
        mock_walk.return_value = []
        with patch("autogen_team.application.mcp.tools.execute_code.MCPService") as MockMCPService:
            MockMCPService.return_value.litellm_model = "gpt-4o"
            MockMCPService.return_value.litellm_api_base = "http://localhost"
            MockMCPService.return_value.litellm_api_key = "fake"
            MockMCPService.return_value.get_prompt.return_value = "system prompt"

            mock_response = MagicMock()
            mock_response.choices = [MagicMock()]
            mock_response.choices[0].message.content = json.dumps({"files_changed": []})

            with patch("litellm.acompletion", return_value=mock_response):
                result = await execute_code(task, malicious_workspace)
                assert result["status"] == "error"
                assert any("Security Error" in err for err in result["validation_errors"])


@pytest.mark.asyncio
async def test_run_tests_workspace_path_traversal() -> None:
    # Test that run_tests rejects workspace_path pointing outside current dir
    malicious_workspace: str = "../../../../../etc"
    changes: T.Dict[str, T.Any] = {"files_changed": []}

    with patch("autogen_team.application.mcp.tools.run_tests.shutil.copytree") as mock_copy:
        result = await run_tests(changes, workspace_path=malicious_workspace)
        assert result["passed"] is False
        assert "Security Error" in result["summary"]
        mock_copy.assert_not_called()
