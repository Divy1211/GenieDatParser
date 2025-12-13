from __future__ import annotations

from zlib_ng import zlib_ng as zlib
from typing import TYPE_CHECKING

from bfp_rs import BaseStruct, Retriever, Version, Context
from bfp_rs.types.le import (
    Bytes, Array16, Array32, StackedAttrArray16, Option32, i16
)

from sections.civilization import Civilization
from sections.color_data import ColorData
from sections.dat_versions import DE_LATEST
from sections.map_data import MapData
from sections.sounds import Sound
from sections.sprite_data import Sprite
from sections.swgb_data import SwgbData
from sections.tech import Tech
from sections.tech_effect import TechEffect
from sections.tech_tree import TechTree
from sections.terrain_data import TerrainData
from sections.terrain_table_data import TerrainTableData
from sections.unit_data import UnitData

if TYPE_CHECKING:
    from bfp_rs import ByteStream

# unused, just for info
def get_num_terrains(struct_ver: Version, num_used_terrains) -> int:
    match (struct_ver, num_used_terrains):
        case (Version(3, 7), _): return 32
        case (Version(4, 5), _): return 96
        case (Version(5, 7), 32): return 32
        case (Version(5, 7), 41): return 42
        case (Version(5, 7), 100): return 100
        case (Version(5, 9), _): return 55
        case (Version(7, _), _): return 200


class DatFile(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    file_version: bytes                      = Retriever(Bytes[8],                                                           default = b"VER 7.8\x00", remaining_compressed = True)
    swgb_data: SwgbData                      = Retriever(SwgbData,         min_ver = Version(5, 9), max_ver = Version(5, 9), default_factory = SwgbData)
    terrain_table_data: TerrainTableData     = Retriever(TerrainTableData,                                                   default_factory = TerrainTableData)
    color_data: ColorData                    = Retriever(ColorData,                                                          default_factory = ColorData)
    sounds: list[Sound]                      = Retriever(Array16[Sound],                                                     default_factory = lambda _ver: [])
    sprites: list[Sprite | None]             = Retriever(StackedAttrArray16[Option32[Sprite]],                               default_factory = lambda _ver: [])
    terrain_data: TerrainData                = Retriever(TerrainData,                                                        default_factory = TerrainData)
    map_data: MapData                        = Retriever(MapData,                                                            default_factory = MapData)
    tech_effects: list[TechEffect]           = Retriever(Array32[TechEffect],                                                default_factory = lambda _ver: [])
    unit_data: UnitData                      = Retriever(UnitData,                                                           default_factory = UnitData)
    civilizations: list[Civilization]        = Retriever(Array16[Civilization],                                              default_factory = lambda _ver: [])
    unknown_swgb1: int                       = Retriever(Bytes[1],       min_ver = Version(5, 9), max_ver = Version(5, 9),   default = b"\x00")
    techs: list[Tech]                        = Retriever(Array16[Tech],                                                      default_factory = lambda _ver: [])
    unknown_swgb2: int                       = Retriever(Bytes[1],       min_ver = Version(5, 9), max_ver = Version(5, 9),   default = b"\x00")
    tech_tree: TechTree                      = Retriever(TechTree,                                                           default_factory = TechTree)
    # @formatter:on

    @classmethod
    def _decompress(cls, bytes_: bytes) -> bytes:
        bytes_ = zlib.decompress(bytes_, -zlib.MAX_WBITS)
        return bytes_

    @classmethod
    def _compress(cls, bytes_: bytes) -> bytes:
        deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed = deflate_obj.compress(bytes_) + deflate_obj.flush()
        return compressed

    @classmethod
    def _get_version(
        cls,
        stream: ByteStream,
        _ver: Version = Version(0),
    ) -> Version:
        ver_str = stream.peek(8)[4:-1].decode("ASCII")
        ver = Version(*map(int, ver_str.split(".")))
        if ver != Version(5, 7):
            return ver
        num_terrains = i16.from_bytes(stream.peek(12)[-2:])
        if num_terrains == 32:
            return Version(5, 7, 0) # AoK
        if num_terrains == 41:
            return Version(5, 7, 1) # AoC/HD
        if num_terrains == 100:
            return Version(5, 7, 2) # HD DLCs
