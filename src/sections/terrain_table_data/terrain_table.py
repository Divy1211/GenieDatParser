from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import void, float32

from src.sections.terrain_table_data.terrain_pass_graphic import TerrainPassGraphic


class TerrainTable(BaseStruct):
    num_used_terrains: int = 0

    @staticmethod
    def set_repeat(_, instance: TerrainTable):
        Retriever.set_repeat(TerrainTable.passable_buildable_dmg_mult, instance, TerrainTable.num_used_terrains)
        Retriever.set_repeat(TerrainTable.terrain_pass_graphics, instance, TerrainTable.num_used_terrains)

    # @formatter:off
    _void                                                 = Retriever(void,                             on_read = [set_repeat])
    passable_buildable_dmg_mult: list[int]                = Retriever(float32,            default = 0, repeat = 0)
    terrain_pass_graphics: list[TerrainPassGraphic]       = Retriever(TerrainPassGraphic, default = 0, repeat = 0)
    # @formatter:on
