from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i8, i16, f32


class TerrainAnimation(BaseStruct):
    # @formatter:off
    enabled: int               = Retriever(i8, default = 0)
    num_frames: int             = Retriever(i16,   default = 0)
    num_pause_frames: int       = Retriever(i16,   default = 0)
    frame_interval:  float      = Retriever(f32,   default = 0)
    replay_delay: float         = Retriever(f32,   default = 0)
    frame: int                  = Retriever(i16,   default = 0)
    draw_frame: int             = Retriever(i16,   default = 0)
    animate_last: float         = Retriever(f32,   default = 0)
    frame_changed: int         = Retriever(i8, default = 0)
    drawn: int                 = Retriever(i8, default = 0)
    # @formatter:on
