from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import (
    int8, Bytes, str16, FixedLenNTStr, uint16, int16, FixedLenArray, float32, uint8,
    StackedAttrArray16, Option32
)

from src.sections.civilization.unit import Unit


class Civilization(BaseStruct):
    @staticmethod
    def set_resources_repeat(_, instance: Civilization):
        Retriever.set_repeat(Civilization.resources, instance, instance.num_resources)

    player_type: int                  = Retriever(int8,                                                                          default = 0)

    _str_sign_de1: bytes              = Retriever(Bytes[2],                min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = b"\x60\x0A")
    _name_de1: str                    = Retriever(str16,                   min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = "")

    _str_sign_de2: bytes              = Retriever(Bytes[2],                min_ver = Version((7, 1)),                            default = b"\x60\x0A")
    _name_de2: str                    = Retriever(str16,                   min_ver = Version((7, 1)),                            default = "")

    _name_aoe1: str                   = Retriever(FixedLenNTStr[20],       min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = "")
    _name_aoe2_swgb: str              = Retriever(FixedLenNTStr[20],       min_ver = Version((5, 7)), max_ver = Version((5, 9)), default = "")

    name: str                         = RetrieverCombiner([_name_de2, _name_aoe2_swgb, _name_de1, _name_aoe1])

    num_resources: int                = Retriever(uint16,                                                                        default = 0, on_read = [set_resources_repeat])
    tech_tree_effect_id: int          = Retriever(int16,                                                                         default = 0)
    team_bonus_effect_id: int         = Retriever(int16,                   min_ver = Version((5, 7)),                            default = 0)

    name2: str                        = Retriever(FixedLenNTStr[20],       min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = 0)
    unique_unit_effect_ids: list[int] = Retriever(FixedLenArray[int16, 4], min_ver = Version((5, 9)), max_ver = Version((5, 9)), default_factory = lambda _: [0] * 4)

    resources: list[float]            = Retriever(float32,                                                                       default = 0, repeat = 0)
    icon_set: int                     = Retriever(uint8,                                                                         default = 0)

    units: list[Unit | None]          = Retriever(StackedAttrArray16[Option32[Unit]],                                            default_factory = lambda _: [])
