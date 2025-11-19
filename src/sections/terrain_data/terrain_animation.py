from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, f32, bool8


class TerrainAnimation(BaseStruct):
    # @formatter:off
    enabled: bool               = Retriever(bool8,    default = False)
    num_frames: int             = Retriever(i16,      default = 0)
    num_pause_frames: int       = Retriever(i16,      default = 0)
    frame_interval:  float      = Retriever(f32,      default = 0)
    replay_delay: float         = Retriever(f32,      default = 0)
    frame: int                  = Retriever(i16,      default = 0)
    draw_frame: int             = Retriever(i16,      default = 0)
    animate_last: float         = Retriever(f32,      default = 0)
    change_frame_flag: bool     = Retriever(bool8,    default = False)
    draw_flag: bool             = Retriever(bool8,    default = False)
    # @formatter:on
