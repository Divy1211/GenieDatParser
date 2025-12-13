from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import Array, i16, f32, i8, i32, u8, Array16

from sections.civilization.type_info.unit_cost import UnitCost

class TrainLocation(BaseStruct):
    # @formatter:off
    train_time: int                             = Retriever(i16,                                         default = 0)
    location_unit_id: int                       = Retriever(i16,                                         default = -1)
    button_id: int                              = Retriever(u8,                                          default = 0)
    hotkey_id: int                              = Retriever(i32,                min_ver = Version(8, 7), default = 0)
    # @formatter:on

class CreationInfo(BaseStruct):
    # @formatter:off
    costs: list[UnitCost]                       = Retriever(Array[3][UnitCost],                                                         default_factory = lambda ver: [UnitCost(ver) for _ in range(3)])

    train_locations_old: list[TrainLocation]    = Retriever(Array[1][TrainLocation],                          max_ver = Version(8, 5),  default_factory = lambda ver: [TrainLocation(ver)])
    train_locations_new: list[TrainLocation]    = Retriever(Array16[TrainLocation],  min_ver = Version(8, 6),                           default_factory = lambda ver: [])

    rear_attack_modifier: float                 = Retriever(f32,                     min_ver = Version(5, 7), default = 0)
    """aka heal_timer"""
    flank_attack_modifier: float                = Retriever(f32,                     min_ver = Version(5, 7), default = 0)
    creatable_type: int                         = Retriever(i8,                      min_ver = Version(5, 7), default = 0)
    hero_mode: int                              = Retriever(i8,                      min_ver = Version(5, 7), default = 0)

    garrisoned_sprite_id: int                   = Retriever(i32,                     min_ver = Version(5, 7), default = -1)
    spawning_sprite_id: int                     = Retriever(i16,                     min_ver = Version(7, 1), default = -1)
    upgrading_sprite_id: int                    = Retriever(i16,                     min_ver = Version(7, 1), default = -1)
    hero_glowing_sprite_id: int                 = Retriever(i16,                     min_ver = Version(7, 4), default = -1)
    idle_attack_graphic: int                    = Retriever(i16,                     min_ver = Version(8, 3), default = -1)
    max_charge: float                           = Retriever(f32,                     min_ver = Version(7, 3), default = 0)
    charge_regen_rate: float                    = Retriever(f32,                     min_ver = Version(7, 3), default = 0)

    charge_event: int                           = Retriever(i16,                     min_ver = Version(7, 3), default = 0)
    charge_type: int                            = Retriever(i16,                     min_ver = Version(7, 3), default = 0)
    charge_target: float                        = Retriever(i16,                     min_ver = Version(8, 0), default = 0)
    charge_projectile_unit: float               = Retriever(i32,                     min_ver = Version(8, 2), default = 0)
    attack_priority: float                      = Retriever(u8,                      min_ver = Version(8, 2), default = 0)
    invulnerability_level: float                = Retriever(f32,                     min_ver = Version(8, 2), default = 0)

    button_icon_id: float                       = Retriever(i16,                     min_ver = Version(8, 1), default = 0)
    button_short_tooltip_str_id: float          = Retriever(i32,                     min_ver = Version(8, 1), default = 0)
    button_extend_tooltip_str_id: float         = Retriever(i32,                     min_ver = Version(8, 1), default = 0)
    button_hotkey_action: float                 = Retriever(i16,                     min_ver = Version(8, 1), default = 0)


    min_conversion_time_modifier: float         = Retriever(f32,                     min_ver = Version(7, 6), default = 0)
    max_conversion_time_modifier: float         = Retriever(f32,                     min_ver = Version(7, 6), default = 0)
    conversion_chance_mod: float                = Retriever(f32,                     min_ver = Version(7, 6), default = 0)

    min_projectiles: float                      = Retriever(f32,                     min_ver = Version(5, 7), default = 0)
    max_projectiles: int                        = Retriever(i8,                      min_ver = Version(5, 7), default = 0)
    projectile_spawning_area_width: float       = Retriever(f32,                     min_ver = Version(5, 7), default = 0)
    projectile_spawning_area_length: float      = Retriever(f32,                     min_ver = Version(5, 7), default = 0)
    projectile_spawning_area_randomness: float  = Retriever(f32,                     min_ver = Version(5, 7), default = 0)
    secondary_projectile_unit_id: int           = Retriever(i32,                     min_ver = Version(5, 7), default = 0)
    special_graphic_id: int                     = Retriever(i32,                     min_ver = Version(5, 7), default = 0)
    special_activation: int                     = Retriever(i8,                      min_ver = Version(5, 7), default = 0)

    displayed_pierce_armor: int                 = Retriever(i16,                                              default = 0)
    # @formatter:on
