from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16


class DamageClass(BaseStruct):
    # @formatter:off
    id: int         = Retriever(int16, default = -1)
    amount: int     = Retriever(int16, default = 0)
    # @formatter:on
