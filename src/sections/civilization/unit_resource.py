from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, f32, i8


class UnitResource(BaseStruct):
    # @formatter:off
    type: int       = Retriever(i16, default = -1)
    quantity: float = Retriever(f32, default = 0)
    store_mode: int = Retriever(i8,  default = 0)
    # @formatter:on
