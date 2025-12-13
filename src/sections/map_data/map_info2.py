from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat, set_
from bfp_rs.types.le import i32, u32, Bytes

from sections.map_data.map_elevation import MapElevation
from sections.map_data.map_land import MapLand
from sections.map_data.map_terrain import MapTerrain
from sections.map_data.map_unit import MapUnit


def set_lands_repeat():
    return [
        set_repeat(ret(MapInfo2.lands)).from_(MapInfo2.num_lands)
    ]


def set_terrains_repeat():
    return [
        set_repeat(ret(MapInfo2.terrains)).from_(MapInfo2.num_terrains)
    ]


def set_units_repeat():
    return [
        set_repeat(ret(MapInfo2.units)).from_(MapInfo2.num_units)
    ]


def set_elevations_repeat():
    return [
        set_repeat(ret(MapInfo2.elevations)).from_(MapInfo2.num_elevations)
    ]

def sync_repeats():
    return [
        set_(MapInfo2.num_lands).from_len(ret(MapInfo2.lands)),
        set_(MapInfo2.num_terrains).from_len(ret(MapInfo2.terrains)),
        set_(MapInfo2.num_units).from_len(ret(MapInfo2.units)),
        set_(MapInfo2.num_elevations).from_len(ret(MapInfo2.elevations)),
    ]

class MapInfo2(BaseStruct):
    # @formatter:off
    border_south_west: int          = Retriever(i32,          default = 0)
    border_north_west: int          = Retriever(i32,          default = 0)
    border_north_east: int          = Retriever(i32,          default = 0)
    border_south_east: int          = Retriever(i32,          default = 0)
    border_fade: int                = Retriever(i32,          default = 0)
    water_border: int               = Retriever(i32,          default = 0)
    base_terrain: int               = Retriever(i32,          default = 0)
    land_percent: int               = Retriever(i32,          default = 0)
    unused_id: int                  = Retriever(i32,          default = 0)

    num_lands: int                  = Retriever(u32,          default = 0, on_read = set_lands_repeat, on_write = sync_repeats)
    _land_ptr: bytes                = Retriever(Bytes[4],     default = b"\x00" * 4)
    lands: list[MapLand]            = Retriever(MapLand,      default_factory = MapLand, repeat = 0)

    num_terrains: int               = Retriever(u32,          default = 0, on_read = set_terrains_repeat)
    _terrain_ptr: bytes             = Retriever(Bytes[4],     default = b"\x00" * 4)
    terrains: list[MapTerrain]      = Retriever(MapTerrain,   default_factory = MapTerrain, repeat = 0)

    num_units: int                  = Retriever(u32,          default = 0, on_read = set_units_repeat)
    _unit_ptr: bytes                = Retriever(Bytes[4],     default = b"\x00" * 4)
    units: list[MapUnit]            = Retriever(MapUnit,      default_factory = MapUnit, repeat = 0)

    num_elevations: int             = Retriever(u32,          default = 0, on_read = set_elevations_repeat)
    _elevation_ptr: bytes           = Retriever(Bytes[4],     default = b"\x00" * 4)
    elevations: list[MapElevation]  = Retriever(MapElevation, default_factory = MapElevation, repeat = 0)
    # @formatter:on
