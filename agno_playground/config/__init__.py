"""
Config package exports.
Makes settings available directly from the config package.
"""

from .settings import agent_storage, BASE_DIR

__all__ = ["agent_storage", "BASE_DIR"]