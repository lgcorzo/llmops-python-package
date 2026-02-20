"""Tests for MCP path traversal vulnerabilities."""

import json
import os
import tempfile
import typing as T
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from autogen_team.application.mcp.tools.execute_code import execute_code
from autogen_team.application.mcp.tools.run_tests import run_tests


@pytest.mark.asyncio
async def test_execute_code_path_traversal() -> None:
    """Test execute_code allows path traversal (vulnerability confirmation)."""
    # Create a directory outside the sandbox to target
    with tempfile.TemporaryDirectory() as outside_sandbox:
        target_file = os.path.join(outside_sandbox, "pwned.txt")

        # We need to construct a relative path that goes up from the sandbox dir
        # Since we don't know the exact sandbox dir path, we'll just try to write to /tmp/pwned.txt
        # or use an absolute path if the system allows it (which os.path.join does).

        # Using absolute path is the easiest way to demonstrate the vulnerability
        # because os.path.join(base, /abs/path) returns /abs/path.

        malicious_path = target_file

        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = json.dumps(
            {
                "files_changed": [
                    {
                        "path": malicious_path,
                        "action": "create",
                        "content": "PWNED",
                    }
                ]
            }
        )

        task = {"name": "pwn", "description": "pwn"}

        with patch("autogen_team.application.mcp.tools.execute_code.litellm") as mock_litellm:
            mock_litellm.acompletion = AsyncMock(return_value=mock_response)
            # workspace_path doesn't matter much here
            result = await execute_code(task=task, workspace_path=outside_sandbox)

        # Check if the file was written outside the sandbox
        if os.path.exists(target_file):
            pytest.fail("Vulnerability triggered: File was written to target path!")

        # Verify error reporting
        assert len(result["validation_errors"]) > 0
        assert "Path traversal attempt" in result["validation_errors"][0]


@pytest.mark.asyncio
async def test_run_tests_path_traversal() -> None:
    """Test run_tests allows path traversal (vulnerability confirmation)."""
    with tempfile.TemporaryDirectory() as outside_sandbox:
        target_file = os.path.join(outside_sandbox, "pwned_test.txt")
        malicious_path = target_file

        changes = {
            "files_changed": [
                {
                    "path": malicious_path,
                    "action": "create",
                    "content": "PWNED_TEST",
                }
            ]
        }

        await run_tests(changes=changes, workspace_path=outside_sandbox)

        if os.path.exists(target_file):
            pytest.fail("Vulnerability triggered: File was written to target path!")
