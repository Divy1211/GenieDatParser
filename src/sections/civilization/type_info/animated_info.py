from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import f32


class AnimationInfo(BaseStruct):
    # @formatter:off
    speed: float = Retriever(f32, default = 0)
    # @formatter:on
