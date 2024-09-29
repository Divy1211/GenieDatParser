from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import int32, uint8, uint16

from src.sections.tech_tree.tech_tree_age import TechTreeAge
from src.sections.tech_tree.tech_tree_building import TechTreeBuilding
from src.sections.tech_tree.tech_tree_tech import TechTreeTech
from src.sections.tech_tree.tech_tree_unit import TechTreeUnit


class TechTree(BaseStruct):
    @staticmethod
    def set_repeats(_, instance: TechTree):
        Retriever.set_repeat(TechTree.ages, instance, instance.num_ages)
        Retriever.set_repeat(TechTree.buildings, instance, instance.num_buildings)
        Retriever.set_repeat(TechTree.units, instance, instance.num_units)
        Retriever.set_repeat(TechTree.techs, instance, instance.num_techs)

    @staticmethod
    def sync_repeats(_, instance: TechTree):
        instance.num_ages = len(instance.ages)
        instance.num_buildings = len(instance.buildings)
        instance.num_units = len(instance.units)
        # instance.num_techs = len(instance.techs)

    # @formatter:off
    _time_slice: int                    = Retriever(int32,                                                            default = 0)
    _unit_kill_rate: int                = Retriever(int32,                                                            default = 0)
    _unit_kill_total: int               = Retriever(int32,                                                            default = 0)
    _unit_hit_point_rate: int           = Retriever(int32,                                                            default = 0)
    _unit_hit_point_total: int          = Retriever(int32,                                                            default = 0)
    _razing_kill_rate: int              = Retriever(int32,                                                            default = 0)
    _razing_kill_total: int             = Retriever(int32,                                                            default = 0)

    num_ages: int                       = Retriever(uint8,                                                            default = 0, on_write = [sync_repeats])
    num_buildings: int                  = Retriever(uint8,                                                            default = 0)

    _num_units_swgb: int                = Retriever(uint16, min_ver = Version((5, 9)), max_ver = Version((5, 9)),     default = 0)
    _num_units_age1_aoe2_swgb: int      = Retriever(uint8,  min_ver = Version((3, 7)), max_ver = Version((5, 7, 2)),  default = 0)
    _num_units_de2: int                 = Retriever(uint8,  min_ver = Version((7, 1)),                                default = 0)

    num_units: int                      = RetrieverCombiner(_num_units_de2, _num_units_age1_aoe2_swgb, _num_units_swgb)
    num_techs: int                      = Retriever(uint8,                                                            default = 0, on_read = [set_repeats])
    num_groups: int                     = Retriever(int32,                                                            default = 0)

    ages: list[TechTreeAge]             = Retriever(TechTreeAge,                                                      default_factory = TechTreeAge)
    buildings: list[TechTreeBuilding]   = Retriever(TechTreeBuilding,                                                 default_factory = TechTreeBuilding)
    units: list[TechTreeUnit]           = Retriever(TechTreeUnit,                                                     default_factory = TechTreeUnit)
    techs: list[TechTreeTech]           = Retriever(TechTreeTech,                                                     default_factory = TechTreeTech)
    # @formatter:on
