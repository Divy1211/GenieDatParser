from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, bool8


class TechCost(BaseStruct):
    # @formatter:off
    resource_id: int  = Retriever(i16,    default = 0)
    quantity: int     = Retriever(i16,    default = 0)
    is_deducted: bool = Retriever(bool8, default = True)
    # @formatter:on
