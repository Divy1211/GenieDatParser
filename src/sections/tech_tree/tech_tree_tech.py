from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner
from bfp_rs.types.le import i32, Array8, i8, Array, u8, StackedAttrArray

from sections.tech_tree.tech_tree_dependency import TechTreeDependency


class TechTreeTech(BaseStruct):
    # @formatter:off
    id: int                                        = Retriever(i32,                                                                                           default = -1)
    status: int                                    = Retriever(i8,                                                                                            default = 2)
    building_id: int                               = Retriever(i32,                                                                                           default = -1)

    _num_buildings_used_age1: int                  = Retriever(u8,                                      min_ver = Version(3, 7), max_ver = Version(4, 5),     default = 0)
    _buildings_age1: list[int]                     = Retriever(Array[40][i32],                          min_ver = Version(3, 7), max_ver = Version(4, 5),     default_factory = lambda _ver: [-1] * 40)
    _num_units_used_age1: int                      = Retriever(u8,                                      min_ver = Version(3, 7), max_ver = Version(4, 5),     default = 0)
    _units_age1: list[int]                         = Retriever(Array[40][i32],                          min_ver = Version(3, 7), max_ver = Version(4, 5),     default_factory = lambda _ver: [-1] * 40)
    _num_techs_used_age1: int                      = Retriever(u8,                                      min_ver = Version(3, 7), max_ver = Version(4, 5),     default = 0)
    _techs_age1: list[int]                         = Retriever(Array[40][i32],                          min_ver = Version(3, 7), max_ver = Version(4, 5),     default_factory = lambda _ver: [-1] * 40)
    _buildings_age2: list[int]                     = Retriever(Array8[i32],                             min_ver = Version(5, 7),                              default_factory = lambda _ver: [])
    _units_age2: list[int]                         = Retriever(Array8[i32],                             min_ver = Version(5, 7),                              default_factory = lambda _ver: [])
    _techs_age2: list[int]                         = Retriever(Array8[i32],                             min_ver = Version(5, 7),                              default_factory = lambda _ver: [])

    building_ids: list[int]                        = RetrieverCombiner(_buildings_age2, _buildings_age1)
    unit_ids: list[int]                            = RetrieverCombiner(_units_age2, _units_age1)
    tech_ids: list[int]                            = RetrieverCombiner(_techs_age2, _techs_age1)

    num_used_dependencies: int                     = Retriever(i32,                                                                                           default = 0)

    _dependencies_age1: list[TechTreeDependency]   = Retriever(StackedAttrArray[5][TechTreeDependency],  min_ver = Version(3, 7), max_ver = Version(4, 5),    default_factory = lambda ver: [TechTreeDependency(ver) for _ in range(5)])
    _dependencies_aoe2: list[TechTreeDependency]   = Retriever(StackedAttrArray[10][TechTreeDependency], min_ver = Version(5, 7), max_ver = Version(5, 7, 2), default_factory = lambda ver: [TechTreeDependency(ver) for _ in range(10)])
    _dependencies_swgb: list[TechTreeDependency]   = Retriever(StackedAttrArray[20][TechTreeDependency], min_ver = Version(5, 9), max_ver = Version(5, 9),    default_factory = lambda ver: [TechTreeDependency(ver) for _ in range(20)])
    _dependencies_de2: list[TechTreeDependency]    = Retriever(StackedAttrArray[10][TechTreeDependency], min_ver = Version(7, 1),                             default_factory = lambda ver: [TechTreeDependency(ver) for _ in range(10)])

    dependencies: list[TechTreeDependency]         = RetrieverCombiner(_dependencies_de2, _dependencies_aoe2, _dependencies_age1, _dependencies_swgb)

    group_id: int                                  = Retriever(i32,                                                                                           default = -1)
    """aka vertical_line"""
    location_in_age: int                           = Retriever(i32,                                                                                           default = 0)
    node_type: int                                 = Retriever(i32,                                                                                           default = 0)
    """aka line_mode"""
    # @formatter:on

