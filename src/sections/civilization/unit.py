from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner, ret
from bfp_rs.combinators import set_repeat, set_, if_else, if_
from bfp_rs.types.le import (
    i8, u16, i16, u32, f32, i32, u8, Array8, Bytes, str16, Array, Str, bool8
)

from sections.civilization.type_info import (
    AnimationInfo, UnitType, MovementInfo, TaskInfo, CreationInfo, ProjectileInfo, CombatInfo, BuildingInfo
)
from sections.civilization.unit_damage_sprite import UnitDamageSprite
from sections.civilization.unit_resource import UnitResource


def disable_types():
    disables = [
        set_repeat(ret(Unit.animation_info)).to(-1),
        set_repeat(ret(Unit.movement_info)).to(-1),
        set_repeat(ret(Unit.task_info)).to(-1),
        set_repeat(ret(Unit.combat_info)).to(-1),
        set_repeat(ret(Unit.projectile_info)).to(-1),
        set_repeat(ret(Unit.creation_info)).to(-1),
        set_repeat(ret(Unit.building_info)).to(-1),
    ]

    return [if_else(
        if_(Unit.type_).lt(UnitType.Animated).then(*disables),
        if_(Unit.type_).eq(UnitType.LegacyTree).then(*disables),
        if_(Unit.type_).lt(UnitType.Moving).then(*disables[1:]),
        if_(Unit.type_).lt(UnitType.Acting).then(*disables[2:]),
        if_(Unit.type_).lt(UnitType.Combat).then(*disables[3:]),
        if_(Unit.type_).eq(UnitType.Projectile).then(*disables[5:]),
        if_(Unit.type_).lt(UnitType.Creatable).then(*disables[4:]),
        if_(Unit.type_).lt(UnitType.Building).then(*disables[6:], disables[4]),
        set_repeat(ret(Unit.projectile_info)).to(-1),
    )]


def name_aoe2_len():
    return [
        set_repeat(ret(Unit._name_aoe2_swgb)).from_(Unit._len_name_aoe2_swgb)
    ]

def sync_name_aoe2_len():
    return [
        set_(Unit._len_name_aoe2_swgb).from_len(ret(Unit._name_aoe2_swgb))
    ]

def name_aoe1_len():
    return [
        set_repeat(ret(Unit._name_aoe1)).from_(Unit._len_name_aoe1)
    ]

def sync_name_aoe1_len():
    return [
        set_(Unit._len_name_aoe1).from_len(ret(Unit._name_aoe1))
    ]


def sync_ids():
    return [
        set_(Unit.copy_id).from_(Unit.id),
        set_(Unit.base_id).from_(Unit.id),
    ]

