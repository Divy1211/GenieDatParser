from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16


class TerrainSpriteFrame(BaseStruct):
    # @formatter:off
    num_frames: int    = Retriever(int16,      default = 0)
    num_facets: int    = Retriever(int16,      default = 0)
    frame_id: int      = Retriever(int16,      default = 0)
    # @formatter:on
