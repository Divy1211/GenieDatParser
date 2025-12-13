from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat, set_key
from bfp_rs.types.le import void, f32

from sections.terrain_table_data.terrain_pass_graphic import TerrainPassGraphic


def set_dmg_mult_and_graphics_repeat():
    return [
        set_repeat(ret(TerrainTable.passable_buildable_dmg_mult)).from_key("num_used_terrains"),
        set_repeat(ret(TerrainTable.terrain_pass_graphics)).from_key("num_used_terrains"),
    ]

class TerrainTable(BaseStruct):
    # @formatter:off
    _void                                                 = Retriever(void,                             on_read = set_dmg_mult_and_graphics_repeat, repeat = -2)
    passable_buildable_dmg_mult: list[int]                = Retriever(f32,                              default = 0, repeat = 0)
    terrain_pass_graphics: list[TerrainPassGraphic]       = Retriever(TerrainPassGraphic,               default = 0, repeat = 0)
    # @formatter:on
