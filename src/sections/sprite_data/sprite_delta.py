from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, int32


class SpriteDelta(BaseStruct):
    # @formatter:off
    sprite_id: int          = Retriever(int16, default = 0)
    _padding1: int          = Retriever(int16, default = 0)
    _parent_sprite_ptr: int = Retriever(int32, default = 0)
    offset_x: int           = Retriever(int16, default = 0)
    offset_y: int           = Retriever(int16, default = 0)
    display_angle: int      = Retriever(int16, default = 0)
    _padding2: int          = Retriever(int16, default = 0)
    # @formatter:on
