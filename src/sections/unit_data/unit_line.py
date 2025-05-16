from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, str16, Array16


class UnitLine(BaseStruct):
    # @formatter:off
    id: int                    = Retriever(i16,          default = 0)
    name: str                  = Retriever(str16,        default = "")
    unit_types: list[int]      = Retriever(Array16[i16], default_factory = lambda _ver: [])
    # @formatter:on
