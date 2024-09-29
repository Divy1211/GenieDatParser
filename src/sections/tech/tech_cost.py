from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, bool8


class TechCost(BaseStruct):
    # @formatter:off
    resource_id: int = Retriever(int16, default = 0)
    quantity: int    = Retriever(int16, default = 0)
    enabled: bool    = Retriever(bool8, default = False)
    # @formatter:on
