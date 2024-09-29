from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import int32, Array8, int8, FixedLenArray, uint8
from binary_file_parser.types.le.array import StackedAttrArray8

from src.sections.tech_tree.tech_tree_dependency import TechTreeDependency


class TechTreeAge(BaseStruct):
    # @formatter:off
    id: int                                        = Retriever(int32, default = -1)
    status: int                                    = Retriever(int8,  default = 2)

    _num_buildings_used_age1: int                  = Retriever(uint8,                                     min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default = 0)
    _buildings_age1: list[int]                     = Retriever(FixedLenArray[int32, 40],                  min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default_factory = lambda _: [-1] * 40)
    _num_units_used_age1: int                      = Retriever(uint8,                                     min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default = 0)
    _units_age1: list[int]                         = Retriever(FixedLenArray[int32, 40],                  min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default_factory = lambda _: [-1] * 40)
    _num_techs_used_age1: int                      = Retriever(uint8,                                     min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default = 0)
    _techs_age1: list[int]                         = Retriever(FixedLenArray[int32, 40],                  min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default_factory = lambda _: [-1] * 40)
    _buildings_age2: list[int]                     = Retriever(Array8[int32],                             min_ver = Version((5, 7)),                               default_factory = lambda _: [])
    _units_age2: list[int]                         = Retriever(Array8[int32],                             min_ver = Version((5, 7)),                               default_factory = lambda _: [])
    _techs_age2: list[int]                         = Retriever(Array8[int32],                             min_ver = Version((5, 7)),                               default_factory = lambda _: [])

    building_ids: list[int]                        = RetrieverCombiner(_buildings_age2, _buildings_age1)
    unit_ids: list[int]                            = RetrieverCombiner(_units_age2, _units_age1)
    tech_ids: list[int]                            = RetrieverCombiner(_techs_age2, _techs_age1)

    num_used_dependencies: int                      = Retriever(int32,                                                                                              default = 0)

    _dependencies_age1: list[TechTreeDependency]   = Retriever(StackedAttrArray8[TechTreeDependency, 5],  min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default_factory = lambda sv: [TechTreeDependency(sv) for _ in range(5)])
    _dependencies_aoe2: list[TechTreeDependency]   = Retriever(StackedAttrArray8[TechTreeDependency, 10], min_ver = Version((5, 7)), max_ver = Version((5, 7, 2)), default_factory = lambda sv: [TechTreeDependency(sv) for _ in range(10)])
    _dependencies_swgb: list[TechTreeDependency]   = Retriever(StackedAttrArray8[TechTreeDependency, 20], min_ver = Version((5, 9)), max_ver = Version((5, 9)),    default_factory = lambda sv: [TechTreeDependency(sv) for _ in range(20)])
    _dependencies_de2: list[TechTreeDependency]    = Retriever(StackedAttrArray8[TechTreeDependency, 10], min_ver = Version((7, 1)),                               default_factory = lambda sv: [TechTreeDependency(sv) for _ in range(10)])

    dependencies: list[TechTreeDependency]         = RetrieverCombiner(_dependencies_de2, _dependencies_aoe2, _dependencies_age1, _dependencies_swgb)

    num_building_levels: int                       = Retriever(int8,                                                                                               default = 0)

    _buildings_per_zone_age1: list[int]            = Retriever(FixedLenArray[int8, 3],                    min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default_factory = lambda _: [0] * 3)
    _buildings_per_zone_aoe2: list[int]            = Retriever(FixedLenArray[int8, 10],                   min_ver = Version((5, 7)), max_ver = Version((5, 7, 2)), default_factory = lambda _: [0] * 10)
    _buildings_per_zone_swgb: list[int]            = Retriever(FixedLenArray[int8, 20],                   min_ver = Version((5, 9)), max_ver = Version((5, 9)),    default_factory = lambda _: [0] * 20)
    _buildings_per_zone_de2: list[int]             = Retriever(FixedLenArray[int8, 10],                   min_ver = Version((7, 1)),                               default_factory = lambda _: [0] * 10)

    buildings_per_zone: list[int]                  = RetrieverCombiner(_buildings_per_zone_de2, _buildings_per_zone_aoe2, _buildings_per_zone_age1, _buildings_per_zone_swgb)

    _group_length_per_zone_age1: list[int]         = Retriever(FixedLenArray[int8, 3],                    min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default_factory = lambda _: [0] * 3)
    _group_length_per_zone_aoe2: list[int]         = Retriever(FixedLenArray[int8, 10],                   min_ver = Version((5, 7)), max_ver = Version((5, 7, 2)), default_factory = lambda _: [0] * 10)
    _group_length_per_zone_swgb: list[int]         = Retriever(FixedLenArray[int8, 20],                   min_ver = Version((5, 9)), max_ver = Version((5, 9)),    default_factory = lambda _: [0] * 20)
    _group_length_per_zone_de2: list[int]          = Retriever(FixedLenArray[int8, 10],                   min_ver = Version((7, 1)),                               default_factory = lambda _: [0] * 10)

    group_length_per_zone: list[int]               = RetrieverCombiner(_group_length_per_zone_de2, _group_length_per_zone_aoe2, _group_length_per_zone_age1, _group_length_per_zone_swgb)

    max_age_length: int                            = Retriever(int8,                                                                                               default = 0)
    node_type: int                                 = Retriever(int32,                                                                                              default = 0)
    """aka line_mode"""
    # @formatter:on
