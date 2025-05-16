from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, i8


class UnitDamageSprite(BaseStruct):
    # @formatter:off
    sprite_id: int       = Retriever(i16, default = -1)
    damage_percent: int  = Retriever(i16, default = 0)
    apply_mode: int      = Retriever(i8,  default = 0)
    # @formatter:on
