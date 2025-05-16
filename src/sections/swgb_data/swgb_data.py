from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u16, u32


class SwgbData(BaseStruct):
    # @formatter:off
    civ_count: int            = Retriever(u16, default = 0)
    unknown1: int             = Retriever(u32, default = 0)
    unknown2: int             = Retriever(u32, default = 0)
    blend_mode_count: int     = Retriever(u32, default = 0)
    blend_mode_count_max: int = Retriever(u32, default = 0)
    # @formatter:on
