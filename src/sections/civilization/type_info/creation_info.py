from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import FixedLenArray, int16, float32, int8, int32

from src.sections.civilization.type_info.unit_cost import UnitCost


class CreationInfo(BaseStruct):
    # @formatter:off
    costs: list[UnitCost]                       = Retriever(FixedLenArray[UnitCost, 3],                                        default_factory = lambda sv: [UnitCost(sv) for _ in range(3)])
    train_time: int                             = Retriever(int16,                                                             default = 0)
    location_unit_id: int                       = Retriever(int16,                                                             default = -1)
    button_id: int                              = Retriever(int8,                                                              default = 0)

    rear_attack_modifier: float                 = Retriever(float32,    min_ver = Version((5, 7)),                             default = 0)
    """aka heal_timer"""
    flank_attack_modifier: float                = Retriever(float32,    min_ver = Version((5, 7)),                             default = 0)
    creatable_type: int                         = Retriever(int8,       min_ver = Version((5, 7)),                             default = 0)
    hero_mode: int                              = Retriever(int8,       min_ver = Version((5, 7)),                             default = 0)

    garrisoned_sprite_id: int                   = Retriever(int32,      min_ver = Version((5, 7)),                             default = -1)
    spawning_sprite_id: int                     = Retriever(int16,      min_ver = Version((7, 1)),                             default = -1)
    upgrading_sprite_id: int                    = Retriever(int16,      min_ver = Version((7, 1)),                             default = -1)
    hero_glowing_sprite_id: int                 = Retriever(int16,      min_ver = Version((7, 4)),                             default = -1)
    max_charge: float                           = Retriever(float32,    min_ver = Version((7, 3)),                             default = 0)
    charge_regen_rate: float                    = Retriever(float32,    min_ver = Version((7, 3)),                             default = 0)
    charge_event: int                           = Retriever(int16,      min_ver = Version((7, 3)),                             default = 0)
    charge_type: int                            = Retriever(int16,      min_ver = Version((7, 3)),                             default = 0)

    min_conversion_time_modifier: float         = Retriever(float32,    min_ver = Version((7, 6)),                             default = 0)
    max_conversion_time_modifier: float         = Retriever(float32,    min_ver = Version((7, 6)),                             default = 0)
    conversion_chance_mod: float                = Retriever(float32,    min_ver = Version((7, 6)),                             default = 0)

    min_projectiles: float                      = Retriever(float32,    min_ver = Version((5, 7)),                             default = 0)
    max_projectiles: int                        = Retriever(int8,       min_ver = Version((5, 7)),                             default = 0)
    projectile_spawning_area_width: float       = Retriever(float32,    min_ver = Version((5, 7)),                             default = 0)
    projectile_spawning_area_length: float      = Retriever(float32,    min_ver = Version((5, 7)),                             default = 0)
    projectile_spawning_area_randomness: float  = Retriever(float32,    min_ver = Version((5, 7)),                             default = 0)
    secondary_projectile_unit_id: int           = Retriever(int32,      min_ver = Version((5, 7)),                             default = 0)
    special_graphic_id: int                     = Retriever(int32,      min_ver = Version((5, 7)),                             default = 0)
    special_activation: int                     = Retriever(int8,       min_ver = Version((5, 7)),                             default = 0)

    displayed_pierce_armor: int                 = Retriever(int16,                                                             default = 0)
    # @formatter:on
