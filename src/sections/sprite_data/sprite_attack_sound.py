from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, uint32


class SpriteAttackSound(BaseStruct):
    # @formatter:off
    sound_delay1: int    = Retriever(int16,                             default = 0)
    sound_id1: int       = Retriever(int16,                             default = 0)
    wwise_sound_id1: int = Retriever(uint32, min_ver = Version((7, 1)), default = 0)
    sound_delay2: int    = Retriever(int16,                             default = 0)
    sound_id2: int       = Retriever(int16,                             default = 0)
    wwise_sound_id2: int = Retriever(uint32, min_ver = Version((7, 1)), default = 0)
    sound_delay3: int    = Retriever(int16,                             default = 0)
    sound_id3: int       = Retriever(int16,                             default = 0)
    wwise_sound_id3: int = Retriever(uint32, min_ver = Version((7, 1)), default = 0)
    # @formatter:on
