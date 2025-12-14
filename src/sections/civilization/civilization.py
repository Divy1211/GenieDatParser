from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner, ret
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import (
    i8, Bytes, str16, NtStr, u16, i16, Array, f32, u8,
    StackedAttrArray16, Option32
)

from sections.civilization.unit import Unit


def resources_repeat():
    return [
        set_repeat(ret(Civilization.resources)).from_(Civilization.num_resources)
    ]

class Civilization(BaseStruct):
    player_type: int                  = Retriever(i8,                                                              default = 0)

    _str_sign_de1: bytes              = Retriever(Bytes[2],      min_ver = Version(4, 5), max_ver = Version(4, 5), default = b"\x0A\x60")
    _name_de1: str                    = Retriever(str16,         min_ver = Version(4, 5), max_ver = Version(4, 5), default = "")

    _str_sign_de2: bytes              = Retriever(Bytes[2],      min_ver = Version(7, 1),                          default = b"\x0A\x60")
    _name_de2: str                    = Retriever(str16,         min_ver = Version(7, 1),                          default = "")

    _name_aoe1: str                   = Retriever(NtStr[20],     min_ver = Version(3, 7), max_ver = Version(3, 7), default = "")
    _name_aoe2_swgb: str              = Retriever(NtStr[20],     min_ver = Version(5, 7), max_ver = Version(5, 9), default = "")

    name: str                         = RetrieverCombiner(_name_de2, _name_aoe2_swgb, _name_de1, _name_aoe1)

    num_resources: int                = Retriever(u16,                                                             default = 0, on_read = resources_repeat)
    tech_tree_effect_id: int          = Retriever(i16,                                                             default = 0)
    team_bonus_effect_id: int         = Retriever(i16,           min_ver = Version(5, 7),                          default = 0)

    name2: str                        = Retriever(NtStr[20],     min_ver = Version(5, 9), max_ver = Version(5, 9), default = 0)
    unique_unit_effect_ids: list[int] = Retriever(Array[4][i16], min_ver = Version(5, 9), max_ver = Version(5, 9), default_factory = lambda _: [0] * 4)

    resources: list[float]            = Retriever(f32,                                                             default = 0, repeat = 0)
    icon_set: int                     = Retriever(u8,                                                              default = 0)

    units: list[Unit | None]          = Retriever(StackedAttrArray16[Option32[Unit]],                              default_factory = lambda _: [])
