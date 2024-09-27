from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, str16, Array16


class UnitLine(BaseStruct):
    # @formatter:off
    id: int                    = Retriever(int16,          default = 0)
    name: str                  = Retriever(str16,          default = "")
    unit_types: list[int]      = Retriever(Array16[int16], default_factory = lambda _: [])
    # @formatter:on
