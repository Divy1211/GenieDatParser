from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16, f32


class BuildingAnnex(BaseStruct):
    # @formatter:off
    unit_id: int        = Retriever(i16, default = -1)
    displacement_x: int = Retriever(f32, default = 0)
    displacement_y: int = Retriever(f32, default = 0)
    # @formatter:on
