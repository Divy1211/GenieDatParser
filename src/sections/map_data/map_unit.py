from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32, int8, int16


class MapUnit(BaseStruct):
    # @formatter:off
    type: int                       = Retriever(int32,  default = 0)
    terrain_type: int               = Retriever(int32,  default = 0)
    group_mode: int                 = Retriever(int8,   default = 0)
    scale_mode: int                 = Retriever(int8,   default = 0)
    _padding1: int                  = Retriever(int16,  default = 0)
    group_size: int                 = Retriever(int32,  default = 0)
    group_size_delta: int           = Retriever(int32,  default = 0)
    num_groups: int                 = Retriever(int32,  default = 0)
    group_radius: int               = Retriever(int32,  default = 0)
    own_at_start: int               = Retriever(int32,  default = 0)
    """aka player_id"""
    set_place_for_all_players: int  = Retriever(int32,  default = 0)
    "aka land_id"
    min_distance_to_players: int    = Retriever(int32,  default = 0)
    max_distance_to_players: int    = Retriever(int32,  default = 0)
    # @formatter:on
