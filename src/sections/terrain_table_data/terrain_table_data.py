from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, ret
from bfp_rs.combinators import set_repeat, set_, set_key
from bfp_rs.types.le import u16, Bytes

from sections.terrain_table_data.terrain_table import TerrainTable

def terrain_table_repeats():
    return [
        set_repeat(ret(TerrainTableData._terrain_table_float_ptrs)).from_(TerrainTableData.num_terrain_tables),
        set_repeat(ret(TerrainTableData._terrain_pass_graphic_ptrs)).from_(TerrainTableData.num_terrain_tables),
        set_repeat(ret(TerrainTableData.terrain_tables)).from_(TerrainTableData.num_terrain_tables),
    ]

def sync_num_terrain_tables():
    return [
        set_(ret(TerrainTableData.num_terrain_tables)).from_len(ret(TerrainTableData.terrain_tables)),
    ]

def set_num_used_terrains():
    return [
        set_key("num_used_terrains").from_(TerrainTableData.num_used_terrains),
    ]

class TerrainTableData(BaseStruct):
    # @formatter:off
    num_terrain_tables: int                 = Retriever(u16,                                                                    default = 33,  on_read = terrain_table_repeats, on_write = sync_num_terrain_tables)
    num_used_terrains: int                  = Retriever(u16,                                                                    default = 113, on_read = set_num_used_terrains)
    _terrain_table_float_ptrs: list[bytes]  = Retriever(Bytes[4],                                                               default = b"\x00" * 4,          repeat = 0)
    _terrain_pass_graphic_ptrs: list[bytes] = Retriever(Bytes[4],      min_ver = Version(5, 7),                                 default = b"\x00" * 4,          repeat = 0)
    terrain_tables: list[TerrainTable]      = Retriever(TerrainTable,                                                           default_factory = TerrainTable, repeat = 0)
    # @formatter:on
