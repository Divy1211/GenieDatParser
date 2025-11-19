from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16


class UnitCost(BaseStruct):
    resource_id: int    = Retriever(i16,    default = -1)
    quantity: int       = Retriever(i16,    default = 0)
    deduct_flag: int    = Retriever(i16,    default = 1)
