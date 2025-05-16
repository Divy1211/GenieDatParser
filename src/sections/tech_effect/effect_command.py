from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i8, i16, f32


class EffectCommand(BaseStruct):
    # @formatter:off
    type: int = Retriever(i8,  default = 0)
    a: int    = Retriever(i16, default = 0)
    b: int    = Retriever(i16, default = 0)
    c: int    = Retriever(i16, default = 0)
    d: int    = Retriever(f32, default = 0)
    # @formatter:on
