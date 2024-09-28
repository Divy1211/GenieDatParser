from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, uint16, uint8, FixedLenNTStr


class PlayerColorData1(BaseStruct):

    # @formatter:off
    color_name: str      = Retriever(FixedLenNTStr[30], default = "")
    id: int              = Retriever(int16,             default = 0)
    resource_id: int     = Retriever(uint16,            default = 0)
    minimap_color: int   = Retriever(uint8,             default = 0)
    type: int            = Retriever(uint8,             default = 0)
    # @formatter:on
