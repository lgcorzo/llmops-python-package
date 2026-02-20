"""Security utilities for path validation and sanitization."""

import os
import typing as T


def safe_join(base_dir: str, *paths: str) -> str:
    """Safely join paths ensuring the result is strictly within base_dir.

    Args:
        base_dir: The trusted base directory.
        paths: Path components to join.

    Returns:
        The absolute path if safe.

    Raises:
        ValueError: If the resulting path is outside or equals base_dir.
    """
    base_dir = os.path.abspath(base_dir)
    full_path = os.path.abspath(os.path.join(base_dir, *paths))

    if not full_path.startswith(base_dir + os.sep):
        raise ValueError(f"Path traversal attempt: {full_path} is outside {base_dir}")

    return full_path
