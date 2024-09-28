from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32, int8, int16


class MapLand(BaseStruct):
    # @formatter:off
    id: int                      = Retriever(int32,   default = 0)
    terrain_type: int            = Retriever(int32,   default = 0)
    land_avoidance_distance: int = Retriever(int32,   default = 0)
    base_size: int               = Retriever(int32,   default = 0)
    zone: int                    = Retriever(int8,    default = 0)
    placement_type: int          = Retriever(int8,    default = 0)
    _padding1: int               = Retriever(int16,   default = 0)
    x: int                       = Retriever(int32,   default = 0)
    y: int                       = Retriever(int32,   default = 0)
    land_usage_percent: int      = Retriever(int8,    default = 0)
    by_player_mode: int          = Retriever(int8,    default = 0)
    _padding2: int               = Retriever(int16,   default = 0)
    start_area_radius: int       = Retriever(int32,   default = 0)
    terrain_edge_fade: int       = Retriever(int32,   default = 0)
    clumpiness_factor: int       = Retriever(int32,   default = 0)
    # @formatter:on
