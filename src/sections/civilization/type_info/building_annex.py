from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16, float32


class BuildingAnnex(BaseStruct):
    # @formatter:off
    unit_id: int        = Retriever(int16,      default = -1)
    displacement_x: int = Retriever(float32,    default = 0)
    displacement_y: int = Retriever(float32,    default = 0)
    # @formatter:on
