from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i16, i8, f32, u32, bool8


class UnitTask(BaseStruct):
    task_type: int                          = Retriever(i16,                                    default = 1)
    id: int                                 = Retriever(i16,                                    default = -1)
    is_default: bool                        = Retriever(bool8,                                  default = False)

    action_type: int                        = Retriever(i16,                                    default = 0)

    unit_class_id: int                      = Retriever(i16,                                    default = -1)
    unit_type: int                          = Retriever(i16,                                    default = -1)
    terrain_type: int                       = Retriever(i16,                                    default = -1)

    resource_in: int                        = Retriever(i16,                                    default = -1)
    productivity_resource: int              = Retriever(i16,                                    default = -1)
    """the value of this resource is used as a multiplier for work_value1"""
    resource_out: int                       = Retriever(i16,                                    default = -1)
    unused_resource: int                    = Retriever(i16,                                    default = -1)

    work_value1: float                      = Retriever(f32,                                    default = 0)
    """min_conversion_time"""
    work_value2: float                      = Retriever(f32,                                    default = 0)
    """max_conversion_time"""
    work_range: float                       = Retriever(f32,                                    default = 0)

    auto_search_targets: bool               = Retriever(bool8,                                  default = False)
    search_wait_time: float                 = Retriever(f32,                                    default = 0)
    enable_targeting: int                   = Retriever(i8,                                     default = 0)
    combat_level: int                       = Retriever(i8,                                     default = 0)
    gather_type: int                        = Retriever(i16,                                    default = 0)
    """
    0 - Plunder from resource
    1 - Plunder from player
    2 - Raider thing?
    """
    work_mode: int                          = Retriever(i16,                                    default = 0)
    """unused?"""
    target_diplomacy: int                   = Retriever(i8,                                     default = 0)
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
    target_resource_flag: bool              = Retriever(bool8,                                  default = False)
    build_task_flag: bool                   = Retriever(bool8,                                  default = False)

    move_sprite_id: int                     = Retriever(i16,                                    default = -1)
    proceed_sprite_id: int                  = Retriever(i16,                                    default = -1)
    work_sprite_id: int                     = Retriever(i16,                                    default = -1)
    carry_sprite_id: int                    = Retriever(i16,                                    default = -1)

    resource_gather_sound_id: int           = Retriever(i16,                                    default = -1)
    resource_deposit_sound_id: int          = Retriever(i16,                                    default = -1)

    wwise_resource_gather_sound_id: int     = Retriever(u32,    min_ver = Version(7, 1),        default = 0)
    wwise_resource_deposit_sound_id: int    = Retriever(u32,    min_ver = Version(7, 1),        default = 0)
    resource_which_enables_task: int        = Retriever(i16,    min_ver = Version(8, 5),        default = -1)
