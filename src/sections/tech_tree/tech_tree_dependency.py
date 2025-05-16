from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32


class TechTreeDependency(BaseStruct):
    # @formatter:off
    id: int   = Retriever(i32, default = -1)
    type: int = Retriever(i32, default = 0)
    """
    0 - age
    1 - building
    2 - unit
    3 - tech
    """
    # @formatter:on
