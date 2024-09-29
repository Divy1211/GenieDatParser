from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import int16, bool8, FixedLenArray, uint16, uint32, int8, int32, Bytes, str16, bool16

from src.sections.tech.tech_cost import TechCost


class Tech(BaseStruct):
    # @formatter:off
    _required_techs_age1: list[int]                 = Retriever(FixedLenArray[int16, 4], min_ver = Version((3, 7)), max_ver = Version((4, 5)), default_factory = lambda _: [-1] * 4)
    _required_techs_age2: list[int]                 = Retriever(FixedLenArray[int16, 6], min_ver = Version((5, 7)),                            default_factory = lambda _: [-1] * 6)

    required_tech_ids: list[int]                    = RetrieverCombiner(_required_techs_age2, _required_techs_age1)

    costs: list[TechCost]                           = Retriever(FixedLenArray[TechCost, 3],                                                    default_factory = lambda sv: [TechCost(sv) for _ in range(3)])

    min_required_techs: int                         = Retriever(int16,                                                                         default = 0)

    civilization_id: int                            = Retriever(int16,                   min_ver = Version((5, 7)),                            default = -1)
    is_available_in_full_tech_tree: bool            = Retriever(bool16,                  min_ver = Version((5, 7)),                            default = True)
    location_unit_id: int                           = Retriever(int16,                                                                         default = -1)

    _name_str_id1: int                              = Retriever(uint16,                  min_ver = Version((3, 7)), max_ver = Version((7, 4)), default = 0)
    _description_str_id1: int                       = Retriever(uint16,                  min_ver = Version((3, 7)), max_ver = Version((7, 4)), default = 0)
    _name_str_id2: int                              = Retriever(uint32,                  min_ver = Version((7, 5)),                            default = 0)
    _description_str_id2: int                       = Retriever(uint32,                  min_ver = Version((7, 5)),                            default = 0)

    name_str_id: int                                = RetrieverCombiner(_name_str_id2, _name_str_id1)
    description_str_id: int                         = RetrieverCombiner(_description_str_id2, _description_str_id1)

    research_time: int                              = Retriever(int16,                                                                         default = 0)
    effect_id: int                                  = Retriever(int16,                                                                         default = -1)
    type: int                                       = Retriever(int16,                                                                         default = 0)
    icon_id: int                                    = Retriever(int16,                                                                         default = -1)
    button_id: int                                  = Retriever(int8,                                                                          default = 0)
    help_str_id: int                                = Retriever(int32,                                                                         default = 0)
    tech_tree_str_id: int                           = Retriever(int32,                                                                         default = 0)
    hotkey_str_id: int                              = Retriever(int32,                                                                         default = -1)

    _str_sign_de1: bytes                            = Retriever(Bytes[2],                min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = b"\x60\x0A")
    _name_de1: str                                  = Retriever(str16,                   min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = "")
    _str_sign_de2: bytes                            = Retriever(Bytes[2],                min_ver = Version((7, 1)),                            default = b"\x60\x0A")
    _name_de2: str                                  = Retriever(str16,                   min_ver = Version((7, 1)),                            default = "")

    repeatable: bool                                = Retriever(bool8,                   min_ver = Version((7, 1)),                            default = False)

    _name_aoe1: str                                 = Retriever(str16,                   min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = "")
    _name_aoe2_swgb: str                            = Retriever(str16,                   min_ver = Version((5, 7)), max_ver = Version((5, 9)), default = "")

    name: str                                       = RetrieverCombiner(_name_de2, _name_aoe2_swgb, _name_de1, _name_aoe1)

    name2: str                                      = Retriever(str16,                   min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = "")
    # @formatter:on
