from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int8, FixedLenStr, int32, uint8, int16

from src.sections.terrain_data.frame_data import FrameData
from src.sections.terrain_data.terrain_animation import TerrainAnimation


class TerrainBorder(BaseStruct):
    # @formatter:off
    enabled: int                        = Retriever(int8,               default = 0)
    random: int                         = Retriever(int8,               default = 0)
    internal_name: str                  = Retriever(FixedLenStr[13],    default = 0)
    filename: int                       = Retriever(FixedLenStr[13],    default = 0)
    slp_id: int                         = Retriever(int32,              default = 0)
    shape_ptr: int                      = Retriever(int32,              default = 0)
    sound_id: int                       = Retriever(int32,              default = 0)
    color: int                          = Retriever(uint8,              default = 0, repeat = 3)

    terrain_animation: TerrainAnimation = Retriever(TerrainAnimation,   default_factory = TerrainAnimation)
    frames: FrameData                   = Retriever(FrameData,          default_factory = FrameData, repeat = 19*12)

    draw_tile: int                      = Retriever(int16,              default = 0)
    underlay_terrain: int               = Retriever(int16,              default = 0)
    border_style: int                   = Retriever(int16,              default = 0)
    # @formatter:on
