"""Test configurations and fixtures.

Dribia 2021/03/23, Nabil Kakeh <nabil@dribia.com>
"""

import asyncio

import pytest


@pytest.fixture
def event_loop():
    """Provide an event loop to aio tests."""
    loop = asyncio.get_event_loop()
    yield loop
