from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner
from bfp_rs.types.le import i32, f32


class TerrainPassGraphic(BaseStruct):
    # @formatter:off
    exit_tile_sprite_id: int          = Retriever(i32,                                                      default = 1)
    enter_tile_sprite_id: int         = Retriever(i32,                                                      default = 1)
    walk_tile_sprite_id: int          = Retriever(i32,                                                      default = 1)
    _replication_amount_de1_aoe2: int = Retriever(i32, min_ver = Version(4, 5), max_ver = Version(5, 7, 2), default = 1)
    walk_sprite_rate: float           = Retriever(f32, min_ver = Version(5, 9), max_ver = Version(5, 9),    default = 1)
    _replication_amount_de2: int      = Retriever(i32, min_ver = Version(7, 7),                             default = 1)

    replication_amount: int           = RetrieverCombiner(_replication_amount_de2, _replication_amount_de1_aoe2)
    # @formatter:on
