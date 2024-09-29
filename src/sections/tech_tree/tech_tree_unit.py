from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import int32, Array8, int8, FixedLenArray, uint8
from binary_file_parser.types.le.array import StackedAttrArray8

from src.sections.tech_tree.tech_tree_dependency import TechTreeDependency


class TechTreeUnit(BaseStruct):
    # @formatter:off
    id: int                                        = Retriever(int32, default = -1)
    status: int                                    = Retriever(int8,  default = 2)
    building_id: int                               = Retriever(int32, default = -1)

    num_used_dependencies: int                     = Retriever(int32,                                                                                              default = 0)

    _dependencies_age1: list[TechTreeDependency]   = Retriever(StackedAttrArray8[TechTreeDependency, 5],  min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default_factory = lambda sv: [TechTreeDependency(sv) for _ in range(5)])
    _dependencies_aoe2: list[TechTreeDependency]   = Retriever(StackedAttrArray8[TechTreeDependency, 10], min_ver = Version((5, 7)), max_ver = Version((5, 7, 2)), default_factory = lambda sv: [TechTreeDependency(sv) for _ in range(10)])
    _dependencies_swgb: list[TechTreeDependency]   = Retriever(StackedAttrArray8[TechTreeDependency, 20], min_ver = Version((5, 9)), max_ver = Version((5, 9)),    default_factory = lambda sv: [TechTreeDependency(sv) for _ in range(20)])
    _dependencies_de2: list[TechTreeDependency]    = Retriever(StackedAttrArray8[TechTreeDependency, 10], min_ver = Version((7, 1)),                               default_factory = lambda sv: [TechTreeDependency(sv) for _ in range(10)])

    dependencies: list[TechTreeDependency]         = RetrieverCombiner(_dependencies_de2, _dependencies_aoe2, _dependencies_age1, _dependencies_swgb)

    group_id: int                                  = Retriever(int32,                                                                                              default = -1)
    """aka vertical_line"""

    _num_units_used_age1: int                      = Retriever(uint8,                                     min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default = 0)
    _units_age1: list[int]                         = Retriever(FixedLenArray[int32, 40],                  min_ver = Version((3, 7)), max_ver = Version((4, 5)),    default_factory = lambda _: [-1] * 40)
    _units_age2: list[int]                         = Retriever(Array8[int32],                             min_ver = Version((5, 7)),                               default_factory = lambda _: [])

    unit_ids: list[int]                            = RetrieverCombiner(_units_age2, _units_age1)

    location_in_age: int                           = Retriever(int32,                                                                                              default = 0)
    """aka level_no"""
    prerequisite_tech_id: int                      = Retriever(int32,                                                                                              default = -1)
    node_type: int                                 = Retriever(int32,                                                                                              default = 0)
    """aka line_mode"""
    enabling_tech_id: int                          = Retriever(int32,                                                                                              default = -1)
    # @formatter:on

