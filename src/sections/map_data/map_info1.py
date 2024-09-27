from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32, uint32, Bytes


class MapInfo1(BaseStruct):
    # @formatter:off
    id: int                 = Retriever(int32,    default = 0)
    # all duplicate info. yES
    _border_south_west: int = Retriever(int32,    default = 0)
    _border_north_west: int = Retriever(int32,    default = 0)
    _border_north_east: int = Retriever(int32,    default = 0)
    _border_south_east: int = Retriever(int32,    default = 0)
    _border_fade: int       = Retriever(int32,    default = 0)
    _water_border: int      = Retriever(int32,    default = 0)
    _base_terrain: int      = Retriever(int32,    default = 0)
    _land_percent: int      = Retriever(int32,    default = 0)
    _unused_id: int         = Retriever(int32,    default = 0)
    _num_base_zones: int    = Retriever(uint32,   default = 0)
    _base_zone_ptr: bytes   = Retriever(Bytes[4], default = b"\x00" * 4)
    _num_terrains: int      = Retriever(uint32,   default = 0)
    _terrain_ptr: bytes     = Retriever(Bytes[4], default = b"\x00" * 4)
    _num_units: int         = Retriever(uint32,   default = 0)
    _unit_ptr: bytes        = Retriever(Bytes[4], default = b"\x00" * 4)
    _num_elevations: int    = Retriever(uint32,   default = 0)
    _elevation_ptr: bytes   = Retriever(Bytes[4], default = b"\x00" * 4)
    # @formatter:on
