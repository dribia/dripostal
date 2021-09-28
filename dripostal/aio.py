"""Asynchronous client for Pelias Libpostal Service.

Dribia 2021/03/23, Nabil Kakeh <nabil@dribia.com>
"""

from typing import List

try:
    from aiohttp import ClientSession
except ModuleNotFoundError as e:
    msg = (
        e.msg
        + " You can install it as an optional dependency installing dripostal[aiohttp]."
    )
    raise ModuleNotFoundError(msg)

from . import DriPostal as _BaseDriPostal
from .schemas import Address


class DriPostal(_BaseDriPostal):
    """Asynchronous version of the DriPostal client."""

    async def parse(self, address: str) -> Address:  # type: ignore
        """Parse an address with Libpostal.

        Args:
            address: Address to parse, in plain text.

        Returns: Parsed address.

        """
        request_url = self._get_url(method="parse", address=address)
        async with ClientSession() as session:
            async with session.get(request_url) as response:
                payload = await response.json()
                return Address(**{el["label"]: el["value"] for el in payload})

    async def expand(self, address: str) -> List[str]:  # type: ignore
        """Expand an address with Libpostal.

        Args:
            address: Address to expand, in plain text.

        Returns: Expanded address.

        """
        request_url = self._get_url(method="expand", address=address)
        async with ClientSession() as session:
            async with session.get(request_url) as response:
                return await response.json()


__all__ = ["DriPostal"]
