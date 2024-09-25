from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint16, Bytes

from src.sections.terrain_table_data.terrain_table import TerrainTable

class TerrainTableData(BaseStruct):
    @staticmethod
    def set_terrain_table_repeats(_, instance: TerrainTableData):
        Retriever.set_repeat(TerrainTableData._terrain_table_float_ptrs, instance, instance.num_terrain_tables) # type: ignore
        Retriever.set_repeat(TerrainTableData._terrain_pass_graphic_ptrs, instance, instance.num_terrain_tables) # type: ignore
        Retriever.set_repeat(TerrainTableData.terrain_tables, instance, instance.num_terrain_tables) # type: ignore

    @staticmethod
    def sync_terrain_table_repeats(_, instance: TerrainTableData):
        if (
            len(instance._terrain_table_float_ptrs)
            == len(instance._terrain_table_float_ptrs)
            == (n := len(instance.terrain_tables))
        ):
            instance.num_terrain_tables = n
            return
        raise ValueError("xxx_ptrs and terrain_table lists have unequal lengths")

    @staticmethod
    def set_num_used_terrains(_, instance: TerrainTableData):
        TerrainTable.num_used_terrains = instance.num_used_terrains

    @staticmethod
    def sync_num_used_terrains(_, instance: TerrainTableData):
        num_terrains = None
        for i, table in enumerate(instance.terrain_tables):
            if (
                (n := len(table.terrain_pass_graphics)) != len(table.passable_buildable_dmg_mult)
            ):
                ValueError(f"TerrainTable '{i}' has unequal lists")
            if num_terrains is None:
                num_terrains = n
            elif num_terrains != n:
                ValueError(f"Different TerrainTables have unequal number of terrains")

    num_terrain_tables: int                 = Retriever(uint16,                                                                 default = 33, on_read = [set_terrain_table_repeats], on_write = [sync_terrain_table_repeats])
    num_used_terrains: int                  = Retriever(uint16,                                                                 default = 113, on_read = [set_num_used_terrains], on_write = [sync_num_used_terrains])
    _terrain_table_float_ptrs: list[bytes]  = Retriever(Bytes[4],                                                               default = b"\x00" * 4)
    _terrain_pass_graphic_ptrs: list[bytes] = Retriever(Bytes[4],      min_ver = Version((5, 7)),                               default = b"\x00" * 4)
    terrain_tables: list[TerrainTable]      = Retriever(TerrainTable,                                                           default_factory = TerrainTable)
