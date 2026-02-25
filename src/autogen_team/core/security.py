"""Security utilities for autogen_team."""

import os


def safe_join(base: str, *paths: str) -> str:
    """Safely join paths, ensuring the result is within the base directory.

    Args:
        base: The base directory.
        paths: The paths to join to the base directory.

    Returns:
        The resolved absolute path.

    Raises:
        ValueError: If the resolved path is outside the base directory.
    """
    base_path = os.path.abspath(base)
    final_path = os.path.abspath(os.path.join(base, *paths))

    if os.path.commonpath([base_path, final_path]) != base_path:
        raise ValueError(f"Path traversal detected: {final_path} is outside {base_path}")

    return final_path
