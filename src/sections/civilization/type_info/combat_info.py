from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import int16, uint8, int8, float32, Array16

from src.sections.civilization.type_info.damage_class import DamageClass


class CombatInfo(BaseStruct):
    # @formatter:off
    _base_armor_aoe1: int              = Retriever(uint8, min_ver = Version((3, 7)), max_ver = Version((3, 7)),                        default = 232)
    _base_armor_de1: int               = Retriever(int16, min_ver = Version((4, 5)), max_ver = Version((4, 5)),                        default = 1000)
    _base_armor_aoe2: int              = Retriever(int16, min_ver = Version((5, 7)), max_ver = Version((5, 7)),                        default = 1000) # todo: AoK
    _base_armor_swgb: int              = Retriever(int16, min_ver = Version((5, 9)), max_ver = Version((5, 9)),                        default = 1000)
    _base_armor_de2: int               = Retriever(int16, min_ver = Version((7, 1)),                                                   default = 10_000)

    base_armor: int                    = RetrieverCombiner(_base_armor_de2, _base_armor_aoe2, _base_armor_de1, _base_armor_aoe1, _base_armor_swgb)

    attacks: list[int]                 = Retriever(Array16[DamageClass], min_ver = Version((3, 7)),                                    default_factory = lambda _: [])
    armors: list[int]                  = Retriever(Array16[DamageClass], min_ver = Version((3, 7)),                                    default_factory = lambda _: [])

    defense_terrain_bonus: int         = Retriever(int16,                                                                              default = -1)
    """aka boundary_id"""

    bonus_damage_resistance: float     = Retriever(float32,              min_ver = Version((7, 3)),                                    default = 0)

    max_range: float                   = Retriever(float32,                                                                            default = 0)
    blast_width: float                 = Retriever(float32,                                                                            default = 0)
    reload_time: float                 = Retriever(float32,                                                                            default = 0)
    projectile_unit_id: int            = Retriever(int16,                                                                              default = -1)
    accuracy_percent: int              = Retriever(int16,                                                                              default = 0)
    break_off_combat: int              = Retriever(int8,                                                                               default = 0)
    """unused"""
    frame_delay: int                   = Retriever(int16,                                                                              default = 0)
    weapon_offset_x: float             = Retriever(float32,                                                                            default = 0)
    weapon_offset_y: float             = Retriever(float32,                                                                            default = 0)
    weapon_offset_z: float             = Retriever(float32,                                                                            default = 0)
    blast_attack_level: int            = Retriever(uint8,                                                                              default = 0)
    min_range: float                   = Retriever(float32,                                                                            default = 0)
    missed_shot_dispersion_mult: float = Retriever(float32,              min_ver = Version((5, 7)),                                    default = 0)
    attacking_sprite_id: int           = Retriever(int16,                                                                              default = -1)
    displayed_melee_armor: int         = Retriever(int16,                                                                              default = 0)
    displayed_attack: int              = Retriever(int16,                                                                              default = 0)
    displayed_range: float             = Retriever(float32,                                                                            default = 0)
    displayed_reload_time: float       = Retriever(float32,                                                                            default = 0)
    blast_damage: float                = Retriever(float32,              min_ver = Version((7, 7)),                                    default = 0)
    # @formatter:on
