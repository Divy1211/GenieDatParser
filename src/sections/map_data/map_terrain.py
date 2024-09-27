from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32


class MapTerrain(BaseStruct):
    percent: int            = Retriever(int32,  default = 0)
    type: int               = Retriever(int32,  default = 0)
    num_clumps: int         = Retriever(int32,  default = 0)
    edge_spacing: int       = Retriever(int32,  default = 0)
    placement_zone: int     = Retriever(int32,  default = 0)
    """aka base_terrain_type"""
    clumpiness_factor: int  = Retriever(int32,  default = 0)
