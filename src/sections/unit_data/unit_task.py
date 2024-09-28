from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int8, float32, uint32, bool16, bool8


class UnitTask(BaseStruct):
    used: bool                              = Retriever(bool16,                            default = True)
    """aka task_type"""
    id: int                                 = Retriever(int16,                             default = 0)
    is_default: int                         = Retriever(int8,                              default = 0)

    action_type: int                        = Retriever(int16,                             default = 0)

    unit_class_id: int                      = Retriever(int16,                             default = 0)
    unit_type: int                          = Retriever(int16,                             default = 0)
    terrain_type: int                       = Retriever(int16,                             default = 0)

    resource_in: int                        = Retriever(int16,                             default = 0)
    productivity_resource: int              = Retriever(int16,                             default = 0)
    """the value of this resource is used as a multiplier for work_value1"""
    resource_out: int                       = Retriever(int16,                             default = 0)
    unused_resource: int                    = Retriever(int16,                             default = 0)

    work_value1: float                      = Retriever(float32,                           default = 0)
    """min_conversion_time"""
    work_value2: float                      = Retriever(float32,                           default = 0)
    """max_conversion_time"""
    work_range: float                       = Retriever(float32,                           default = 0)

    auto_search_targets: bool               = Retriever(bool8,                             default = False)
    search_wait_time: float                 = Retriever(float32,                           default = 0)
    enable_targeting: bool                  = Retriever(bool8,                             default = False)
    combat_level: int                       = Retriever(int8,                              default = 0)
    gather_type: int                        = Retriever(int16,                             default = 0)
    """
    0 - Plunder from resource
    1 - Plunder from player
    2 - Raider thing?
    """
    work_mode: int                          = Retriever(int16,                             default = 0)
    """unused?"""
    target_diplomacy: int                   = Retriever(int8,                              default = 0)
    """
    0 - All
    1 - Self
    2 - Neutral + Enemy
    3 - Gaia
    4 - Self + Ally + Gaia
    5 - Gaia + Neutral + Enemy
    6 - Non Self
    other - All
    """
    check_target_resource: bool             = Retriever(bool8,                             default = False)
    is_build_task: bool                     = Retriever(bool8,                             default = False)

    move_sprite_id: int                     = Retriever(int16,                             default = 0)
    proceed_sprite_id: int                  = Retriever(int16,                             default = 0)
    work_sprite_id: int                     = Retriever(int16,                             default = 0)
    carry_sprite_id: int                    = Retriever(int16,                             default = 0)

    resource_gather_sound_id: int           = Retriever(int16,                             default = 0)
    resource_deposit_sound_id: int          = Retriever(int16,                             default = 0)

    wwise_resource_gather_sound_id: int     = Retriever(uint32, min_ver = Version((7, 1)), default = 0)
    wwise_resource_deposit_sound_id: int    = Retriever(uint32, min_ver = Version((7, 1)), default = 0)
