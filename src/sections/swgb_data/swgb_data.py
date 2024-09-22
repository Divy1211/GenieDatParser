from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import uint16, uint32


class SwgbData(BaseStruct):
    # @formatter:off
    civ_count_swgb: int            = Retriever(uint16,        default = 0)
    unknown_swgb1: int             = Retriever(uint32,        default = 0)
    unknown_swgb2: int             = Retriever(uint32,        default = 0)
    blend_mode_count_swgb: int     = Retriever(uint32,        default = 0)
    blend_mode_count_max_swgb: int = Retriever(uint32,        default = 0)
    # @formatter:on
