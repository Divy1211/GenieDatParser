from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, float32, bool8


class TerrainAnimation(BaseStruct):
    # @formatter:off
    enabled: bool               = Retriever(bool8,       default = False)
    num_frames: int             = Retriever(int16,       default = 0)
    num_pause_frames: int       = Retriever(int16,       default = 0)
    frame_interval:  float      = Retriever(float32,     default = 0)
    replay_delay: float         = Retriever(float32,     default = 0)
    frame: int                  = Retriever(int16,       default = 0)
    draw_frame: int             = Retriever(int16,       default = 0)
    animate_last: float         = Retriever(float32,     default = 0)
    frame_changed: bool         = Retriever(bool8,       default = False)
    drawn: bool                 = Retriever(bool8,       default = False)
    # @formatter:on
