from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16


class TileSize(BaseStruct):
    # @formatter:off
    width: int      = Retriever(i16, default = 0)
    height: int     = Retriever(i16, default = 0)
    delta_z: int    = Retriever(i16, default = 0)
    # @formatter:on
