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
    num_terrains: int = -1

    @staticmethod
    def set_borders_repeat(_, instance: Terrain):
        Retriever.set_repeat(Terrain.borders, instance, Terrain.num_terrains)

    # @formatter:off
    enabled: bool                               = Retriever(bool8,                                                                   default = False)
    random: int                                 = Retriever(int8,                                                                    default = 0)

    _is_water_de1: bool                         = Retriever(bool8,             min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = False)
    _hide_in_editor_de1: bool                   = Retriever(bool8,             min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = False)
    _str_id_de1: int                            = Retriever(int32,             min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)

    _is_water_de2: bool                         = Retriever(bool8,             min_ver = Version((7, 1)),                            default = False)
    _hide_in_editor_de2: bool                   = Retriever(bool8,             min_ver = Version((7, 1)),                            default = False)
    _str_id_de2: int                            = Retriever(int32,             min_ver = Version((7, 1)),                            default = 0)

    is_water: bool                              = RetrieverCombiner(_is_water_de2, _is_water_de1)
    hide_in_editor: bool                        = RetrieverCombiner(_hide_in_editor_de2, _hide_in_editor_de1)
    str_id: int                                 = RetrieverCombiner(_str_id_de2, _str_id_de1)

    _blend_priority_de1: int                    = Retriever(int16,             min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    _blend_mode_de1: int                        = Retriever(int16,             min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)

    _str_sign1_de1: int                         = Retriever(Bytes[2],          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = b"\x60\x0A")
    _internal_name_de1: str                     = Retriever(str16,             min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = "")
    _str_sign2_de1: int                         = Retriever(Bytes[2],          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = b"\x60\x0A")
    _slp_filename_de1: str                      = Retriever(str16,             min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = "")

    _str_sign1_de2: int                         = Retriever(Bytes[2],          min_ver = Version((7, 1)),                            default = b"\x60\x0A")
    _internal_name_de2: str                     = Retriever(str16,             min_ver = Version((7, 1)),                            default = "")
    _str_sign2_de2: int                         = Retriever(Bytes[2],          min_ver = Version((7, 1)),                            default = b"\x60\x0A")
    _slp_filename_de2: str                      = Retriever(str16,             min_ver = Version((7, 1)),                            default = "")

    _internal_name_aoe1: str                    = Retriever(FixedLenNTStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = "")
    _slp_filename_aoe1: str                     = Retriever(FixedLenNTStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = "")

    _internal_name_aoe2: str                    = Retriever(FixedLenNTStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = "")
    _slp_filename_aoe2: str                     = Retriever(FixedLenNTStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = "")

    _internal_name_swgb: str                    = Retriever(FixedLenNTStr[17], min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = "")
    _slp_filename_swgb: str                     = Retriever(FixedLenNTStr[17], min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = "")

    internal_name: str                          = RetrieverCombiner(_internal_name_de2, _internal_name_aoe2, _internal_name_de1, _internal_name_aoe1, _internal_name_swgb)
    slp_filename: str                           = RetrieverCombiner(_slp_filename_de2, _slp_filename_aoe2, _slp_filename_de1, _slp_filename_aoe1, _slp_filename_swgb)

    slp_id: int                                 = Retriever(int32,                                                                   default = 0)
    _slp_ptr: bytes                             = Retriever(Bytes[4],                                                                default = b"\x00" * 4)
    sound_id: int                               = Retriever(int32,                                                                   default = 0)

    wwise_sound_id: int                         = Retriever(uint32,            min_ver = Version((7, 1)),                            default = 0)
    wwise_stop_sound_id: int                    = Retriever(uint32,            min_ver = Version((7, 1)),                            default = 0)

    _blend_priority_aoe2: int                   = Retriever(int32,             min_ver = Version((5, 7)),                            default = 0)
    _blend_mode_aoe2: int                       = Retriever(int32,             min_ver = Version((5, 7)),                            default = 0)

    blend_priority: int                         = RetrieverCombiner(_blend_priority_aoe2, _blend_priority_de1)
    blend_mode: int                             = RetrieverCombiner(_blend_mode_aoe2, _blend_mode_de1)

    _str_sign3_de2: bytes                       = Retriever(Bytes[2],          min_ver = Version((7, 1)),                            default = b"\x60\x0A")
    overlay_mask_name: str                      = Retriever(str16,             min_ver = Version((7, 1)),                            default = "")

    map_color_high: int                         = Retriever(uint8,                                                                   default = 0)
    map_color_medium: int                       = Retriever(uint8,                                                                   default = 0)
    map_color_low: int                          = Retriever(uint8,                                                                   default = 0)
    map_color_cliff_left: int                   = Retriever(uint8,                                                                   default = 0)
    map_color_cliff_right: int                  = Retriever(uint8,                                                                   default = 0)
    passable_terrain: int                       = Retriever(int8,                                                                    default = 0)
    impassable_terrain: int                     = Retriever(int8,                                                                    default = 0)

    animation: TerrainAnimation                 = Retriever(TerrainAnimation,                                                        default_factory = TerrainAnimation)
    elevation_sprites: list[TerrainSpriteFrame] = Retriever(FixedLenArray[TerrainSpriteFrame, 19],                                   default_factory = lambda sv: [TerrainSpriteFrame(sv) for _ in range(19)])

    terrain_to_draw: int                        = Retriever(int16,                                                                   default = 0)
    rows: int                                   = Retriever(int16,                                                                   default = 0)
    cols: int                                   = Retriever(int16,                                                                   default = 0)

    _void: bytes                                = Retriever(void,              min_ver = Version((3, 7)), max_ver = Version((5, 9)), default = b"", on_set = [set_borders_repeat])
    borders: list[int]                          = Retriever(int16,             min_ver = Version((3, 7)), max_ver = Version((5, 9)), default = 0, repeat = 200) # todo: fixed len array based on version

    units: list[TerrainUnit]                    = Retriever(StackedAttrArray8[TerrainUnit, 30],                                      default_factory = lambda sv: [TerrainUnit(sv) for _ in range(30)])
    num_units_used: int                         = Retriever(int16,                                                                   default = 0)

    _phantom_aoe1_de1_aoe2: int                 = Retriever(int16,             min_ver = Version((3, 7)), max_ver = Version((5, 7)), default = 0)
    _phantom_de2: int                           = Retriever(int16,             min_ver = Version((7, 1)),                            default = 0)

    phantom: int                                = RetrieverCombiner(_phantom_de2, _phantom_aoe1_de1_aoe2)
    # @formatter:on
