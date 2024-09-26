from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, bool8


class TerrainUnit(BaseStruct):
    # @formatter:off
    mask: int         = Retriever(int16, min_ver = Version((7, 1)), default = 0)
    type: int         = Retriever(int16,                            default = 0)
    density: int      = Retriever(int16,                            default = 0)
    centralized: bool = Retriever(bool8,                            default = False)
    # @formatter:on
