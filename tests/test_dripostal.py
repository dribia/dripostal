"""Dripostal package test module.

Dribia 2021/01/11, Albert Iribarne <iribarne@dribia.com>
"""

import json
import re
from io import StringIO
from urllib import parse

import pytest
from pydantic import AnyHttpUrl, ValidationError
from pytest_mock import MockerFixture

import dripostal
from dripostal import Address, DriPostal
from tests import utils


def test_version():
    """Assert that `__version__` exists and is valid."""
    assert re.match(r"\d.\d.\d", dripostal.__version__)


def test_address_to_list():
    """Test the Address schema `to_list` method."""
    address_args = {k: utils.random_lower_string() for k in Address.__fields__}
    address = Address(**address_args)
    for k, v in address.list():
        assert address_args[k] == v


def test_base_url_error():
    """Test the base URL setting on init."""
    url = utils.random_lower_string()
    with pytest.raises(ValidationError):
        _ = DriPostal(url)


@pytest.mark.parametrize(
    "host",
    [utils.random_lower_string(), f"{utils.random_lower_string()}/"],
)
@pytest.mark.parametrize("scheme", ["https", "http"])
def test_base_url(host, scheme):
    """Test the base URL setting on init."""
    url = f"{scheme}://{utils.random_lower_string()}"
    dri_postal = DriPostal(url)
    assert isinstance(dri_postal.service_url, AnyHttpUrl)
    assert str(dri_postal.service_url) == url


@pytest.mark.parametrize(
    "host",
    [utils.random_lower_string(), f"{utils.random_lower_string()}/"],
)
@pytest.mark.parametrize("scheme", ["https", "http"])
def test_parse(mocker: MockerFixture, scheme, host):
    """Test the parse method.

    Here we need to mock the `urllib.request.urlopen` method, since
    we want the test to be independent from external services.

    Args:
        mocker: Pytest mocker.
        scheme: Parametrized scheme.
        host: Parametrized host.

    """
    url = f"{scheme}://{host}"
    fake_parse_response = [
        {"label": label, "value": utils.random_lower_string()}
        for label in Address.__fields__
    ]
    magic_mocker = mocker.patch(
        "dripostal.request.urlopen",
        return_value=StringIO(json.dumps(fake_parse_response)),
    )

    # Let's assert that the response is correctly parsed.
    dri_postal = DriPostal(url)
    input_address = "Carrer de la Llacuna, 162, 08018 Barcelona"
    address = dri_postal.parse(input_address)
    for el in fake_parse_response:
        assert getattr(address, el["label"]) == el["value"]

    # Let's assert that we have correctly built the URL.
    arg_1, *args = magic_mocker.call_args[0]
    assert isinstance(arg_1, AnyHttpUrl)
    assert arg_1.scheme == scheme
    assert arg_1.host == host.rstrip("/")
    assert arg_1.path == "/parse"
    assert parse.parse_qs(arg_1.query) == {"address": [input_address]}


@pytest.mark.parametrize(
    "host",
    [utils.random_lower_string(), f"{utils.random_lower_string()}/"],
)
@pytest.mark.parametrize("scheme", ["https", "http"])
def test_expand(mocker: MockerFixture, host, scheme):
    """Test the expand method.

    Here we need to mock the `urllib.request.urlopen` method, since
    we want the test to be independent from external services.

    Args:
        mocker: Pytest mocker.
        scheme: Parametrized scheme.
        host: Parametrized host.

    """
    url = f"{scheme}://{host}"
    fake_expand_response = [utils.random_lower_string()]
    magic_mocker = mocker.patch(
        "dripostal.request.urlopen",
        return_value=StringIO(json.dumps(fake_expand_response)),
    )

    # Let's assert that the response is correctly parsed.
    dri_postal = DriPostal(url)
    input_address = "Carrer de la Llacuna, 162, 08018 Barcelona"
    results = dri_postal.expand(input_address)
    assert fake_expand_response == results

    # Let's assert that we have correctly built the URL.
    arg_1, *args = magic_mocker.call_args[0]
    assert isinstance(arg_1, AnyHttpUrl)
    assert arg_1.scheme == scheme
    assert arg_1.host == host.rstrip("/")
    assert arg_1.path == "/expand"
    assert parse.parse_qs(arg_1.query) == {"address": [input_address]}
