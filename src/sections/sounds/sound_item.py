from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint16, str16, FixedLenStr, int32, int16


class SoundItem(BaseStruct):
    # @formatter:off
    len_name_debug1: int        = Retriever(uint16,          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)
    sound_name1: str            = Retriever(str16,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = "")
    len_name_debug2: int        = Retriever(uint16,          min_ver = Version((7, 1)),                            default = 2656)
    sound_name2: str            = Retriever(str16,           min_ver = Version((7, 1)),                            default = "")
    filename_swgb: str          = Retriever(FixedLenStr[27], min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = "0" * 27)
    filename1: str              = Retriever(FixedLenStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = "0" * 13)
    filename2: str              = Retriever(FixedLenStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = "0" * 13)
    resource_id: int            = Retriever(int32,                                                                 default = -1)
    probability: int            = Retriever(int16,                                                                 default = 100)
    civilization_id: int        = Retriever(int16,           min_ver = Version((5, 7)),                            default = -1)
    icon_set: int               = Retriever(int16,           min_ver = Version((5, 7)),                            default = -1)
    # @formatter:on
