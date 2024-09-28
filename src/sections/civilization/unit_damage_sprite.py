from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, int8


class UnitDamageSprite(BaseStruct):
    sprite_id: int       = Retriever(int16,   default = -1)
    damage_percent: int  = Retriever(int16,   default = 0)
    apply_mode: int      = Retriever(int8,    default = 0)
