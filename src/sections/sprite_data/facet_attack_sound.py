from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i16, u32


class FacetAttackSound(BaseStruct):
    # @formatter:off
    sound_delay1: int    = Retriever(i16,                          default = 0)
    sound_id1: int       = Retriever(i16,                          default = 0)
    wwise_sound_id1: int = Retriever(u32, min_ver = Version(7, 1), default = 0)
    sound_delay2: int    = Retriever(i16,                          default = 0)
    sound_id2: int       = Retriever(i16,                          default = 0)
    wwise_sound_id2: int = Retriever(u32, min_ver = Version(7, 1), default = 0)
    sound_delay3: int    = Retriever(i16,                          default = 0)
    sound_id3: int       = Retriever(i16,                          default = 0)
    wwise_sound_id3: int = Retriever(u32, min_ver = Version(7, 1), default = 0)
    # @formatter:on
