from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32, i8, i16


class MapUnit(BaseStruct):
    # @formatter:off
    type: int                       = Retriever(i32,  default = 0)
    terrain_type: int               = Retriever(i32,  default = 0)
    group_mode: int                 = Retriever(i8,   default = 0)
    scale_mode: int                 = Retriever(i8,   default = 0)
    _padding1: int                  = Retriever(i16,  default = 0)
    group_size: int                 = Retriever(i32,  default = 0)
    group_size_delta: int           = Retriever(i32,  default = 0)
    num_groups: int                 = Retriever(i32,  default = 0)
    group_radius: int               = Retriever(i32,  default = 0)
    own_at_start: int               = Retriever(i32,  default = 0)
    """aka player_id"""
    set_place_for_all_players: int  = Retriever(i32,  default = 0)
    "aka land_id"
    min_distance_to_players: int    = Retriever(i32,  default = 0)
    max_distance_to_players: int    = Retriever(i32,  default = 0)
    # @formatter:on
