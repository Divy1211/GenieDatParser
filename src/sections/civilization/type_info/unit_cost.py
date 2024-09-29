from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, bool16


class UnitCost(BaseStruct):
    resource_id: int    = Retriever(int16,      default = -1)
    quantity: int       = Retriever(int16,      default = 0)
    is_deducted: bool   = Retriever(bool16,     default = True)
