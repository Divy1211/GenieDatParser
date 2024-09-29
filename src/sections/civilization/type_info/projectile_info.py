from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import uint8, float32


class ProjectileInfo(BaseStruct):
    # @formatter:off
    projectile_type: int         = Retriever(uint8,      default = 0)
    smart_mode: int              = Retriever(uint8,      default = 0)
    hit_mode: int                = Retriever(uint8,      default = 0)
    vanish_mode: int             = Retriever(uint8,      default = 0)
    area_effect_specials: int    = Retriever(uint8,      default = 0)
    projectile_arc: float        = Retriever(float32,    default = 0)
    # @formatter:on
