from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import (
    int8, int32, int16, str16, uint32, uint8, bool8, void,
    FixedLenNTStr, Bytes, FixedLenArray, StackedAttrArray8
)

from src.sections.terrain_data.terrain_sprite_frame import TerrainSpriteFrame
from src.sections.terrain_data.terrain_animation import TerrainAnimation
from src.sections.terrain_data.terrain_unit import TerrainUnit


class Terrain(BaseStruct):
    # @formatter:off
    enabled: bool                               = Retriever(bool8,                                                                      default = True)
    random: int                                 = Retriever(int8,                                                                       default = 0)

    _type_de1: int                              = Retriever(int8,             min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = False)
    _hide_in_editor_de1: bool                   = Retriever(bool8,             min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = False)
    _str_id_de1: int                            = Retriever(int32,             min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = 0)

    _type_de2: int                              = Retriever(int8,             min_ver = Version((7, 1)),                               default = False)
    _hide_in_editor_de2: bool                   = Retriever(bool8,             min_ver = Version((7, 1)),                               default = False)
    _str_id_de2: int                            = Retriever(int32,             min_ver = Version((7, 1)),                               default = 0)

    type: int                                   = RetrieverCombiner(_type_de2, _type_de1)
    hide_in_editor: bool                        = RetrieverCombiner(_hide_in_editor_de2, _hide_in_editor_de1)
    str_id: int                                 = RetrieverCombiner(_str_id_de2, _str_id_de1)

    _blend_priority_de1: int                    = Retriever(int16,             min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = 0)
    _blend_mode_de1: int                        = Retriever(int16,             min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = 0)

    _str_sign1_de1: int                         = Retriever(Bytes[2],          min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = b"\x60\x0A")
    _internal_name_de1: str                     = Retriever(str16,             min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = "")
    _str_sign2_de1: int                         = Retriever(Bytes[2],          min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = b"\x60\x0A")
    _slp_filename_de1: str                      = Retriever(str16,             min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = "")

    _str_sign1_de2: int                         = Retriever(Bytes[2],          min_ver = Version((7, 1)),                               default = b"\x60\x0A")
    _internal_name_de2: str                     = Retriever(str16,             min_ver = Version((7, 1)),                               default = "")
    _str_sign2_de2: int                         = Retriever(Bytes[2],          min_ver = Version((7, 1)),                               default = b"\x60\x0A")
    _slp_filename_de2: str                      = Retriever(str16,             min_ver = Version((7, 1)),                               default = "")

    _internal_name_aoe1: str                    = Retriever(FixedLenNTStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)),    default = "")
    _slp_filename_aoe1: str                     = Retriever(FixedLenNTStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)),    default = "")

    _internal_name_aoe2: str                    = Retriever(FixedLenNTStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7, 2)), default = "")
    _slp_filename_aoe2: str                     = Retriever(FixedLenNTStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7, 2)), default = "")

    _internal_name_swgb: str                    = Retriever(FixedLenNTStr[17], min_ver = Version((5, 9)), max_ver = Version((5, 9)),    default = "")
    _slp_filename_swgb: str                     = Retriever(FixedLenNTStr[17], min_ver = Version((5, 9)), max_ver = Version((5, 9)),    default = "")

    internal_name: str                          = RetrieverCombiner(_internal_name_de2, _internal_name_aoe2, _internal_name_de1, _internal_name_aoe1, _internal_name_swgb)
    slp_filename: str                           = RetrieverCombiner(_slp_filename_de2, _slp_filename_aoe2, _slp_filename_de1, _slp_filename_aoe1, _slp_filename_swgb)

    slp_id: int                                 = Retriever(int32,                                                                      default = 0)
    _slp_ptr: bytes                             = Retriever(Bytes[4],                                                                   default = b"\x00" * 4)
    sound_id: int                               = Retriever(int32,                                                                      default = 0)

    wwise_sound_id: int                         = Retriever(uint32,            min_ver = Version((7, 1)),                               default = 0)
    wwise_stop_sound_id: int                    = Retriever(uint32,            min_ver = Version((7, 1)),                               default = 0)

    _blend_priority_aoe2: int                   = Retriever(int32,             min_ver = Version((5, 7)),                               default = 0)
    _blend_mode_aoe2: int                       = Retriever(int32,             min_ver = Version((5, 7)),                               default = 0)

    blend_priority: int                         = RetrieverCombiner(_blend_priority_aoe2, _blend_priority_de1)
    blend_mode: int                             = RetrieverCombiner(_blend_mode_aoe2, _blend_mode_de1)

    _str_sign3_de2: bytes                       = Retriever(Bytes[2],          min_ver = Version((7, 1)),                               default = b"\x60\x0A")
    overlay_mask_name: str                      = Retriever(str16,             min_ver = Version((7, 1)),                               default = "")

    map_color_high: int                         = Retriever(uint8,                                                                      default = 0)
    map_color_medium: int                       = Retriever(uint8,                                                                      default = 0)
    map_color_low: int                          = Retriever(uint8,                                                                      default = 0)
    map_color_cliff_left: int                   = Retriever(uint8,                                                                      default = 0)
    map_color_cliff_right: int                  = Retriever(uint8,                                                                      default = 0)
    passable_terrain: int                       = Retriever(int8,                                                                       default = 0)
    impassable_terrain: int                     = Retriever(int8,                                                                       default = 0)

    animation: TerrainAnimation                 = Retriever(TerrainAnimation,                                                           default_factory = TerrainAnimation)
    elevation_sprites: list[TerrainSpriteFrame] = Retriever(FixedLenArray[TerrainSpriteFrame, 19],                                      default_factory = lambda sv: [TerrainSpriteFrame(sv) for _ in range(19)])

    terrain_to_draw: int                        = Retriever(int16,                                                                      default = 0)
    rows: int                                   = Retriever(int16,                                                                      default = 0)
    cols: int                                   = Retriever(int16,                                                                      default = 0)

    _borders_aoe1: list[int]                    = Retriever(FixedLenArray[int16, 32],   min_ver = Version((3, 7)),    max_ver = Version((3, 7)),    default_factory = lambda _: [0] * 32)
    _borders_de1: list[int]                     = Retriever(FixedLenArray[int16, 96],   min_ver = Version((4, 5)),    max_ver = Version((4, 5)),    default_factory = lambda _: [0] * 96)
    _borders_aok: list[int]                     = Retriever(FixedLenArray[int16, 32],   min_ver = Version((5, 7, 0)), max_ver = Version((5, 7, 0)), default_factory = lambda _: [0] * 32)
    _borders_aoc: list[int]                     = Retriever(FixedLenArray[int16, 42],   min_ver = Version((5, 7, 1)), max_ver = Version((5, 7, 1)), default_factory = lambda _: [0] * 42)
    _borders_hd: list[int]                      = Retriever(FixedLenArray[int16, 100],  min_ver = Version((5, 7, 2)), max_ver = Version((5, 7, 2)), default_factory = lambda _: [0] * 100)
    _borders_swgb: list[int]                    = Retriever(FixedLenArray[int16, 55],   min_ver = Version((5, 9)),    max_ver = Version((5, 9)),    default_factory = lambda _: [0] * 55)

    borders: list[int]                          = RetrieverCombiner(_borders_hd, _borders_aoc, _borders_aok, _borders_de1, _borders_aoe1, _borders_swgb)

    units: list[TerrainUnit]                    = Retriever(StackedAttrArray8[TerrainUnit, 30],                                                     default_factory = lambda sv: [TerrainUnit(sv) for _ in range(30)])
    num_units_used: int                         = Retriever(int16,                                                                                  default = 0)

    _phantom_aoe1_de1_aoe2: int                 = Retriever(int16,                      min_ver = Version((3, 7)),    max_ver = Version((5, 7, 2)), default = 0)
    _phantom_de2: int                           = Retriever(int16,                      min_ver = Version((7, 1)),                                  default = 0)

    phantom: int                                = RetrieverCombiner(_phantom_de2, _phantom_aoe1_de1_aoe2)
    # @formatter:on
