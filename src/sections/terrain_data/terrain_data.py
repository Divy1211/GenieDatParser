from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner
from bfp_rs.types.le import i8, i16, f32, i32, u16, u32, u8, Bytes, Array

from sections.terrain_data.terrain import Terrain
from sections.terrain_data.terrain_border import TerrainBorder
from sections.terrain_data.tile_size import TileSize


class TerrainData(BaseStruct):
    # @formatter:off
    _vtable_ptr: bytes                  = Retriever(Bytes[4],                                                                          default = b"\x00" * 4)
    _map_ptr: bytes                     = Retriever(Bytes[4],                                                                          default = b"\x00" * 4)
    _map_width: int                     = Retriever(i32,                                                                               default = 0)
    _map_height: int                    = Retriever(i32,                                                                               default = 0)
    _world_width: int                   = Retriever(i32,                                                                               default = 0)
    _world_height: int                  = Retriever(i32,                                                                               default = 0)

    tile_sizes: list[TileSize]          = Retriever(Array[19][TileSize],                                                               default_factory = TileSize)

    _padding1: int                      = Retriever(i16,                                                                               default = 0)

    _terrains_aoe1: list[Terrain]       = Retriever(Array[32][Terrain],        min_ver = Version(3, 7),    max_ver = Version(3, 7),    default_factory = lambda ver: [Terrain(ver) for _ in range(32)])
    _terrains_de1: list[Terrain]        = Retriever(Array[96][Terrain],        min_ver = Version(4, 5),    max_ver = Version(4, 5),    default_factory = lambda ver: [Terrain(ver) for _ in range(96)])
    _terrains_aok: list[Terrain]        = Retriever(Array[32][Terrain],        min_ver = Version(5, 7, 0), max_ver = Version(5, 7, 0), default_factory = lambda ver: [Terrain(ver) for _ in range(32)])
    _terrains_aoc: list[Terrain]        = Retriever(Array[42][Terrain],        min_ver = Version(5, 7, 1), max_ver = Version(5, 7, 1), default_factory = lambda ver: [Terrain(ver) for _ in range(42)])
    _terrains_hd: list[Terrain]         = Retriever(Array[100][Terrain],       min_ver = Version(5, 7, 2), max_ver = Version(5, 7, 2), default_factory = lambda ver: [Terrain(ver) for _ in range(100)])
    _terrains_swgb: list[Terrain]       = Retriever(Array[55][Terrain],        min_ver = Version(5, 9),    max_ver = Version(5, 9),    default_factory = lambda ver: [Terrain(ver) for _ in range(55)])
    _terrains_de2: list[Terrain]        = Retriever(Array[200][Terrain],       min_ver = Version(7, 1),                                default_factory = lambda ver: [Terrain(ver) for _ in range(200)])

    terrains: list[Terrain]             = RetrieverCombiner(_terrains_de2, _terrains_hd, _terrains_aoc, _terrains_aok, _terrains_de1, _terrains_aoe1, _terrains_swgb)

    terrain_border: list[TerrainBorder] = Retriever(Array[16][TerrainBorder],  min_ver = Version(3, 7),    max_ver = Version(5, 9),    default_factory = TerrainBorder)

    # all useless... yES
    _map_row_offset: int                = Retriever(i32,             min_ver = Version(3, 7),    max_ver = Version(5, 9), default = 0)
    _map_min_x: int                     = Retriever(f32,             min_ver = Version(5, 7),                             default = 0)
    _map_min_y: int                     = Retriever(f32,             min_ver = Version(5, 7),                             default = 0)
    _map_max_x: int                     = Retriever(f32,             min_ver = Version(5, 7),                             default = 0)
    _map_max_y: int                     = Retriever(f32,             min_ver = Version(5, 7),                             default = 0)
    _map_max_x1: int                    = Retriever(f32,             min_ver = Version(5, 7),                             default = 0)
    _map_min_y1: int                    = Retriever(f32,             min_ver = Version(5, 7),                             default = 0)
    _num_additional_terrains: int       = Retriever(u16,                                                                  default = 0)
    _borders_used: int                  = Retriever(u16,                                                                  default = 0)
    _max_terrain: int                   = Retriever(i16,                                                                  default = 0)
    _tile_width: int                    = Retriever(i16,                                                                  default = 0)
    _tile_height: int                   = Retriever(i16,                                                                  default = 0)
    _tile_half_height: int              = Retriever(i16,                                                                  default = 0)
    _tile_half_width: int               = Retriever(i16,                                                                  default = 0)
    _elev_height: int                   = Retriever(i16,                                                                  default = 0)
    _current_row: int                   = Retriever(i16,                                                                  default = 0)
    _current_column: int                = Retriever(i16,                                                                  default = 0)
    _block_begin_row: int               = Retriever(i16,                                                                  default = 0)
    _block_end_row: int                 = Retriever(i16,                                                                  default = 0)
    _block_begin_column: int            = Retriever(i16,                                                                  default = 0)
    _block_end_column: int              = Retriever(i16,                                                                  default = 0)
    _search_map_ptr: bytes              = Retriever(Bytes[4],        min_ver = Version(5, 7),                             default = b"\x00" * 4)
    _search_map_rows_ptr: bytes         = Retriever(Bytes[4],        min_ver = Version(5, 7),                             default = b"\x00" * 4)
    _any_frame_change_aoe1: int         = Retriever(i32,             max_ver = Version(4, 5),                             default = 0)
    _any_frame_change_aoe2: int         = Retriever(i8,              min_ver = Version(5, 7),                             default = 0)
    _search_map_ptr_aoe1: int           = Retriever(Bytes[4],                                 max_ver = Version(4, 5),    default = b"\x00" * 4)
    _search_map_rows_ptr_aoe1: int      = Retriever(Bytes[4],                                 max_ver = Version(4, 5),    default = b"\x00" * 4)
    _map_visible_mode: int              = Retriever(i8,                                                                   default = 0)
    _fog_mode: int                      = Retriever(i8,                                                                   default = 0)
    _terrain_blob0_swgb: int            = Retriever(Array[25][u8],   min_ver = Version(5, 9), max_ver = Version(5, 9),    default_factory = lambda _ver: [0] * 25)
    _terrain_blob1_swgb: int            = Retriever(Array[157][u32], min_ver = Version(5, 9), max_ver = Version(5, 9),    default_factory = lambda _ver: [0] * 157)
    _terrain_blob0_aoe1: int            = Retriever(Array[2][u8],    max_ver = Version(4, 5),                             default_factory = lambda _ver: [0] * 2)
    _terrain_blob1_aoe1: int            = Retriever(Array[5][u32],   max_ver = Version(4, 5),                             default_factory = lambda _ver: [0] * 5)
    _terrain_blob0_aoe2: int            = Retriever(Array[21][u8],   min_ver = Version(5, 7), max_ver = Version(5, 7, 2), default_factory = lambda _ver: [0] * 21)
    _terrain_blob1_aoe2: int            = Retriever(Array[157][u32], min_ver = Version(5, 7), max_ver = Version(5, 7, 2), default_factory = lambda _ver: [0] * 157)
    # @formatter:on
