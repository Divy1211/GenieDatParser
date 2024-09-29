from __future__ import annotations

import zlib
from typing import TYPE_CHECKING

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import (
    Bytes, Array16, Array32, StackedAttrArray16, Option32, int16
)

from src.sections.civilization import Civilization
from src.sections.color_data import ColorData
from src.sections.dat_versions import DE_LATEST
from src.sections.map_data import MapData
from src.sections.sounds import Sound
from src.sections.sprite_data import Sprite
from src.sections.swgb_data import SwgbData
from src.sections.tech_effect import TechEffect
from src.sections.terrain_data import TerrainData
from src.sections.terrain_table_data import TerrainTableData
from src.sections.unit_data import UnitData

if TYPE_CHECKING:
    from binary_file_parser import ByteStream

# unused, just for info
def get_num_terrains(struct_ver: Version, num_used_terrains) -> int:
    match (struct_ver, num_used_terrains):
        case (Version((3, 7)), _): return 32
        case (Version((4, 5)), _): return 96
        case (Version((5, 7)), 32): return 32
        case (Version((5, 7)), 41): return 42
        case (Version((5, 7)), 100): return 100
        case (Version((5, 9)), _): return 55
        case (Version((7, _)), _): return 200


class DatFile(BaseStruct):
    # @formatter:off
    file_version: bytes                      = Retriever(Bytes[8],                                                               default = b"VER 7.8\x00")
    swgb_data: SwgbData                      = Retriever(SwgbData,       min_ver = Version((5, 9)), max_ver = Version((5, 9)),   default_factory = SwgbData)
    terrain_table_data: TerrainTableData     = Retriever(TerrainTableData,                                                       default_factory = TerrainTableData)
    color_data: ColorData                    = Retriever(ColorData,                                                              default_factory = ColorData)
    sounds: list[Sound]                      = Retriever(Array16[Sound],                                                         default_factory = lambda _: [])
    sprites: list[Sprite | None]             = Retriever(StackedAttrArray16[Option32[Sprite]],                                   default_factory = lambda _: [])
    terrain_data: TerrainData                = Retriever(TerrainData,                                                            default_factory = TerrainData)
    map_data: MapData                        = Retriever(MapData,                                                                default_factory = MapData)
    tech_effects: list[TechEffect]           = Retriever(Array32[TechEffect],                                                    default_factory = lambda _: [])
    unit_data: UnitData                      = Retriever(UnitData,                                                               default_factory = UnitData)
    civilizations: list[Civilization]        = Retriever(Array16[Civilization],                                                  default_factory = lambda _: [])
    unknown_swgb: int                        = Retriever(Bytes[1],       min_ver = Version((5, 9)), max_ver = Version((5, 9)),   default = 0)
    # technologies: list[Technology]
    # @formatter:on

    @classmethod
    def _decompress(cls, bytes_: bytes) -> bytes:
        return zlib.decompress(bytes_, -zlib.MAX_WBITS)

    @classmethod
    def _compress(cls, bytes_: bytes) -> bytes:
        deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed = deflate_obj.compress(bytes_) + deflate_obj.flush()
        return compressed

    @classmethod
    def _get_version(
        cls,
        stream: ByteStream,
        struct_ver: Version = Version((0,)),
    ) -> Version:
        ver_str = stream.peek(8)[4:-1].decode("ASCII")
        ver = Version(map(int, ver_str.split(".")))
        if ver != Version((5, 7)):
            return ver
        num_terrains = int16._from_bytes(stream.peek(12)[-2:])
        if num_terrains == 32:
            return Version((5, 7, 0)) # AoK
        if num_terrains == 41:
            return Version((5, 7, 1)) # AoC/HD
        if num_terrains == 100:
            return Version((5, 7, 2)) # HD DLCs

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults, **retriever_inits)

    @classmethod
    def from_file(cls, file_name: str, *, file_version: Version = Version((0,)), strict = True) -> DatFile:
        return cls._from_compressed_file(file_name, file_version = file_version, strict = strict)

    def to_file(self, file_name: str, *, show_progress = True) -> DatFile:
        return self._to_compressed_file(file_name, show_progress = show_progress)
