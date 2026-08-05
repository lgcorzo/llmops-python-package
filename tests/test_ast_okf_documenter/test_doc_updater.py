import pytest
import subprocess
import os

def test_full_mode():
    result = subprocess.run(['python3', 'scripts/doc_updater.py', 'full'], capture_output=True, text=True)
    assert result.returncode == 0
    assert os.path.exists('openwiki/SUMMARY.md')

def test_diff_mode():
    result = subprocess.run(['python3', 'scripts/doc_updater.py', 'diff'], capture_output=True, text=True)
    assert result.returncode == 0
