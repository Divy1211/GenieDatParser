from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int8, FixedLenStr, int32, uint8, int16, FixedLenArray, bool8, Bytes, uint16

from src.sections.terrain_data.terrain_sprite_frame import TerrainSpriteFrame
from src.sections.terrain_data.terrain_animation import TerrainAnimation


class TerrainBorder(BaseStruct):
    # @formatter:off
    enabled: int                        = Retriever(bool8,                                    default = False)
    random: int                         = Retriever(int8,                                     default = 0)
    internal_name: str                  = Retriever(FixedLenStr[13],                          default = "")
    slp_filename: str                   = Retriever(FixedLenStr[13],                          default = "")
    slp_id: int                         = Retriever(int32,                                    default = 0)
    _slp_ptr: bytes                     = Retriever(Bytes[4],                                 default = b"\x00" * 4)
    sound_id: int                       = Retriever(int32,                                    default = 0)
    color: list[int]                    = Retriever(FixedLenArray[uint8, 3],                                    default = 0)

    animation: TerrainAnimation         = Retriever(TerrainAnimation,                         default_factory = TerrainAnimation)
    frames: list[TerrainSpriteFrame]    = Retriever(FixedLenArray[TerrainSpriteFrame, 19*12], default_factory = TerrainSpriteFrame)

    draw_tile: int                      = Retriever(int8,                                     default = 0)
    _padding: int                        = Retriever(int8,                                     default = 0)

    underlay_terrain: int               = Retriever(uint16,                                   default = 0)
    border_style: int                   = Retriever(int16,                                    default = 0)
    # @formatter:on
