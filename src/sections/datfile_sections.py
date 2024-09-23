from __future__ import annotations

import zlib
from typing import TYPE_CHECKING

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import Bytes, Array16

from src.sections.color_data import ColorData
from src.sections.dat_versions import DE_LATEST
from src.sections.sounds import Sound
from src.sections.swgb_data import SwgbData
from src.sections.terrain_data import TerrainData

if TYPE_CHECKING:
    from binary_file_parser import ByteStream


class DatFile(BaseStruct):
    # @formatter:off
    file_version: bytes                      = Retriever(Bytes[8],                                                               default = b"VER 7.8\x00")
    swgb_data: SwgbData                      = Retriever(SwgbData,       min_ver = Version((5, 9)), max_ver = Version((5, 9)),   default_factory = SwgbData)
    terrain_data: TerrainData                = Retriever(TerrainData,                                                            default_factory = TerrainData)
    color_data: ColorData                    = Retriever(ColorData,                                                              default_factory = ColorData)
    sounds: list[Sound]                      = Retriever(Array16[Sound],                                                         default_factory = lambda sv: [Sound(sv) for _ in range(685)])
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
        return Version(map(int, ver_str.split(".")))

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults, **retriever_inits)

    @classmethod
    def from_file(cls, file_name: str, *, file_version: Version = Version((0,)), strict = True) -> DatFile:
        return cls._from_compressed_file(file_name, file_version = file_version, strict = strict)

    def to_file(self, file_name: str, *, show_progress = True) -> DatFile:
        return self._to_compressed_file(file_name, show_progress = show_progress)
