from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner, ret
from bfp_rs.combinators import set_repeat, set_, if_ver
from bfp_rs.types.le import i32, u8, u16

from sections.tech_tree.tech_tree_age import TechTreeAge
from sections.tech_tree.tech_tree_building import TechTreeBuilding
from sections.tech_tree.tech_tree_tech import TechTreeTech
from sections.tech_tree.tech_tree_unit import TechTreeUnit


def set_repeats():
    return [
        set_repeat(ret(TechTree.ages)).from_(TechTree.num_ages),
        set_repeat(ret(TechTree.buildings)).from_(TechTree.num_buildings),

        if_ver(min = Version(3, 7), max = Version(5, 7, 2)).then(
            set_repeat(ret(TechTree.units)).from_(TechTree._num_units_age1_aoe2_swgb),
        ),
        if_ver(min = Version(5, 9), max = Version(5, 9)).then(
            set_repeat(ret(TechTree.units)).from_(TechTree._num_units_swgb),
        ),
        if_ver(min = Version(7, 1)).then(
            set_repeat(ret(TechTree.units)).from_(TechTree._num_units_de2),
        ),

        set_repeat(ret(TechTree.techs)).from_(TechTree.num_techs),
    ]


def sync_repeats():
    return [
        set_(TechTree.num_ages).from_len(ret(TechTree.ages)),
        set_(TechTree.num_buildings).from_len(ret(TechTree.buildings)),

        if_ver(min = Version(3, 7), max = Version(5, 7, 2)).then(
            set_(TechTree._num_units_age1_aoe2_swgb).from_len(ret(TechTree.units))
        ),
        if_ver(min = Version(5, 9), max = Version(5, 9)).then(
            set_(TechTree._num_units_swgb).from_len(ret(TechTree.units))
        ),
        if_ver(min = Version(7, 1)).then(
            set_(TechTree._num_units_de2).from_len(ret(TechTree.units))
        ),

        set_(TechTree.num_techs).from_len(ret(TechTree.techs)),
    ]

class TechTree(BaseStruct):
    # @formatter:off
    _time_slice: int                    = Retriever(i32,                                                      default = 0)
    _unit_kill_rate: int                = Retriever(i32,                                                      default = 0)
    _unit_kill_total: int               = Retriever(i32,                                                      default = 0)
    _unit_hit_point_rate: int           = Retriever(i32,                                                      default = 0)
    _unit_hit_point_total: int          = Retriever(i32,                                                      default = 0)
    _razing_kill_rate: int              = Retriever(i32,                                                      default = 0)
    _razing_kill_total: int             = Retriever(i32,                                                      default = 0)

    num_ages: int                       = Retriever(u8,                                                       default = 0, on_write = sync_repeats)
    num_buildings: int                  = Retriever(u8,                                                       default = 0)

    _num_units_age1_aoe2_swgb: int      = Retriever(u8,  min_ver = Version(3, 7), max_ver = Version(5, 7, 2), default = 0)
    _num_units_swgb: int                = Retriever(u16, min_ver = Version(5, 9), max_ver = Version(5, 9),    default = 0)
    _num_units_de2: int                 = Retriever(u8,  min_ver = Version(7, 1),                             default = 0)

    num_units: int                      = RetrieverCombiner(_num_units_de2, _num_units_age1_aoe2_swgb, _num_units_swgb)
    num_techs: int                      = Retriever(u8,                                                       default = 0, on_read = set_repeats)
    num_groups: int                     = Retriever(i32,                                                      default = 0)

    ages: list[TechTreeAge]             = Retriever(TechTreeAge,                                              default_factory = TechTreeAge,      repeat = 0)
    buildings: list[TechTreeBuilding]   = Retriever(TechTreeBuilding,                                         default_factory = TechTreeBuilding, repeat = 0)
    units: list[TechTreeUnit]           = Retriever(TechTreeUnit,                                             default_factory = TechTreeUnit,     repeat = 0)
    techs: list[TechTreeTech]           = Retriever(TechTreeTech,                                             default_factory = TechTreeTech,     repeat = 0)
    # @formatter:on
