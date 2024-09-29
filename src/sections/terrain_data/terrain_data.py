from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import int8, int16, float32, int32, uint16, uint32, uint8, void, Bytes, FixedLenArray

from src.sections.terrain_data.terrain import Terrain
from src.sections.terrain_data.terrain_border import TerrainBorder
from src.sections.terrain_data.tile_size import TileSize


class TerrainData(BaseStruct):
    # @formatter:off
    _vtable_ptr: bytes                  = Retriever(Bytes[4],                                                                                      default = b"\x00" * 4)
    _map_ptr: bytes                     = Retriever(Bytes[4],                                                                                      default = b"\x00" * 4)
    _map_width: int                     = Retriever(int32,                                                                                         default = 0)
    _map_height: int                    = Retriever(int32,                                                                                         default = 0)
    _world_width: int                   = Retriever(int32,                                                                                         default = 0)
    _world_height: int                  = Retriever(int32,                                                                                         default = 0)

    tile_sizes: list[TileSize]          = Retriever(FixedLenArray[TileSize, 19],                                                                   default_factory = TileSize)

    _padding1: int                      = Retriever(int16,                                                                                         default = 0)

    _terrains_aoe1: list[Terrain]       = Retriever(FixedLenArray[Terrain, 32],        min_ver = Version((3, 7)),    max_ver = Version((3, 7)),    default_factory = lambda sv: [Terrain(sv) for _ in range(32)])
    _terrains_de1: list[Terrain]        = Retriever(FixedLenArray[Terrain, 96],        min_ver = Version((4, 5)),    max_ver = Version((4, 5)),    default_factory = lambda sv: [Terrain(sv) for _ in range(96)])
    _terrains_aok: list[Terrain]        = Retriever(FixedLenArray[Terrain, 32],        min_ver = Version((5, 7, 0)), max_ver = Version((5, 7, 0)), default_factory = lambda sv: [Terrain(sv) for _ in range(32)])
    _terrains_aoc: list[Terrain]        = Retriever(FixedLenArray[Terrain, 42],        min_ver = Version((5, 7, 1)), max_ver = Version((5, 7, 1)), default_factory = lambda sv: [Terrain(sv) for _ in range(42)])
    _terrains_hd: list[Terrain]         = Retriever(FixedLenArray[Terrain, 100],       min_ver = Version((5, 7, 2)), max_ver = Version((5, 7, 2)), default_factory = lambda sv: [Terrain(sv) for _ in range(100)])
    _terrains_swgb: list[Terrain]       = Retriever(FixedLenArray[Terrain, 55],        min_ver = Version((5, 9)),    max_ver = Version((5, 9)),    default_factory = lambda sv: [Terrain(sv) for _ in range(55)])
    _terrains_de2: list[Terrain]        = Retriever(FixedLenArray[Terrain, 200],       min_ver = Version((7, 1)),                                  default_factory = lambda sv: [Terrain(sv) for _ in range(200)])

    terrains: list[Terrain]             = RetrieverCombiner(_terrains_de2, _terrains_hd, _terrains_aoc, _terrains_aok, _terrains_de1, _terrains_aoe1, _terrains_swgb)

    terrain_border: list[TerrainBorder] = Retriever(FixedLenArray[TerrainBorder, 16],  min_ver = Version((3, 7)),    max_ver = Version((5, 9)),    default_factory = TerrainBorder)

    # all useless... yES
    _map_row_offset: int                = Retriever(int32,                             min_ver = Version((3, 7)),    max_ver = Version((5, 9)),    default = 0)
    _map_min_x: int                     = Retriever(float32,                           min_ver = Version((5, 7)),                                  default = 0)
    _map_min_y: int                     = Retriever(float32,                           min_ver = Version((5, 7)),                                  default = 0)
    _map_max_x: int                     = Retriever(float32,                           min_ver = Version((5, 7)),                                  default = 0)
    _map_max_y: int                     = Retriever(float32,                           min_ver = Version((5, 7)),                                  default = 0)
    _map_max_x1: int                    = Retriever(float32,                           min_ver = Version((5, 7)),                                  default = 0)
    _map_min_y1: int                    = Retriever(float32,                           min_ver = Version((5, 7)),                                  default = 0)
    _num_additional_terrains: int       = Retriever(uint16,                                                                                        default = 0)
    _borders_used: int                  = Retriever(uint16,                                                                                        default = 0)
    _max_terrain: int                   = Retriever(int16,                                                                                         default = 0)
    _tile_width: int                    = Retriever(int16,                                                                                         default = 0)
    _tile_height: int                   = Retriever(int16,                                                                                         default = 0)
    _tile_half_height: int              = Retriever(int16,                                                                                         default = 0)
    _tile_half_width: int               = Retriever(int16,                                                                                         default = 0)
    _elev_height: int                   = Retriever(int16,                                                                                         default = 0)
    _current_row: int                   = Retriever(int16,                                                                                         default = 0)
    _current_column: int                = Retriever(int16,                                                                                         default = 0)
    _block_begin_row: int               = Retriever(int16,                                                                                         default = 0)
    _block_end_row: int                 = Retriever(int16,                                                                                         default = 0)
    _block_begin_column: int            = Retriever(int16,                                                                                         default = 0)
    _block_end_column: int              = Retriever(int16,                                                                                         default = 0)
    _search_map_ptr: bytes              = Retriever(Bytes[4],                          min_ver = Version((5, 7)),                                  default = b"\x00" * 4)
    _search_map_rows_ptr: bytes         = Retriever(Bytes[4],                          min_ver = Version((5, 7)),                                  default = b"\x00" * 4)
    _any_frame_change_aoe1: int         = Retriever(int32,                                                           max_ver = Version((4, 5)),    default = 0)
    _any_frame_change_aoe2: int         = Retriever(int8,                              min_ver = Version((5, 7)),                                  default = 0)
    _search_map_ptr_aoe1: int           = Retriever(Bytes[4],                                                        max_ver = Version((4, 5)),    default = b"\x00" * 4)
    _search_map_rows_ptr_aoe1: int      = Retriever(Bytes[4],                                                        max_ver = Version((4, 5)),    default = b"\x00" * 4)
    _map_visible_mode: int              = Retriever(int8,                                                                                          default = 0)
    _fog_mode: int                      = Retriever(int8,                                                                                          default = 0)
    _terrain_blob0_swgb: int            = Retriever(FixedLenArray[uint8, 25],          min_ver = Version((5, 9)),    max_ver = Version((5, 9)),    default_factory = lambda _: [0] * 25)
    _terrain_blob1_swgb: int            = Retriever(FixedLenArray[uint32, 157],        min_ver = Version((5, 9)),    max_ver = Version((5, 9)),    default_factory = lambda _: [0] * 157)
    _terrain_blob0_aoe1: int            = Retriever(FixedLenArray[uint8, 2],                                         max_ver = Version((4, 5)),    default_factory = lambda _: [0] * 2)
    _terrain_blob1_aoe1: int            = Retriever(FixedLenArray[uint32, 5],                                        max_ver = Version((4, 5)),    default_factory = lambda _: [0] * 5)
    _terrain_blob0_aoe2: int            = Retriever(FixedLenArray[uint8, 21],          min_ver = Version((5, 7)),    max_ver = Version((5, 7, 2)), default_factory = lambda _: [0] * 21)
    _terrain_blob1_aoe2: int            = Retriever(FixedLenArray[uint32, 157],        min_ver = Version((5, 7)),    max_ver = Version((5, 7, 2)), default_factory = lambda _: [0] * 157)
    # @formatter:on
