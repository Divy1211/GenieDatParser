from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int8, int16, float32


class EffectCommand(BaseStruct):
    # @formatter:off
    type: int = Retriever(int8,    default = 0)
    a: int    = Retriever(int16,   default = 0)
    b: int    = Retriever(int16,   default = 0)
    c: int    = Retriever(int16,   default = 0)
    d: int    = Retriever(float32, default = 0)
    # @formatter:on
