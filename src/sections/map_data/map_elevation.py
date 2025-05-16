from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32


class MapElevation(BaseStruct):
    # @formatter:off
    percent: int            = Retriever(i32,  default = 0)
    terrain: int            = Retriever(i32,  default = 0)
    """aka height"""
    num_clumps: int         = Retriever(i32,  default = 0)
    base_terrain: int       = Retriever(i32,  default = 0)
    """aka spacing"""
    base_elevation: int     = Retriever(i32,  default = 0)
    """aka base_terrain_type"""
    tile_spacing: int       = Retriever(i32,  default = 0)
    """aka nase_elevation"""
    # @formatter:on
