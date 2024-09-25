from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int8, int32, int16, uint16, str16, FixedLenStr, uint32, uint8, Bytes

from src.sections.terrain_data.frame_data import FrameData
from src.sections.terrain_data.terrain_animation import TerrainAnimation


class Terrain(BaseStruct):
    num_terrains: int = -1

    @staticmethod
    def set_terrain_repeat(_, instance: Terrain):
        Retriever.set_repeat(Terrain.borders, instance, Terrain.num_terrains)

    # @formatter:off
    enabled: int                            = Retriever(int8,                                                                  default = 0)
    random: int                             = Retriever(int8,                                                                  default = 0)
    is_water_AOE1DE: int                    = Retriever(int8,            min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    hide_in_editor_AOE1DE: int              = Retriever(int8,            min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    string_id_AOE1DE: int                   = Retriever(int32,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    is_water_AOE2DE: int                    = Retriever(int8,            min_ver = Version((7, 1)),                            default = 0)
    hide_in_editor_AOE2DE: int              = Retriever(int8,            min_ver = Version((7, 1)),                            default = 0)
    string_id_AOE2DE: int                   = Retriever(int32,           min_ver = Version((7, 1)),                            default = 0)
    blend_priority_de_AOE1DE: int           = Retriever(int16,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    blend_type_de_AOE1DE: int               = Retriever(int16,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    internal_name_len_debug_AOE1DE: int     = Retriever(uint16,          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    internal_name_AOE1DE: str               = Retriever(str16,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    filename_len_debug_AOE1DE: int          = Retriever(uint16,          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    filename_AOE1DE: str                    = Retriever(str16,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    internal_name_len_debug_AOE2DE: int     = Retriever(uint16,          min_ver = Version((7, 1)),                            default = 0)
    internal_name_AOE2DE: str               = Retriever(str16,           min_ver = Version((7, 1)),                            default = 0)
    filename_len_debug_AOE2DE: int          = Retriever(uint16,          min_ver = Version((7, 1)),                            default = 0)
    filename_AOE2DE: str                    = Retriever(str16,           min_ver = Version((7, 1)),                            default = 0)

    internal_name_AOE1: str                 = Retriever(FixedLenStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = 0)
    filename_AOE1: str                      = Retriever(FixedLenStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = 0)
    internal_name_HD: str                   = Retriever(FixedLenStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = 0)
    filename_HD: str                        = Retriever(FixedLenStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = 0)
    internal_name_SWGB: str                 = Retriever(FixedLenStr[17], min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = 0)
    filename_SWGB: str                      = Retriever(FixedLenStr[17], min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = 0)
    internal_name_AOE2DE: str               = Retriever(str16,           min_ver = Version((7, 1)),                            default = 0)
    filename_AOE2DE: str                    = Retriever(str16,           min_ver = Version((7, 1)),                            default = 0)

    slp_id: int                             = Retriever(int32,                                                                 default = 0)
    shape_ptr: int                          = Retriever(int32,                                                                 default = 0)
    sound_id: int                           = Retriever(int32,                                                                 default = 0)

    wwise_sound_id_AOE2DE: int              = Retriever(uint32,          min_ver = Version((7, 1)),                            default = 0)
    wwise_stop_sound_id_AOE2DE: int         = Retriever(uint32,          min_ver = Version((7, 1)),                            default = 0)


    blend_priority: int                     = Retriever(int32,           min_ver = Version((5, 7)),                            default = 0)
    blend_mode: int                         = Retriever(int32,           min_ver = Version((5, 7)),                            default = 0)

    overlay_mask_name_len_debug:  int       = Retriever(uint16,          min_ver = Version((7, 1)),                            default = 0)
    overlay_mask_name: int                  = Retriever(str16,           min_ver = Version((7, 1)),                            default = 0)

    map_color_hi: int                       = Retriever(uint8,                                                                 default = 0)
    map_color_med: int                      = Retriever(uint8,                                                                 default = 0)
    map_color_low: int                      = Retriever(uint8,                                                                 default = 0)
    map_color_cliff_lt: int                 = Retriever(uint8,                                                                 default = 0)
    map_color_cliff_rt: int                 = Retriever(uint8,                                                                 default = 0)
    passable_terrain: int                   = Retriever(int8,                                                                  default = 0)
    impassable_terrain: int                 = Retriever(int8,                                                                  default = 0)

    terrain_animation: TerrainAnimation     = Retriever(TerrainAnimation,                                                      default_factory = TerrainAnimation)
    elevation_graphics: FrameData           = Retriever(FrameData,                                                             default_factory = FrameData, repeat = 19)

    terrain_replacement_id: int             = Retriever(int16,                                                                 default = 0)
    terrain_to_draw0: int                   = Retriever(int16,                                                                 default = 0)
    terrain_to_draw1: int                   = Retriever(int16,                                                                 default = 0)

    _                                       = Retriever(Bytes[0],                                                              default = b"", on_set = [set_terrain_repeat])
    borders: list[int]                      = Retriever(int16,           min_ver = Version((3, 7)), max_ver = Version((5, 9)), default = 0, repeat = 0)

    terrain_unit_masked_density: list[int]  = Retriever(int16,           min_ver = Version((7, 1)),                            default_factory = lambda _: [], repeat = 30)

    terrain_unit_id: int                    = Retriever(int16,                                                                 default = 0, repeat = 30)
    terrain_unit_density: int               = Retriever(int16,                                                                 default = 0, repeat = 30)
    terrain_placement_flag: int             = Retriever(int8,                                                                  default = 0, repeat = 30)
    terrain_units_used_count: int           = Retriever(int16,                                                                 default = 0)

    phantom_aoe1_HD_DLC: int                = Retriever(int16,           min_ver = Version((3, 7)), max_ver = Version((5, 7)), default = 0)
    phantom_aoe2de: int                     = Retriever(int16,           min_ver = Version((7, 1)),                            default = 0)
    # @formatter:on
