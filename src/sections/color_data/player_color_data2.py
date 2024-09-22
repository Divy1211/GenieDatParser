from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32


class PlayerColorData2(BaseStruct):
    # @formatter:off
    id: int                      = Retriever(int32,           default = 0)
    player_color_base: int       = Retriever(int32,           default = 0)
    outline_color: int           = Retriever(int32,           default = 0)
    unit_selection_color1: int   = Retriever(int32,           default = 0)
    unit_selection_color2: int   = Retriever(int32,           default = 0)
    minimap_color1: int          = Retriever(int32,           default = 0)
    minimap_color2: int          = Retriever(int32,           default = 0)
    minimap_color3: int          = Retriever(int32,           default = 0)
    statistics_text_color: int   = Retriever(int32,           default = 0)
    # @formatter:on
