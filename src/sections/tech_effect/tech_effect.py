from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner
from bfp_rs.types.le import Bytes, str16, NtStr, Array16

from sections.tech_effect.effect_command import EffectCommand


class TechEffect(BaseStruct):
    # @formatter:off
    _str_sign_de1: bytes         = Retriever(Bytes[2],  min_ver = Version(4, 5), max_ver = Version(4, 5), default = b"\x0A\x60")
    _name_de1: str               = Retriever(str16,     min_ver = Version(4, 5), max_ver = Version(4, 5), default = "")

    _str_sign_de2: bytes         = Retriever(Bytes[2],  min_ver = Version(7, 1),                          default = b"\x0A\x60")
    _name_de2: str               = Retriever(str16,     min_ver = Version(7, 1),                          default = "")

    _name_aoe1: str              = Retriever(NtStr[31], min_ver = Version(3, 7), max_ver = Version(3, 7), default = "")
    _name_aoe2_swgb: str         = Retriever(NtStr[31], min_ver = Version(5, 7), max_ver = Version(5, 9), default = "")

    name: str                    = RetrieverCombiner(_name_de2, _name_aoe2_swgb, _name_de1, _name_aoe1)

    effects: list[EffectCommand] = Retriever(Array16[EffectCommand],                                                   default_factory = lambda _: [])
    # @formatter:on
