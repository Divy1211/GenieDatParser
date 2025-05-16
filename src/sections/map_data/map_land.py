from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32, i8, i16


class MapLand(BaseStruct):
    # @formatter:off
    id: int                      = Retriever(i32,   default = 0)
    terrain_type: int            = Retriever(i32,   default = 0)
    land_avoidance_distance: int = Retriever(i32,   default = 0)
    base_size: int               = Retriever(i32,   default = 0)
    zone: int                    = Retriever(i8,    default = 0)
    placement_type: int          = Retriever(i8,    default = 0)
    _padding1: int               = Retriever(i16,   default = 0)
    x: int                       = Retriever(i32,   default = 0)
    y: int                       = Retriever(i32,   default = 0)
    land_usage_percent: int      = Retriever(i8,    default = 0)
    by_player_mode: int          = Retriever(i8,    default = 0)
    _padding2: int               = Retriever(i16,   default = 0)
    start_area_radius: int       = Retriever(i32,   default = 0)
    terrain_edge_fade: int       = Retriever(i32,   default = 0)
    clumpiness_factor: int       = Retriever(i32,   default = 0)
    # @formatter:on
