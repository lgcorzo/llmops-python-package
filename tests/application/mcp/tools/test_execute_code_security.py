import pytest
import json
from unittest.mock import patch, MagicMock, AsyncMock
from pathlib import Path
from autogen_team.application.mcp.tools.execute_code import execute_code


@pytest.mark.asyncio
async def test_path_traversal_vulnerability(tmp_path: Path) -> None:
    # Setup directories
    jail_root = tmp_path / "jail"
    jail_root.mkdir()

    # The sandbox will be inside jail_root
    sandbox_dir = jail_root / "sandbox"
    sandbox_dir.mkdir()

    # The target file we try to overwrite outside sandbox
    sensitive_file = jail_root / "sensitive.txt"
    sensitive_file.write_text("secret")

    # Mock LLM response to try to overwrite ../sensitive.txt
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = json.dumps(
        {"files_changed": [{"path": "../sensitive.txt", "action": "create", "content": "hacked"}]}
    )

    with (
        patch("autogen_team.application.mcp.tools.execute_code.litellm") as mock_litellm,
        patch(
            "autogen_team.application.mcp.tools.execute_code.tempfile.mkdtemp",
            return_value=str(sandbox_dir),
        ),
    ):
        mock_litellm.acompletion = AsyncMock(return_value=mock_response)

        result = await execute_code(task={"name": "hack"}, workspace_path=str(tmp_path))

    # Check if file was overwritten
    if sensitive_file.read_text() != "secret":
        pytest.fail("Path traversal vulnerability confirmed! File was overwritten.")

    # Check that the security error was caught and reported
    assert result["status"] == "error"
    assert any("Security error" in err for err in result["validation_errors"])
