from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16


class TerrainSpriteFrame(BaseStruct):
    # @formatter:off
    num_frames: int    = Retriever(i16, default = 0)
    num_facets: int    = Retriever(i16, default = 0)
    frame_id: int      = Retriever(i16, default = 0)
    # @formatter:on
