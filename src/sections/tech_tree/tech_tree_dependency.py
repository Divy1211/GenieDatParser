from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32


class TechTreeDependency(BaseStruct):
    # @formatter:off
    id: int   = Retriever(int32, default = -1)
    type: int = Retriever(int32, default = 0)
    """
    0 - age
    1 - building
    2 - unit
    3 - tech
    """
    # @formatter:on
