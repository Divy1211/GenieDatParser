from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, i8


class TechCost(BaseStruct):
    # @formatter:off
    resource_id: int  = Retriever(i16,    default = 0)
    quantity: int     = Retriever(i16,    default = 0)
    deduct_flag: bool = Retriever(i8,     default = 0)
    # @formatter:on
