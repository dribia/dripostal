"""Dripostal aio sub-package test module.

Dribia 2021/01/11, Albert Iribarne <iribarne@dribia.com>
"""

import json
from urllib import parse

import pytest
from pydantic import AnyHttpUrl
from pytest_mock import MockerFixture

from dripostal import Address
from dripostal.aio import DriPostal
from tests import utils


class MockResponse:
    """Mock response for the aiohttp ClientSession get method."""

    def __init__(self, text: str, status: int):
        """Mock object initialization.

        Args:
            text: Stringified JSON object.
            status: Status code.
        """
        self._text = text
        self.status = status

    async def json(self):
        """Mock response json method.

        Returns: Object loaded from the stringified JSON object.

        """
        return json.loads(self._text)

    async def __aexit__(self, exc_type, exc, tb):
        """Mock the asyncio-necessary __aexit__ method."""
        pass

    async def __aenter__(self):
        """Mock the asyncio-necessary __aenter__ method."""
        return self


@pytest.mark.parametrize(
    "host",
    [utils.random_lower_string(), f"{utils.random_lower_string()}/"],
)
@pytest.mark.parametrize("scheme", ["https", "http"])
def test_parse(event_loop, mocker: MockerFixture, scheme, host):
    """Test the parse method.

    Here we need to mock the `urllib.request.urlopen` method, since
    we want the test to be independent from external services.

    Args:
        event_loop: Event loop.
        mocker: Pytest mocker.
        scheme: Parametrized scheme.
        host: Parametrized host.

    """
    host = utils.random_lower_string()
    url = f"{scheme}://{host}"
    fake_parse_response = [
        {"label": label, "value": utils.random_lower_string()}
        for label in Address.__fields__
    ]
    magic_mocker = mocker.patch(
        "aiohttp.ClientSession.get",
        return_value=MockResponse(json.dumps(fake_parse_response), 200),
    )

    # Let's assert that the response is correctly parsed.
    dri_postal = DriPostal(url)
    input_address = "Carrer de la Llacuna, 162, 08018 Barcelona"
    address = event_loop.run_until_complete(dri_postal.parse(input_address))
    for el in fake_parse_response:
        assert getattr(address, el["label"]) == el["value"]
    # Let's assert that we have correctly built the URL.
    arg_1, *args = magic_mocker.call_args[0]
    assert isinstance(arg_1, AnyHttpUrl)
    assert arg_1.scheme == scheme
    assert arg_1.host == host
    assert arg_1.path == "/parse"
    assert parse.parse_qs(arg_1.query) == {"address": [input_address]}


@pytest.mark.parametrize(
    "host",
    [utils.random_lower_string(), f"{utils.random_lower_string()}/"],
)
@pytest.mark.parametrize("scheme", ["https", "http"])
def test_expand(event_loop, mocker: MockerFixture, host, scheme):
    """Test the expand method.

    Here we need to mock the `urllib.request.urlopen` method, since
    we want the test to be independent from external services.

    Args:
        event_loop: Event loop.
        mocker: Pytest mocker.
        scheme: Parametrized scheme.
        host: Parametrized host.

    """
    host = utils.random_lower_string()
    url = f"{scheme}://{host}"
    fake_expand_response = [utils.random_lower_string()]
    magic_mocker = mocker.patch(
        "aiohttp.ClientSession.get",
        return_value=MockResponse(json.dumps(fake_expand_response), 200),
    )

    # Let's assert that the response is correctly parsed.
    dri_postal = DriPostal(url)
    input_address = "Carrer de la Llacuna, 162, 08018 Barcelona"
    results = event_loop.run_until_complete(dri_postal.expand(input_address))
    assert fake_expand_response == results
    # Let's assert that we have correctly built the URL.
    arg_1, *args = magic_mocker.call_args[0]
    assert isinstance(arg_1, AnyHttpUrl)
    assert arg_1.scheme == scheme
    assert arg_1.host == host
    assert arg_1.path == "/expand"
    assert parse.parse_qs(arg_1.query) == {"address": [input_address]}
