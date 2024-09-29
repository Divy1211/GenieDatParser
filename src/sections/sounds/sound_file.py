from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import str16, FixedLenStr, int32, int16, Bytes


class SoundFile(BaseStruct):
    # @formatter:off
    _str_sign1: bytes    = Retriever(Bytes[2],        min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = b"\x60\x0A")
    _sound_name_de1: str = Retriever(str16,           min_ver = Version((4, 5)), max_ver = Version((4, 5)),    default = "")
    _str_sign2: bytes    = Retriever(Bytes[2],        min_ver = Version((7, 1)),                               default = b"\x60\x0A")
    _sound_name_de2: str = Retriever(str16,           min_ver = Version((7, 1)),                               default = "")
    _filename_swgb: str  = Retriever(FixedLenStr[27], min_ver = Version((5, 9)), max_ver = Version((5, 9)),    default = "0" * 27)
    _filename_aoe1: str  = Retriever(FixedLenStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)),    default = "0" * 13)
    _filename_aoe2: str  = Retriever(FixedLenStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7, 2)), default = "0" * 13)
    resource_id: int     = Retriever(int32,                                                                    default = -1)
    probability: int     = Retriever(int16,                                                                    default = 100)
    civilization_id: int = Retriever(int16,           min_ver = Version((5, 7)),                               default = -1)
    icon_set: int        = Retriever(int16,           min_ver = Version((5, 7)),                               default = -1)

    sound_name: str      = RetrieverCombiner(_sound_name_de2, _sound_name_de1)
    filename: str        = RetrieverCombiner(_filename_aoe2, _filename_aoe1, _filename_swgb)
    # @formatter:on
