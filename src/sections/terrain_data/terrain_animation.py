from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int8, int16, float32


class TerrainAnimation(BaseStruct):
    # @formatter:off
    is_animated: int            = Retriever(int8,        default = 0)
    animation_frame_count: int  = Retriever(int16,       default = 0)
    pause_frame_count: int      = Retriever(int16,       default = 0)
    interval:  float            = Retriever(float32,     default = 0)
    pause_between_loops: float  = Retriever(float32,     default = 0)
    frame: int                  = Retriever(int16,       default = 0)
    draw_frame: int             = Retriever(int16,       default = 0)
    animate_last: float         = Retriever(float32,     default = 0)
    frame_changed: int          = Retriever(int8,        default = 0)
    drawn: int                  = Retriever(int8,        default = 0)
    # @formatter:on
