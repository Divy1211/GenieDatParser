from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner
from bfp_rs.types.le import i16, u8, i8, f32, Array16

from sections.civilization.type_info.damage_class import DamageClass


class CombatInfo(BaseStruct):
    # @formatter:off
    _base_armor_aoe1: int              = Retriever(u8,                   min_ver = Version(3, 7),    max_ver = Version(3, 7),    default = 232)
    _base_armor_de1: int               = Retriever(i16,                  min_ver = Version(4, 5),    max_ver = Version(4, 5),    default = 1000)
    _base_armor_aok: int               = Retriever(u8,                   min_ver = Version(5, 7, 0), max_ver = Version(5, 7, 0), default = 232)
    _base_armor_aoc: int               = Retriever(i16,                  min_ver = Version(5, 7, 1), max_ver = Version(5, 7, 2), default = 1000)
    _base_armor_swgb: int              = Retriever(i16,                  min_ver = Version(5, 9),    max_ver = Version(5, 9),    default = 1000)
    _base_armor_de2: int               = Retriever(i16,                  min_ver = Version(7, 1),                                default = 10_000)

    base_armor: int                    = RetrieverCombiner(_base_armor_de2, _base_armor_aoc, _base_armor_aok, _base_armor_de1, _base_armor_aoe1, _base_armor_swgb)

    attacks: list[DamageClass]         = Retriever(Array16[DamageClass], min_ver = Version(3, 7),                                default_factory = lambda _ver: [])
    armors: list[DamageClass]          = Retriever(Array16[DamageClass], min_ver = Version(3, 7),                                default_factory = lambda _ver: [])

    defense_terrain_bonus: int         = Retriever(i16,                                                                          default = -1)
    """aka boundary_id"""

    bonus_damage_resistance: float     = Retriever(f32,                  min_ver = Version(7, 3),                                default = 0)

    max_range: float                   = Retriever(f32,                                                                          default = 0)
    blast_width: float                 = Retriever(f32,                                                                          default = 0)
    reload_time: float                 = Retriever(f32,                                                                          default = 0)
    projectile_unit_id: int            = Retriever(i16,                                                                          default = -1)
    accuracy_percent: int              = Retriever(i16,                                                                          default = 0)
    break_off_combat: int              = Retriever(i8,                                                                           default = 0)
    """unused"""
    frame_delay: int                   = Retriever(i16,                                                                          default = 0)
    weapon_offset_x: float             = Retriever(f32,                                                                          default = 0)
    weapon_offset_y: float             = Retriever(f32,                                                                          default = 0)
    weapon_offset_z: float             = Retriever(f32,                                                                          default = 0)
    blast_attack_level: int            = Retriever(u8,                                                                           default = 0)
    min_range: float                   = Retriever(f32,                                                                          default = 0)
    missed_shot_dispersion_mult: float = Retriever(f32,                    min_ver = Version(5, 7),                              default = 0)
    attacking_sprite_id: int           = Retriever(i16,                                                                          default = -1)
    displayed_melee_armor: int         = Retriever(i16,                                                                          default = 0)
    displayed_attack: int              = Retriever(i16,                                                                          default = 0)
    displayed_range: float             = Retriever(f32,                                                                          default = 0)
    displayed_reload_time: float       = Retriever(f32,                                                                          default = 0)
    blast_damage: float                = Retriever(f32,                    min_ver = Version(7, 7),                              default = 0)
    damage_reflection: float           = Retriever(f32,                    min_ver = Version(7, 9),                              default = 0)
    friendly_fire_damage: float        = Retriever(f32,                    min_ver = Version(7, 9),                              default = 0)
    interrupt_frame: int               = Retriever(i16,                    min_ver = Version(8, 4),                              default = 0)
    garrison_firepower: float          = Retriever(f32,                    min_ver = Version(8, 4),                              default = 0)
    attack_graphic2: int               = Retriever(i16,                    min_ver = Version(8, 4),                              default = 0)
    # @formatter:on
