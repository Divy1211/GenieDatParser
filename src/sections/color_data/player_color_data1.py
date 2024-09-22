from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import FixedLenStr, int16, uint16, uint8


class PlayerColorData1(BaseStruct):

    # @formatter:off
    color_name: str      = Retriever(FixedLenStr[30], default = "0"*30) # todo: default
    id: int              = Retriever(int16,           default = 0)
    resource_id: int     = Retriever(uint16,          default = 0)
    minimap_color: int   = Retriever(uint8,           default = 0)
    type: int            = Retriever(uint8,           default = 0)
    # @formatter:on
