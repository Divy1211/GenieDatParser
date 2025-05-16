from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16


class DamageClass(BaseStruct):
    # @formatter:off
    id: int         = Retriever(i16, default = -1)
    amount: int     = Retriever(i16, default = 0)
    # @formatter:on
