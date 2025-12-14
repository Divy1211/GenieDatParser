from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner
from bfp_rs.types.le import (
    i8, i32, i16, str16, u32, u8, NtStr, Bytes, bool8, Array, StackedAttrArray
)

from sections.terrain_data.terrain_sprite_frame import TerrainSpriteFrame
from sections.terrain_data.terrain_animation import TerrainAnimation
from sections.terrain_data.terrain_unit import TerrainUnit


class Terrain(BaseStruct):
    # @formatter:off
    enabled: bool                               = Retriever(bool8,                                                                    default = True)
    random: int                                 = Retriever(i8,                                                                       default = 0)

    _type_de1: int                              = Retriever(i8,        min_ver = Version(4, 5), max_ver = Version(4, 5),              default = 0)
    _hide_in_editor_de1: int                    = Retriever(bool8,     min_ver = Version(4, 5), max_ver = Version(4, 5),              default = False)
    _str_id_de1: int                            = Retriever(i32,       min_ver = Version(4, 5), max_ver = Version(4, 5),              default = 0)

    _type_de2: int                              = Retriever(i8,        min_ver = Version(7, 1),                                       default = 0)
    _hide_in_editor_de2: int                    = Retriever(bool8,     min_ver = Version(7, 1),                                       default = False)
    _str_id_de2: int                            = Retriever(i32,       min_ver = Version(7, 1),                                       default = 0)

    type: int                                   = RetrieverCombiner(_type_de2, _type_de1)
    hide_in_editor: int                         = RetrieverCombiner(_hide_in_editor_de2, _hide_in_editor_de1)
    str_id: int                                 = RetrieverCombiner(_str_id_de2, _str_id_de1)

    _blend_priority_de1: int                    = Retriever(i16,       min_ver = Version(4, 5), max_ver = Version(4, 5),              default = 0)
    _blend_mode_de1: int                        = Retriever(i16,       min_ver = Version(4, 5), max_ver = Version(4, 5),              default = 0)

    _str_sign1_de1: int                         = Retriever(Bytes[2],  min_ver = Version(4, 5), max_ver = Version(4, 5),              default = b"\x0A\x60")
    _internal_name_de1: str                     = Retriever(str16,     min_ver = Version(4, 5), max_ver = Version(4, 5),              default = "")
    _str_sign2_de1: int                         = Retriever(Bytes[2],  min_ver = Version(4, 5), max_ver = Version(4, 5),              default = b"\x0A\x60")
    _slp_filename_de1: str                      = Retriever(str16,     min_ver = Version(4, 5), max_ver = Version(4, 5),              default = "")

    _str_sign1_de2: int                         = Retriever(Bytes[2],  min_ver = Version(7, 1),                                       default = b"\x0A\x60")
    _internal_name_de2: str                     = Retriever(str16,     min_ver = Version(7, 1),                                       default = "")
    _str_sign2_de2: int                         = Retriever(Bytes[2],  min_ver = Version(7, 1),                                       default = b"\x0A\x60")
    _slp_filename_de2: str                      = Retriever(str16,     min_ver = Version(7, 1),                                       default = "")

    _internal_name_aoe1: str                    = Retriever(NtStr[13], min_ver = Version(3, 7), max_ver = Version(3, 7),              default = "")
    _slp_filename_aoe1: str                     = Retriever(NtStr[13], min_ver = Version(3, 7), max_ver = Version(3, 7),              default = "")

    _internal_name_aoe2: str                    = Retriever(NtStr[13], min_ver = Version(5, 7), max_ver = Version(5, 7, 2),           default = "")
    _slp_filename_aoe2: str                     = Retriever(NtStr[13], min_ver = Version(5, 7), max_ver = Version(5, 7, 2),           default = "")

    _internal_name_swgb: str                    = Retriever(NtStr[17], min_ver = Version(5, 9), max_ver = Version(5, 9),              default = "")
    _slp_filename_swgb: str                     = Retriever(NtStr[17], min_ver = Version(5, 9), max_ver = Version(5, 9),              default = "")

    internal_name: str                          = RetrieverCombiner(_internal_name_de2, _internal_name_aoe2, _internal_name_de1, _internal_name_aoe1, _internal_name_swgb)
    slp_filename: str                           = RetrieverCombiner(_slp_filename_de2, _slp_filename_aoe2, _slp_filename_de1, _slp_filename_aoe1, _slp_filename_swgb)

    slp_id: int                                 = Retriever(i32,                                                                      default = 0)
    _slp_ptr: bytes                             = Retriever(Bytes[4],                                                                 default = b"\x00" * 4)
    sound_id: int                               = Retriever(i32,                                                                      default = 0)

    wwise_sound_id: int                         = Retriever(u32,       min_ver = Version(7, 1),                                       default = 0)
    wwise_stop_sound_id: int                    = Retriever(u32,       min_ver = Version(7, 1),                                       default = 0)

    _blend_priority_aoe2: int                   = Retriever(i32,       min_ver = Version(5, 7),                                       default = 0)
    _blend_mode_aoe2: int                       = Retriever(i32,       min_ver = Version(5, 7),                                       default = 0)

    blend_priority: int                         = RetrieverCombiner(_blend_priority_aoe2, _blend_priority_de1)
    blend_mode: int                             = RetrieverCombiner(_blend_mode_aoe2, _blend_mode_de1)

    _str_sign3_de2: bytes                       = Retriever(Bytes[2], min_ver = Version(7, 1),                                        default = b"\x0A\x60")
    overlay_mask_name: str                      = Retriever(str16,    min_ver = Version(7, 1),                                        default = "")

    map_color_high: int                         = Retriever(u8,                                                                       default = 0)
    map_color_medium: int                       = Retriever(u8,                                                                       default = 0)
    map_color_low: int                          = Retriever(u8,                                                                       default = 0)
    map_color_cliff_left: int                   = Retriever(u8,                                                                       default = 0)
    map_color_cliff_right: int                  = Retriever(u8,                                                                       default = 0)
    passable_terrain: int                       = Retriever(i8,                                                                       default = 0)
    impassable_terrain: int                     = Retriever(i8,                                                                       default = 0)

    animation: TerrainAnimation                 = Retriever(TerrainAnimation,                                                         default_factory = TerrainAnimation)
    elevation_sprites: list[TerrainSpriteFrame] = Retriever(Array[19][TerrainSpriteFrame],                                            default_factory = lambda ver: [TerrainSpriteFrame(ver) for _ in range(19)])

    terrain_to_draw: int                        = Retriever(i16,                                                                      default = 0)
    rows: int                                   = Retriever(i16,                                                                      default = 0)
    cols: int                                   = Retriever(i16,                                                                      default = 0)

    _borders_aoe1: list[int]                    = Retriever(Array[32][i16],  min_ver = Version(3, 7),    max_ver = Version(3, 7),     default_factory = lambda _ver: [0] * 32)
    _borders_de1: list[int]                     = Retriever(Array[96][i16],  min_ver = Version(4, 5),    max_ver = Version(4, 5),     default_factory = lambda _ver: [0] * 96)
    _borders_aok: list[int]                     = Retriever(Array[32][i16],  min_ver = Version(5, 7, 0), max_ver = Version(5, 7, 0),  default_factory = lambda _ver: [0] * 32)
    _borders_aoc: list[int]                     = Retriever(Array[42][i16],  min_ver = Version(5, 7, 1), max_ver = Version(5, 7, 1),  default_factory = lambda _ver: [0] * 42)
    _borders_hd: list[int]                      = Retriever(Array[100][i16], min_ver = Version(5, 7, 2), max_ver = Version(5, 7, 2),  default_factory = lambda _ver: [0] * 100)
    _borders_swgb: list[int]                    = Retriever(Array[55][i16],  min_ver = Version(5, 9),    max_ver = Version(5, 9),     default_factory = lambda _ver: [0] * 55)

    borders: list[int]                          = RetrieverCombiner(_borders_hd, _borders_aoc, _borders_aok, _borders_de1, _borders_aoe1, _borders_swgb)

    units: list[TerrainUnit]                    = Retriever(StackedAttrArray[30][TerrainUnit],                                        default_factory = lambda ver: [TerrainUnit(ver) for _ in range(30)])
    num_units_used: int                         = Retriever(i16,                                                                      default = 0)

    _phantom_aoe1_de1_aoe2: int                 = Retriever(i16,             min_ver = Version(3, 7),    max_ver = Version(5, 7, 2),  default = 0)
    _phantom_de2: int                           = Retriever(i16,             min_ver = Version(7, 1),                                 default = 0)

    phantom: int                                = RetrieverCombiner(_phantom_de2, _phantom_aoe1_de1_aoe2)
    # @formatter:on
