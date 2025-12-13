from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i8, Str, i32, u8, i16, Array, Bytes, u16, bool8

from sections.terrain_data.terrain_sprite_frame import TerrainSpriteFrame
from sections.terrain_data.terrain_animation import TerrainAnimation


class TerrainBorder(BaseStruct):
    # @formatter:off
    enabled: bool                       = Retriever(bool8,                            default = False)
    random: int                         = Retriever(i8,                               default = 0)
    internal_name: str                  = Retriever(Str[13],                          default = "")
    slp_filename: str                   = Retriever(Str[13],                          default = "")
    slp_id: int                         = Retriever(i32,                              default = 0)
    _slp_ptr: bytes                     = Retriever(Bytes[4],                         default = b"\x00" * 4)
    sound_id: int                       = Retriever(i32,                              default = 0)
    color: list[int]                    = Retriever(Array[3][u8],                     default_factory = lambda _ver: [0, 0, 0])

    animation: TerrainAnimation         = Retriever(TerrainAnimation,                 default_factory = TerrainAnimation)
    frames: list[TerrainSpriteFrame]    = Retriever(Array[19*12][TerrainSpriteFrame], default_factory = lambda ver: [TerrainSpriteFrame(ver) for _ in range(19*12)])

    draw_tile: int                      = Retriever(i8,                               default = 0)
    _padding: int                       = Retriever(i8,                               default = 0)

    underlay_terrain: int               = Retriever(u16,                              default = 0)
    border_style: int                   = Retriever(i16,                              default = 0)
    # @formatter:on
