from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32


class MapTerrain(BaseStruct):
    # @formatter:off
    percent: int            = Retriever(i32,  default = 0)
    type: int               = Retriever(i32,  default = 0)
    num_clumps: int         = Retriever(i32,  default = 0)
    edge_spacing: int       = Retriever(i32,  default = 0)
    placement_zone: int     = Retriever(i32,  default = 0)
    """aka base_terrain_type"""
    clumpiness_factor: int  = Retriever(i32,  default = 0)
    # @formatter:on
