from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import (
    int8, uint16, int16, uint32, float32, int32, uint8, Array8, Bytes, str16, bool8,
    FixedLenArray, FixedLenStr
)

from src.sections.civilization.type_info import (
    AnimationInfo, UnitType, MovementInfo, TaskInfo, CreationInfo, ProjectileInfo, CombatInfo, BuildingInfo
)
from src.sections.civilization.unit_damage_sprite import UnitDamageSprite
from src.sections.civilization.unit_resource import UnitResource

class Unit(BaseStruct):
    @staticmethod
    def disable_types(_, instance: Unit):
        if instance.base_class < UnitType.Animated or instance.base_class == UnitType.LegacyTree:
            Retriever.set_repeat(Unit.animation_info, instance, -1)
            Retriever.set_repeat(Unit.movement_info, instance, -1)
            Retriever.set_repeat(Unit.task_info, instance, -1)
            Retriever.set_repeat(Unit.combat_info, instance, -1)
            Retriever.set_repeat(Unit.projectile_info, instance, -1)
            Retriever.set_repeat(Unit.creation_info, instance, -1)
            Retriever.set_repeat(Unit.building_info, instance, -1)
        elif instance.base_class < UnitType.Moving:
            Retriever.set_repeat(Unit.movement_info, instance, -1)
            Retriever.set_repeat(Unit.task_info, instance, -1)
            Retriever.set_repeat(Unit.combat_info, instance, -1)
            Retriever.set_repeat(Unit.projectile_info, instance, -1)
            Retriever.set_repeat(Unit.creation_info, instance, -1)
            Retriever.set_repeat(Unit.building_info, instance, -1)
        elif instance.base_class < UnitType.Acting:
            Retriever.set_repeat(Unit.task_info, instance, -1)
            Retriever.set_repeat(Unit.combat_info, instance, -1)
            Retriever.set_repeat(Unit.projectile_info, instance, -1)
            Retriever.set_repeat(Unit.creation_info, instance, -1)
            Retriever.set_repeat(Unit.building_info, instance, -1)
        elif instance.base_class < UnitType.Combat:
            Retriever.set_repeat(Unit.combat_info, instance, -1)
            Retriever.set_repeat(Unit.projectile_info, instance, -1)
            Retriever.set_repeat(Unit.creation_info, instance, -1)
            Retriever.set_repeat(Unit.building_info, instance, -1)
        elif instance.base_class == UnitType.Projectile:
            Retriever.set_repeat(Unit.creation_info, instance, -1)
            Retriever.set_repeat(Unit.building_info, instance, -1)
        elif instance.base_class < UnitType.Creatable:
            Retriever.set_repeat(Unit.projectile_info, instance, -1)
            Retriever.set_repeat(Unit.creation_info, instance, -1)
            Retriever.set_repeat(Unit.building_info, instance, -1)
        elif instance.base_class < UnitType.Building:
            Retriever.set_repeat(Unit.projectile_info, instance, -1)
            Retriever.set_repeat(Unit.building_info, instance, -1)
        else:
            Retriever.set_repeat(Unit.projectile_info, instance, -1)

    @staticmethod
    def set_name_len(_, instance: Unit):
        Unit._name_aoe1.dtype.length = instance._len_name_aoe1
        Unit._name_aoe2_swgb.dtype.length = instance._len_name_aoe2_swgb

    @staticmethod
    def sync_name_len(_, instance: Unit):
        Unit._name_aoe1.dtype.length = instance._len_name_aoe1 = len(instance._name_aoe1)
        Unit._name_aoe2_swgb.dtype.length = instance._len_name_aoe2_swgb = len(instance._name_aoe2_swgb)

    @staticmethod
    def sync_ids(_, instance: Unit):
        instance.copy_id = instance.base_id = instance.id

    # @formatter:off
    base_class: int                          = Retriever(int8,                                                                 default = UnitType.EyeCandy, on_read = [disable_types])

    _len_name_aoe1: int                      = Retriever(uint16,         min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = 0)
    _len_name_aoe2_swgb: int                 = Retriever(uint16,         min_ver = Version((5, 7)), max_ver = Version((5, 9)), default = 0, on_read = [set_name_len], on_write = [sync_name_len])

    id: int                                  = Retriever(int16,                                                                default = -1, on_write = [sync_ids])

    _name_str_id_de2: int                    = Retriever(uint32,         min_ver = Version((7, 2)),                            default = 0)
    _creation_str_id_de2: int                = Retriever(uint32,         min_ver = Version((7, 2)),                            default = 0)

    _name_str_id_aoe1_de1_aoe2_swgb: int     = Retriever(uint16,         min_ver = Version((3, 7)), max_ver = Version((7, 1)), default = 0)
    _creation_str_id_aoe1_de1_aoe2_swgb: int = Retriever(uint16,         min_ver = Version((3, 7)), max_ver = Version((7, 1)), default = 0)

    name_str_id: int                         = RetrieverCombiner(_name_str_id_de2, _name_str_id_aoe1_de1_aoe2_swgb)
    creation_str_id: int                     = RetrieverCombiner(_creation_str_id_de2, _creation_str_id_aoe1_de1_aoe2_swgb)

    class_: int                              = Retriever(int16,                                                                default = -1)

    standing_sprite_id1: int                 = Retriever(int16,                                                                default = -1)
    standing_sprite_id2: int                 = Retriever(int16,          min_ver = Version((5, 7)),                            default = -1)
    dying_sprite_id: int                     = Retriever(int16,                                                                default = -1)
    undead_sprite_id: int                    = Retriever(int16,                                                                default = -1)

    undead_mode: int                         = Retriever(int8,                                                                 default = False)
    hit_points: int                          = Retriever(int16,                                                                default = 1)
    line_of_sight: float                     = Retriever(float32,                                                              default = 2)
    garrison_capacity: int                   = Retriever(int8,                                                                 default = 0)
    radius_x: float                          = Retriever(float32,                                                              default = 0)
    radius_y: float                          = Retriever(float32,                                                              default = 0)
    radius_z: float                          = Retriever(float32,                                                              default = 0)

    train_sound_id: int                      = Retriever(int16,                                                                default = -1)
    damage_sound_id1: int                    = Retriever(int16,          min_ver = Version((5, 7)),                            default = -1)

    dead_unit_id: int                        = Retriever(int16,                                                                default = -1)
    _blood_unit_id_de1: int                  = Retriever(int16,          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = -1)
    _blood_unit_id_de2: int                  = Retriever(int16,          min_ver = Version((7, 1)),                            default = -1)

    blood_unit_id: int                       = RetrieverCombiner(_blood_unit_id_de2, _blood_unit_id_de1)

    sort_number: int                         = Retriever(int8,                                                                 default = 0)
    can_be_built_on: int                     = Retriever(int8,                                                                 default = 0)
    icon_id: int                             = Retriever(int16,                                                                default = -1)
    hide_in_editor: int                      = Retriever(int8,                                                                 default = 0)
    old_portrait_icon_id: int                = Retriever(int16,                                                                default = -1)

    enabled: bool                            = Retriever(bool8,                                                                default = True)
    disabled: bool                           = Retriever(bool8,          min_ver = Version((5, 7)),                            default = False)

    required_side_terrain_id1: int           = Retriever(int16,                                                                default = -1)
    required_side_terrain_id2: int           = Retriever(int16,                                                                default = -1)
    required_center_terrain_id1: int         = Retriever(int16,                                                                default = -1)
    required_center_terrain_id2: int         = Retriever(int16,                                                                default = -1)
    required_clearance_radius_x: float       = Retriever(float32,                                                              default = 0)
    required_clearance_radius_y: float       = Retriever(float32,                                                              default = 0)

    elevation_restriction_mode: int          = Retriever(int8,                                                                 default = 0)
    """aka hill_mode"""
    fog_visibility_mode: int                 = Retriever(int8,                                                                 default = 0)
    terrain_restriction_id: int              = Retriever(int16,                                                                default = 0)
    movement_mode: int                       = Retriever(int8,                                                                 default = 0)
    """aka fly_mode"""

    resource_carry_capacity: int             = Retriever(int16,                                                                default = 0)
    resource_decay_rate: float               = Retriever(float32,                                                              default = -1)

    blast_defense_level: int                 = Retriever(int8,                                                                 default = 3)
    combat_level: int                        = Retriever(int8,                                                                 default = 0)

    interaction_mode: int                    = Retriever(int8,                                                                 default = 0)
    """aka select_level"""
    minimap_mode: int                        = Retriever(int8,                                                                 default = 0)
    """aka map_draw_level"""
    interface_mode: int                      = Retriever(int8,                                                                 default = 0)
    """aka unit_level"""
    multiple_attribute_mode: float           = Retriever(float32,                                                              default = 0)
    minimap_color: int                       = Retriever(int8,                                                                 default = 0)

    help_str_id: int                         = Retriever(int32,                                                                default = 0)
    hotkey_text_str_id: int                  = Retriever(int32,                                                                default = 0)
    """aka help_page_str_id"""
    hotkey_str_id: int                       = Retriever(int32,                                                                default = 0)

    recyclable: int                          = Retriever(int8,                                                                 default = 0)
    enable_auto_gather: int                  = Retriever(int8,                                                                 default = 0)
    doppelganger_mode: int                   = Retriever(int8,                                                                 default = 0)
    resource_gather_group: int               = Retriever(int8,                                                                 default = 0)

    occlusion_mode: int                      = Retriever(uint8,          min_ver = Version((5, 7)),                            default = 0)
    _obstruction_type_aoe2_swgb_de2: int     = Retriever(int8,           min_ver = Version((5, 7)),                            default = 0)
    _obstruction_class_aoe2_swgb_de2: int    = Retriever(int8,           min_ver = Version((5, 7)),                            default = 0)
    """aka selection_shape"""
    trait: int                               = Retriever(uint8,          min_ver = Version((5, 7)),                            default = 0) # todo: AoK
    civilization_id: int                     = Retriever(int8,           min_ver = Version((5, 7)),                            default = 0) # todo: AoK
    trait_piece: int                         = Retriever(int16,          min_ver = Version((5, 7)),                            default = 0) # todo: AoK
    """likely unused"""

    _obstruction_type_de1: int               = Retriever(int8,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    _obstruction_class_de1: int              = Retriever(int8,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)

    obstruction_type: int                    = RetrieverCombiner(_obstruction_type_aoe2_swgb_de2, _obstruction_type_de1)
    obstruction_class: int                   = RetrieverCombiner(_obstruction_class_aoe2_swgb_de2, _obstruction_class_de1)

    selection_effect: int                    = Retriever(int8,                                                                 default = 1)
    editor_selection_color: int              = Retriever(uint8,                                                                default = 0)
    selection_radius_x: float                = Retriever(float32,                                                              default = 0)
    selection_radius_y: float                = Retriever(float32,                                                              default = 0)
    selection_radius_z: float                = Retriever(float32,                                                              default = 0)

    # todo: investigate this
    scx_trigger_data1: int                   = Retriever(uint32,         min_ver = Version((7, 1)),                            default = 0)
    scx_trigger_data2: int                   = Retriever(uint32,         min_ver = Version((7, 1)),                            default = 0)

    resources: list[UnitResource]            = Retriever(FixedLenArray[UnitResource, 3],                                       default_factory = lambda sv: [UnitResource(sv) for _ in range(3)])
    damage_sprites: list[UnitDamageSprite]   = Retriever(Array8[UnitDamageSprite],                                             default_factory = lambda _: [])

    selection_sound_id:  int                 = Retriever(int16,                                                                default = -1)
    dying_sound_id: int                      = Retriever(int16,                                                                default = -1)

    wwise_train_sound_id: int                = Retriever(uint32,         min_ver = Version((7, 1)),                            default = 0)
    wwise_damage_sound_id: int               = Retriever(uint32,         min_ver = Version((7, 1)),                            default = 0)
    wwise_selection_sound_id: int            = Retriever(uint32,         min_ver = Version((7, 1)),                            default = 0)
    wwise_dying_sound_id: int                = Retriever(uint32,         min_ver = Version((7, 1)),                            default = 0)

    old_attack_mode: int                     = Retriever(int8,                                                                 default = 0)
    convert_terrain: int                     = Retriever(int8,                                                                 default = 0)

    _str_sign_de1: bytes                     = Retriever(Bytes[2],       min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = b"\x60\x0A")
    _str_sign_de2: bytes                     = Retriever(Bytes[2],       min_ver = Version((7, 1)),                            default = b"\x60\x0A")

    _name_de1: str                           = Retriever(str16,          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = "")
    _name_de2: str                           = Retriever(str16,          min_ver = Version((7, 1)),                            default = "")

    _name_aoe1: str                          = Retriever(FixedLenStr[0], min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = "")
    _name_aoe2_swgb: str                     = Retriever(FixedLenStr[0], min_ver = Version((5, 7)), max_ver = Version((5, 9)), default = "")

    name: str                                = RetrieverCombiner(_name_de2, _name_aoe2_swgb, _name_de1, _name_aoe1)

    name2: str                               = Retriever(str16,          min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = "")
    unit_line_id: int                        = Retriever(int16,          min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = -1)
    min_tech_level: int                      = Retriever(int8,           min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = -1)

    copy_id: int                             = Retriever(int16,                                                                default = -1)
    base_id: int                             = Retriever(int16,          min_ver = Version((5, 7)),                            default = -1)

    telemetry_id: int                        = Retriever(int16,          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = -1)

    animation_info: AnimationInfo            = Retriever(AnimationInfo,                                                        default_factory = AnimationInfo)
    movement_info: MovementInfo              = Retriever(MovementInfo,                                                         default_factory = MovementInfo)
    task_info: TaskInfo                      = Retriever(TaskInfo,                                                             default_factory = TaskInfo)
    combat_info: CombatInfo                  = Retriever(CombatInfo,                                                           default_factory = CombatInfo)
    projectile_info: ProjectileInfo          = Retriever(ProjectileInfo,                                                       default_factory = ProjectileInfo)
    creation_info: CreationInfo              = Retriever(CreationInfo,                                                         default_factory = CreationInfo)
    building_info: BuildingInfo              = Retriever(BuildingInfo,                                                         default_factory = BuildingInfo)
    # @formatter:on
