from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32, u32, Bytes


class MapInfo1(BaseStruct):
    # @formatter:off
    id: int                 = Retriever(i32,      default = 0)
    # all duplicate info. yES
    _border_south_west: int = Retriever(i32,      default = 0)
    _border_north_west: int = Retriever(i32,      default = 0)
    _border_north_east: int = Retriever(i32,      default = 0)
    _border_south_east: int = Retriever(i32,      default = 0)
    _border_fade: int       = Retriever(i32,      default = 0)
    _water_border: int      = Retriever(i32,      default = 0)
    _base_terrain: int      = Retriever(i32,      default = 0)
    _land_percent: int      = Retriever(i32,      default = 0)
    _unused_id: int         = Retriever(i32,      default = 0)
    _num_base_zones: int    = Retriever(u32,      default = 0)
    _base_zone_ptr: bytes   = Retriever(Bytes[4], default = b"\x00" * 4)
    _num_terrains: int      = Retriever(u32,      default = 0)
    _terrain_ptr: bytes     = Retriever(Bytes[4], default = b"\x00" * 4)
    _num_units: int         = Retriever(u32,      default = 0)
    _unit_ptr: bytes        = Retriever(Bytes[4], default = b"\x00" * 4)
    _num_elevations: int    = Retriever(u32,      default = 0)
    _elevation_ptr: bytes   = Retriever(Bytes[4], default = b"\x00" * 4)
    # @formatter:on
