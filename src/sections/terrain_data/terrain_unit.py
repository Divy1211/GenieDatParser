from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i16, bool8


class TerrainUnit(BaseStruct):
    # @formatter:off
    mask: int         = Retriever(i16, min_ver = Version(7, 1), default = 0)
    type: int         = Retriever(i16,                          default = 0)
    density: int      = Retriever(i16,                          default = 0)
    centralized: bool = Retriever(bool8,                        default = False)
    # @formatter:on
