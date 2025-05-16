from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u8, f32


class ProjectileInfo(BaseStruct):
    # @formatter:off
    projectile_type: int         = Retriever(u8,  default = 0)
    smart_mode: int              = Retriever(u8,  default = 0)
    hit_mode: int                = Retriever(u8,  default = 0)
    vanish_mode: int             = Retriever(u8,  default = 0)
    area_effect_specials: int    = Retriever(u8,  default = 0)
    projectile_arc: float        = Retriever(f32, default = 0)
    # @formatter:on
