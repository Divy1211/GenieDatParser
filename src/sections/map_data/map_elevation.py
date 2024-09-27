from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32


class MapElevation(BaseStruct):
    # @formatter:off
    percent: int            = Retriever(int32,  default = 0)
    terrain: int            = Retriever(int32,  default = 0)
    """aka height"""
    num_clumps: int         = Retriever(int32,  default = 0)
    base_terrain: int       = Retriever(int32,  default = 0)
    """aka spacing"""
    base_elevation: int     = Retriever(int32,  default = 0)
    """aka base_terrain_type"""
    tile_spacing: int       = Retriever(int32,  default = 0)
    """aka nase_elevation"""
    # @formatter:on
