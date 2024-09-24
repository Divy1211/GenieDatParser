from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import uint16, uint32


class SwgbData(BaseStruct):
    # @formatter:off
    civ_count: int            = Retriever(uint16,        default = 0)
    unknown1: int             = Retriever(uint32,        default = 0)
    unknown2: int             = Retriever(uint32,        default = 0)
    blend_mode_count: int     = Retriever(uint32,        default = 0)
    blend_mode_count_max: int = Retriever(uint32,        default = 0)
    # @formatter:on
