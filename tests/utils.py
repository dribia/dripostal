"""Utility functions for the testing module.

Dribia 2021/03/23, Nabil Kakeh <nabil@dribia.com>
"""

import random
import string


def random_lower_string(k: int = 32) -> str:
    """Generate a random string in lowercase."""
    return "".join(random.choices(string.ascii_lowercase, k=k))
