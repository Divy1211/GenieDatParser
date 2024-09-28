from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import float32


class AnimationInfo(BaseStruct):
    # @formatter:off
    speed: float = Retriever(float32, default = 0)
    # @formatter:on
