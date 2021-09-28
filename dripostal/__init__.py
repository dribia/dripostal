"""Client for Pelias Libpostal Service.

Dribia 2021/03/23, Nabil Kakeh <nabil@dribia.com>
"""

try:
    from importlib.metadata import version  # type: ignore
except ModuleNotFoundError:
    from importlib_metadata import version  # type: ignore


import json
from typing import List
from urllib import parse, request

import pydantic
from pydantic import AnyHttpUrl

from dripostal.schemas import Address

__version__ = version(__name__)


class DriPostal:
    """Wrapper for binding pelias/libpostal service."""

    def __init__(self, url: str):
        """Dripostal configuration.

        Args:
            url: URL of the Libpostal service.

        """
        self.service_url: AnyHttpUrl = self._parse_url(url)

    @staticmethod
    def _parse_url(url: str):
        """Validate the URL parameter.

        Args:
            url: URL parameter.

        Returns: Parsed URL parameter.

        """
        return pydantic.parse_obj_as(AnyHttpUrl, url.rstrip("/"))

    def _get_url(self, method: str, address: str):
        """Get the request url for the specified method and address.

        Args:
            method: Libpostal method to call.
            address: Address to assess.

        Returns: Request URL.

        """
        q = parse.urlencode({"address": address})
        return pydantic.parse_obj_as(AnyHttpUrl, f"{self.service_url}/{method}?{q}")

    def parse(self, address: str) -> Address:
        """Parse an address with Libpostal.

        Args:
            address: Address to parse, in plain text.

        Returns: Parsed address.

        """
        request_url = self._get_url(method="parse", address=address)
        response = request.urlopen(request_url)
        payload = json.loads(response.read())
        return Address(**{el["label"]: el["value"] for el in payload})

    def expand(self, address: str) -> List[str]:
        """Expand an address with Libpostal.

        Args:
            address: Address to expand, in plain text.

        Returns: Expanded address.

        """
        request_url = self._get_url(method="expand", address=address)
        response = request.urlopen(request_url)
        payload = json.loads(response.read())
        return payload


__all__ = ["DriPostal", "Address"]
