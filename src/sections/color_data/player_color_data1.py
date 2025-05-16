from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, u16, u8, NtStr


class PlayerColorData1(BaseStruct):

    # @formatter:off
    color_name: str      = Retriever(NtStr[30], default = "")
    id: int              = Retriever(i16,       default = 0)
    resource_id: int     = Retriever(u16,       default = 0)
    minimap_color: int   = Retriever(u8,        default = 0)
    type: int            = Retriever(u8,        default = 0)
    # @formatter:on
