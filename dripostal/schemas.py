"""Schemes related for Libpostal responses.

Dribia 2021/03/23, Nabil Kakeh <nabil@dribia.com>
"""

from typing import List, Optional, Tuple

from pydantic import BaseModel


class Address(BaseModel):
    """Base model for parse query response."""

    house: Optional[str]
    category: Optional[str]
    near: Optional[str]
    house_number: Optional[str]
    road: Optional[str]
    unit: Optional[str]
    level: Optional[str]
    entrance: Optional[str]
    po_box: Optional[str]
    postcode: Optional[str]
    suburb: Optional[str]
    city_district: Optional[str]
    city: Optional[str]
    island: Optional[str]
    state_district: Optional[str]
    state: Optional[str]
    country_region: Optional[str]
    country: Optional[str]
    world_region: Optional[str]

    def list(self) -> List[Tuple[str, str]]:
        """Return object as same format as pypostal."""
        return [(k, v) for k, v in self.dict(exclude_unset=True).items()]
