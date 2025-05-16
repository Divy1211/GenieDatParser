from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32


class PlayerColorData2(BaseStruct):
    # @formatter:off
    id: int                      = Retriever(i32, default = 0)
    player_color_base: int       = Retriever(i32, default = 0)
    outline_color: int           = Retriever(i32, default = 0)
    unit_selection_color1: int   = Retriever(i32, default = 0)
    unit_selection_color2: int   = Retriever(i32, default = 0)
    minimap_color1: int          = Retriever(i32, default = 0)
    minimap_color2: int          = Retriever(i32, default = 0)
    minimap_color3: int          = Retriever(i32, default = 0)
    statistics_text_color: int   = Retriever(i32, default = 0)
    # @formatter:on