class Unit(BaseStruct):
    # @formatter:off
    type_: int                               = Retriever(i8,                                                             default = UnitType.EyeCandy, on_read = disable_types)

    _len_name_aoe1: int                      = Retriever(u16,         min_ver = Version(3, 7), max_ver = Version(3, 7),  default = 0, on_read = name_aoe1_len, on_write = sync_name_aoe1_len)
    _len_name_aoe2_swgb: int                 = Retriever(u16,         min_ver = Version(5, 7), max_ver = Version(5, 9),  default = 0, on_read = name_aoe2_len, on_write = sync_name_aoe2_len)

    id: int                                  = Retriever(i16,                                                            default = -1, on_write = sync_ids)

    _name_str_id_de2: int                    = Retriever(u32,         min_ver = Version(7, 2),                           default = 0)
    _creation_str_id_de2: int                = Retriever(u32,         min_ver = Version(7, 2),                           default = 0)

    _name_str_id_aoe1_de1_aoe2_swgb: int     = Retriever(u16,         min_ver = Version(3, 7), max_ver = Version(7, 1),  default = 0)
    _creation_str_id_aoe1_de1_aoe2_swgb: int = Retriever(u16,         min_ver = Version(3, 7), max_ver = Version(7, 1),  default = 0)

    name_str_id: int                         = RetrieverCombiner(_name_str_id_de2, _name_str_id_aoe1_de1_aoe2_swgb)
    creation_str_id: int                     = RetrieverCombiner(_creation_str_id_de2, _creation_str_id_aoe1_de1_aoe2_swgb)

    class_: int                              = Retriever(i16,                                                            default = -1)

    standing_sprite_id1: int                 = Retriever(i16,                                                            default = -1)
    standing_sprite_id2: int                 = Retriever(i16,          min_ver = Version(5, 7),                          default = -1)
    dying_sprite_id: int                     = Retriever(i16,                                                            default = -1)
    undead_sprite_id: int                    = Retriever(i16,                                                            default = -1)

    undead_mode: int                         = Retriever(i8,                                                             default = False)
    hit_points: int                          = Retriever(i16,                                                            default = 1)
    line_of_sight: float                     = Retriever(f32,                                                            default = 2)
    garrison_capacity: int                   = Retriever(i8,                                                             default = 0)
    radius_x: float                          = Retriever(f32,                                                            default = 0)
    radius_y: float                          = Retriever(f32,                                                            default = 0)
    radius_z: float                          = Retriever(f32,                                                            default = 0)

    train_sound_id: int                      = Retriever(i16,                                                            default = -1)
    damage_sound_id1: int                    = Retriever(i16,          min_ver = Version(5, 7),                          default = -1)

    dead_unit_id: int                        = Retriever(i16,                                                            default = -1)
    _blood_unit_id_de1: int                  = Retriever(i16,          min_ver = Version(4, 5), max_ver = Version(4, 5), default = -1)
    _blood_unit_id_de2: int                  = Retriever(i16,          min_ver = Version(7, 1),                          default = -1)

    blood_unit_id: int                       = RetrieverCombiner(_blood_unit_id_de2, _blood_unit_id_de1)

    sort_number: int                         = Retriever(i8,                                                             default = 0)
    can_be_built_on: int                     = Retriever(i8,                                                             default = 0)
    icon_id: int                             = Retriever(i16,                                                            default = -1)
    hide_in_editor: int                      = Retriever(i8,                                                             default = 0)
    old_portrait_icon_id: int                = Retriever(i16,                                                            default = -1)

    enabled: bool                            = Retriever(bool8,                                                          default = True)
    disabled: bool                           = Retriever(bool8,           min_ver = Version(5, 7),                       default = False)

    required_side_terrain_id1: int           = Retriever(i16,                                                            default = -1)
    required_side_terrain_id2: int           = Retriever(i16,                                                            default = -1)
    required_center_terrain_id1: int         = Retriever(i16,                                                            default = -1)
    required_center_terrain_id2: int         = Retriever(i16,                                                            default = -1)
    required_clearance_radius_x: float       = Retriever(f32,                                                            default = 0)
    required_clearance_radius_y: float       = Retriever(f32,                                                            default = 0)

    elevation_restriction_mode: int          = Retriever(i8,                                                             default = 0)
    """aka hill_mode"""
    fog_visibility_mode: int                 = Retriever(i8,                                                             default = 0)
    terrain_restriction_id: int              = Retriever(i16,                                                            default = 0)
    movement_mode: int                       = Retriever(i8,                                                             default = 0)
    """aka fly_mode"""

    resource_carry_capacity: int             = Retriever(i16,                                                            default = 0)
    resource_decay_rate: float               = Retriever(f32,                                                            default = -1)

    blast_defense_level: int                 = Retriever(i8,                                                             default = 3)
    combat_level: int                        = Retriever(i8,                                                             default = 0)

    interaction_mode: int                    = Retriever(i8,                                                             default = 0)
    """aka select_level"""
    minimap_mode: int                        = Retriever(i8,                                                             default = 0)
    """aka map_draw_level"""
    interface_mode: int                      = Retriever(i8,                                                             default = 0)
    """aka unit_level"""
    multiple_attribute_mode: float           = Retriever(f32,                                                            default = 0)
    minimap_color: int                       = Retriever(i8,                                                             default = 0)

    help_str_id: int                         = Retriever(i32,                                                            default = 0)
    hotkey_text_str_id: int                  = Retriever(i32,                                                            default = 0)
    """aka help_page_str_id"""
    hotkey_str_id: int                       = Retriever(i32,                            max_ver = Version(8, 6),        default = 0)

    recyclable: int                          = Retriever(i8,                                                             default = 0)
    enable_auto_gather: int                  = Retriever(i8,                                                             default = 0)
    doppelganger_mode: int                   = Retriever(i8,                                                             default = 0)
    resource_gather_group: int               = Retriever(i8,                                                             default = 0)

    occlusion_mode: int                      = Retriever(u8,           min_ver = Version(5, 7),                          default = 0)
    _obstruction_type_aoe2_swgb_de2: int     = Retriever(i8,           min_ver = Version(5, 7),                          default = 0)
    _obstruction_class_aoe2_swgb_de2: int    = Retriever(i8,           min_ver = Version(5, 7),                          default = 0)
    """aka selection_shape"""
    trait: int                               = Retriever(u8,           min_ver = Version(5, 7, 1),                       default = 0)
    civilization_id: int                     = Retriever(i8,           min_ver = Version(5, 7, 1),                       default = 0)
    trait_piece: int                         = Retriever(i16,          min_ver = Version(5, 7, 1),                       default = 0)
    """likely unused"""

    _obstruction_type_de1: int               = Retriever(i8,           min_ver = Version(4, 5), max_ver = Version(4, 5), default = 0)
    _obstruction_class_de1: int              = Retriever(i8,           min_ver = Version(4, 5), max_ver = Version(4, 5), default = 0)

    obstruction_type: int                    = RetrieverCombiner(_obstruction_type_aoe2_swgb_de2, _obstruction_type_de1)
    obstruction_class: int                   = RetrieverCombiner(_obstruction_class_aoe2_swgb_de2, _obstruction_class_de1)

    selection_effect: int                    = Retriever(i8,                                                             default = 1)
    editor_selection_color: int              = Retriever(u8,                                                             default = 0)
    selection_radius_x: float                = Retriever(f32,                                                            default = 0)
    selection_radius_y: float                = Retriever(f32,                                                            default = 0)
    selection_radius_z: float                = Retriever(f32,                                                            default = 0)

    # todo: investigate this
    scx_trigger_data1: int                   = Retriever(u32,         min_ver = Version(7, 1),                           default = 0)
    scx_trigger_data2: int                   = Retriever(u32,         min_ver = Version(7, 1),                           default = 0)

    resources: list[UnitResource]            = Retriever(Array[3][UnitResource],                                         default_factory = lambda ver: [UnitResource(ver) for _ in range(3)])
    damage_sprites: list[UnitDamageSprite]   = Retriever(Array8[UnitDamageSprite],                                       default_factory = lambda _ver: [])

    selection_sound_id:  int                 = Retriever(i16,                                                            default = -1)
    dying_sound_id: int                      = Retriever(i16,                                                            default = -1)

    wwise_train_sound_id: int                = Retriever(u32,         min_ver = Version(7, 1),                           default = 0)
    wwise_damage_sound_id: int               = Retriever(u32,         min_ver = Version(7, 1),                           default = 0)
    wwise_selection_sound_id: int            = Retriever(u32,         min_ver = Version(7, 1),                           default = 0)
    wwise_dying_sound_id: int                = Retriever(u32,         min_ver = Version(7, 1),                           default = 0)

    old_attack_mode: int                     = Retriever(i8,                                                             default = 0)
    convert_terrain: int                     = Retriever(i8,                                                             default = 0)

    _str_sign_de1: bytes                     = Retriever(Bytes[2],    min_ver = Version(4, 5), max_ver = Version(4, 5),  default = b"\x0A\x60")
    _str_sign_de2: bytes                     = Retriever(Bytes[2],    min_ver = Version(7, 1),                           default = b"\x0A\x60")

    _name_de1: str                           = Retriever(str16,       min_ver = Version(4, 5), max_ver = Version(4, 5),  default = "")
    _name_de2: str                           = Retriever(str16,       min_ver = Version(7, 1),                           default = "")

    _name_aoe1: str                          = Retriever(Str[1],      min_ver = Version(3, 7), max_ver = Version(3, 7),  default = "", repeat = 0)
    _name_aoe2_swgb: str                     = Retriever(Str[1],      min_ver = Version(5, 7), max_ver = Version(5, 9),  default = "", repeat = 0)

    name: str                                = RetrieverCombiner(_name_de2, _name_aoe2_swgb, _name_de1, _name_aoe1)

    name2: str                               = Retriever(str16,       min_ver = Version(5, 9), max_ver = Version(5, 9),  default = "")
    unit_line_id: int                        = Retriever(i16,         min_ver = Version(5, 9), max_ver = Version(5, 9),  default = -1)
    min_tech_level: int                      = Retriever(i8,          min_ver = Version(5, 9), max_ver = Version(5, 9),  default = -1)

    copy_id: int                             = Retriever(i16,                                                            default = -1)
    base_id: int                             = Retriever(i16,          min_ver = Version(5, 7),                          default = -1)

    telemetry_id: int                        = Retriever(i16,          min_ver = Version(4, 5), max_ver = Version(4, 5), default = -1)

    animation_info: AnimationInfo | None     = Retriever(AnimationInfo,                                                  default_factory = AnimationInfo)
    movement_info: MovementInfo | None       = Retriever(MovementInfo,                                                   default_factory = MovementInfo)
    task_info: TaskInfo | None               = Retriever(TaskInfo,                                                       default_factory = TaskInfo)
    combat_info: CombatInfo | None           = Retriever(CombatInfo,                                                     default_factory = CombatInfo)
    projectile_info: ProjectileInfo | None   = Retriever(ProjectileInfo,                                                 default_factory = ProjectileInfo)
    creation_info: CreationInfo | None       = Retriever(CreationInfo,                                                   default_factory = CreationInfo)
    building_info: BuildingInfo | None       = Retriever(BuildingInfo,                                                   default_factory = BuildingInfo)
    # @formatter:on
