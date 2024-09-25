from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16


class FrameData(BaseStruct):
    # @formatter:off
    frame_count: int    = Retriever(int16,      default = 0)
    angle_count: int    = Retriever(int16,      default = 0)
    shape_id: int       = Retriever(int16,      default = 0)
    # @formatter:on
