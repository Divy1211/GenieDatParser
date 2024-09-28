from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, float32, int8


class UnitResource(BaseStruct):
    type: int       = Retriever(int16,      default = -1)
    quantity: float = Retriever(float32,    default = 0)
    store_mode: int = Retriever(int8,       default = 0)
