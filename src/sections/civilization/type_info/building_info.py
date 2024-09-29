from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int8, float32, FixedLenArray, int32, uint8

from src.sections.civilization.type_info.building_annex import BuildingAnnex
from src.sections.civilization.type_info.looting_table import LootingTable


class BuildingInfo(BaseStruct):
    # @formatter:off
    construction_sprite_id: int        = Retriever(int16,                                                                default = -1)
    snow_sprite_id: int                = Retriever(int16,                            min_ver = Version((5, 7, 1)),       default = -1)
    destruction_sprite_id: int         = Retriever(int16,                            min_ver = Version((7, 1)),          default = -1)
    destruction_rubble_sprite_id: int  = Retriever(int16,                            min_ver = Version((7, 1)),          default = -1)
    research_sprite_id: int            = Retriever(int16,                            min_ver = Version((7, 1)),          default = -1)
    research_complete_sprite_id: int   = Retriever(int16,                            min_ver = Version((7, 1)),          default = -1)

    adjacent_mode: int                 = Retriever(int8,                                                                 default = 0)
    graphics_angle: int                = Retriever(int16,                                                                default = 0)
    disappears_when_built: int         = Retriever(int8,                                                                 default = 0)
    stack_unit_id: int                 = Retriever(int16,                                                                default = -1)
    foundation_terrain_id: int         = Retriever(int16,                                                                default = -1)
    old_overlay_id: int                = Retriever(int16,                                                                default = -1)
    completion_tech_id: int            = Retriever(int16,                                                                default = -1)

    can_burn: int                      = Retriever(int8,                             min_ver = Version((5, 7)),          default = 0)
    building_annex: BuildingAnnex      = Retriever(FixedLenArray[BuildingAnnex, 4],  min_ver = Version((5, 7)),          default_factory = lambda sv: [BuildingAnnex(sv) for _ in range(4)])
    head_unit_id: int                  = Retriever(int16,                            min_ver = Version((5, 7)),          default = -1)
    transform_unit_id: int             = Retriever(int16,                            min_ver = Version((5, 7)),          default = -1)

    transform_sound_id: int            = Retriever(int16,                            min_ver = Version((5, 7)),          default = -1)
    construction_sound_id: int         = Retriever(int16,                                                                default = -1)
    wwise_construction_sound_id: int   = Retriever(int32,                            min_ver = Version((7, 1)),          default = 0)
    wwise_transform_sound_id: int      = Retriever(int32,                            min_ver = Version((7, 1)),          default = 0)

    garrison_type: int                 = Retriever(uint8,                            min_ver = Version((5, 7)),          default = 0)
    garrison_heal_rate: float          = Retriever(float32,                          min_ver = Version((5, 7)),          default = 0)
    garrison_repair_rate: float        = Retriever(float32,                          min_ver = Version((5, 7)),          default = 0)
    salvage_unit_id: int               = Retriever(int16,                            min_ver = Version((5, 7)),          default = 0)
    salvage_attributes: LootingTable   = Retriever(LootingTable,                     min_ver = Version((5, 7)),          default_factory = LootingTable)
    # @formatter:on
