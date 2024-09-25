from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int8, int16, float32, int32, uint16, uint32, uint8, Bytes, void

from src.sections.terrain_data.terrain import Terrain
from src.sections.terrain_data.terrain_border import TerrainBorder
from src.sections.terrain_data.tile_size import TileSize


class TerrainData(BaseStruct):
    @staticmethod
    def set_terrain_repeat(_, instance: TerrainData):
        Retriever.set_repeat(TerrainData.terrains, instance, Terrain.num_terrains)

    # @formatter:off
    virt_function_ptr: int          = Retriever(int32,                                                                default = 0)
    map_pointer: int                = Retriever(int32,                                                                default = 0)
    map_width: int                  = Retriever(int32,                                                                default = 0)
    map_height: int                 = Retriever(int32,                                                                default = 0)
    world_width: int                = Retriever(int32,                                                                default = 0)
    world_height: int               = Retriever(int32,                                                                default = 0)
    tile_sizes: TileSize            = Retriever(TileSize,                                                             default_factory = TileSize, repeat = 19)
    padding1: int                   = Retriever(int16,                                                                default = 0)

    _                               = Retriever(void,                                                                 default = b"", on_set = [set_terrain_repeat])
    terrains: Terrain               = Retriever(Terrain,                                                              default_factory = Terrain)
    terrain_border: TerrainBorder   = Retriever(TerrainBorder,  min_ver = Version((3, 7)), max_ver = Version((5, 9)), default_factory = TerrainBorder, repeat = 16)

    map_row_offset: int             = Retriever(int32,          min_ver = Version((3, 7)), max_ver = Version((5, 9)), default=0)

    map_min_x: int                  = Retriever(float32,        min_ver = Version((5, 7)),                            default = 0)
    map_min_y: int                  = Retriever(float32,        min_ver = Version((5, 7)),                            default = 0)
    map_max_x: int                  = Retriever(float32,        min_ver = Version((5, 7)),                            default = 0)
    map_max_y: int                  = Retriever(float32,        min_ver = Version((5, 7)),                            default = 0)
    map_max_xplus1: int             = Retriever(float32,        min_ver = Version((5, 7)),                            default = 0)
    map_min_yplus1: int             = Retriever(float32,        min_ver = Version((5, 7)),                            default = 0)

    terrain_count_additional: int   = Retriever(uint16,                                                               default = 0)
    borders_used: int               = Retriever(uint16,                                                               default = 0)
    max_terrain: int                = Retriever(int16,                                                                default = 0)
    tile_width: int                 = Retriever(int16,                                                                default = 0)
    tile_height: int                = Retriever(int16,                                                                default = 0)
    tile_half_height: int           = Retriever(int16,                                                                default = 0)
    tile_half_width: int            = Retriever(int16,                                                                default = 0)
    elev_height: int                = Retriever(int16,                                                                default = 0)
    current_row: int                = Retriever(int16,                                                                default = 0)
    current_column: int             = Retriever(int16,                                                                default = 0)
    block_beginn_row: int           = Retriever(int16,                                                                default = 0)
    block_end_row: int              = Retriever(int16,                                                                default = 0)
    block_begin_column: int         = Retriever(int16,                                                                default = 0)
    block_end_column: int           = Retriever(int16,                                                                default = 0)

    search_map_ptr: int             = Retriever(int32,          min_ver = Version((5, 7)),                            default = 0)
    search_map_rows_ptr: int        = Retriever(int32,          min_ver = Version((5, 7)),                            default = 0)
    any_frame_change: int           = Retriever(int8,           min_ver = Version((5, 7)),                            default = 0)

    any_frame_change_aoe1: int      = Retriever(int32,          max_ver = Version((4, 5)),                            default = 0)
    search_map_ptr_aoe1: int        = Retriever(int32,          max_ver = Version((4, 5)),                            default = 0)
    search_map_rows_ptr_aoe1: int   = Retriever(int32,          max_ver = Version((4, 5)),                            default = 0)

    map_visible_flag: int           = Retriever(int8,                                                                 default = 0)
    fog_flag: int                   = Retriever(int8,                                                                 default = 0)

    terrain_blob0_swgb: int         = Retriever(uint8,          min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = 0, repeat = 25)
    terrain_blob1_swgb: int         = Retriever(uint32,         min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = 0, repeat = 157)

    terrain_blob0_aoe1: int         = Retriever(uint8,          max_ver = Version((4, 5)),                            default = 0, repeat = 2)
    terrain_blob1_aoe1: int         = Retriever(uint32,         max_ver = Version((4, 5)),                            default = 0, repeat = 5)

    terrain_blob0: int              = Retriever(uint8,          min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = 0, repeat = 21)
    terrain_blob1: int              = Retriever(uint32,         min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = 0, repeat = 157)
    # @formatter:on
