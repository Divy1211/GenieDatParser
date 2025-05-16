from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, Bytes


class SpriteDelta(BaseStruct):
    # @formatter:off
    sprite_id: int            = Retriever(i16,      default = 0)
    _padding1: int            = Retriever(i16,      default = 0)
    _parent_sprite_ptr: bytes = Retriever(Bytes[4], default = b"\x00" * 4)
    offset_x: int             = Retriever(i16,      default = 0)
    offset_y: int             = Retriever(i16,      default = 0)
    display_angle: int        = Retriever(i16,      default = 0)
    _padding2: int            = Retriever(i16,      default = 0)
    # @formatter:on
