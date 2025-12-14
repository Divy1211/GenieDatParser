from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner
from bfp_rs.types.le import i16, Array, u16, u32, i8, i32, Bytes, str16, Array16, u8, bool8

from sections.tech.tech_cost import TechCost


class ResearchLocation(BaseStruct):
    # @formatter:off
    location_unit_id: int = Retriever(i16,  default = -1)
    research_time: int    = Retriever(i16,  default = 0)
    button_id: int        = Retriever(u8,   default = 0)
    hotkey_str_id: int    = Retriever(i32,  default = -1)
    # @formatter:on


class Tech(BaseStruct):
    # @formatter:off
    _required_techs_age1: list[int]                 = Retriever(Array[4][i16],             min_ver = Version(3, 7), max_ver = Version(4, 5), default_factory = lambda _ver: [-1] * 4)
    _required_techs_age2: list[int]                 = Retriever(Array[6][i16],             min_ver = Version(5, 7),                          default_factory = lambda _ver: [-1] * 6)

    required_tech_ids: list[int]                    = RetrieverCombiner(_required_techs_age2, _required_techs_age1)

    costs: list[TechCost]                           = Retriever(Array[3][TechCost],                                                          default_factory = lambda ver: [TechCost(ver) for _ in range(3)])

    min_required_techs: int                         = Retriever(i16,                                                                         default = 0)

    civilization_id: int                            = Retriever(i16,                       min_ver = Version(5, 7),                          default = -1)
    full_tech_tree_mode: int                        = Retriever(i16,                       min_ver = Version(5, 7),                          default = 0)
    location_unit_id: int                           = Retriever(i16,                                                max_ver = Version(8, 7), default = -1)

    _name_str_id1: int                              = Retriever(u16,                       min_ver = Version(3, 7), max_ver = Version(7, 4), default = 0)
    _description_str_id1: int                       = Retriever(u16,                       min_ver = Version(3, 7), max_ver = Version(7, 4), default = 0)
    _name_str_id2: int                              = Retriever(u32,                       min_ver = Version(7, 5),                          default = 0)
    _description_str_id2: int                       = Retriever(u32,                       min_ver = Version(7, 5),                          default = 0)

    name_str_id: int                                = RetrieverCombiner(_name_str_id2, _name_str_id1)
    description_str_id: int                         = RetrieverCombiner(_description_str_id2, _description_str_id1)

    research_time: int                              = Retriever(i16,                                                max_ver = Version(8, 7), default = 0)
    effect_id: int                                  = Retriever(i16,                                                                         default = -1)
    type: int                                       = Retriever(i16,                                                                         default = 0)
    icon_id: int                                    = Retriever(i16,                                                                         default = -1)
    button_id: int                                  = Retriever(i8,                                                 max_ver = Version(8, 7), default = 0)
    help_str_id: int                                = Retriever(i32,                                                                         default = 0)
    tech_tree_str_id: int                           = Retriever(i32,                                                                         default = 0)
    hotkey_str_id: int                              = Retriever(i32,                                                max_ver = Version(8, 7), default = -1)

    _str_sign_de1: bytes                            = Retriever(Bytes[2],                  min_ver = Version(4, 5), max_ver = Version(4, 5), default = b"\x0A\x60")
    _name_de1: str                                  = Retriever(str16,                     min_ver = Version(4, 5), max_ver = Version(4, 5), default = "")
    _str_sign_de2: bytes                            = Retriever(Bytes[2],                  min_ver = Version(7, 1),                          default = b"\x0A\x60")
    _name_de2: str                                  = Retriever(str16,                     min_ver = Version(7, 1),                          default = "")

    repeatable: bool                                = Retriever(bool8,                     min_ver = Version(7, 1),                          default = False)

    _name_aoe1: str                                 = Retriever(str16,                     min_ver = Version(3, 7), max_ver = Version(3, 7), default = "")
    _name_aoe2_swgb: str                            = Retriever(str16,                     min_ver = Version(5, 7), max_ver = Version(5, 9), default = "")

    name: str                                       = RetrieverCombiner(_name_de2, _name_aoe2_swgb, _name_de1, _name_aoe1)

    name2: str                                      = Retriever(str16,                     min_ver = Version(5, 9), max_ver = Version(5, 9), default = "")

    research_locations: list[ResearchLocation]      = Retriever(Array16[ResearchLocation], min_ver = Version(8, 8),                          default_factory = lambda ver: [])
    # @formatter:on
