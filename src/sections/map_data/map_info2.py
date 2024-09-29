from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32, uint32, Bytes

from src.sections.map_data.map_elevation import MapElevation
from src.sections.map_data.map_land import MapLand
from src.sections.map_data.map_terrain import MapTerrain
from src.sections.map_data.map_unit import MapUnit


class MapInfo2(BaseStruct):
    @staticmethod
    def set_lands_repeat(_, instance: MapInfo2):
        Retriever.set_repeat(MapInfo2.lands, instance, instance.num_lands)

    @staticmethod
    def set_terrains_repeat(_, instance: MapInfo2):
        Retriever.set_repeat(MapInfo2.terrains, instance, instance.num_terrains)

    @staticmethod
    def set_units_repeat(_, instance: MapInfo2):
        Retriever.set_repeat(MapInfo2.units, instance, instance.num_units)

    @staticmethod
    def set_elevations_repeat(_, instance: MapInfo2):
        Retriever.set_repeat(MapInfo2.elevations, instance, instance.num_elevations)

    @staticmethod
    def sync_repeats(_, instance: MapInfo2):
        instance.num_lands = instance.lands
        instance.num_terrains = instance.terrains
        instance.num_units = instance.units
        instance.num_elevations = instance.elevations

    # @formatter:off
    border_south_west: int          = Retriever(int32,        default = 0)
    border_north_west: int          = Retriever(int32,        default = 0)
    border_north_east: int          = Retriever(int32,        default = 0)
    border_south_east: int          = Retriever(int32,        default = 0)
    border_fade: int                = Retriever(int32,        default = 0)
    water_border: int               = Retriever(int32,        default = 0)
    base_terrain: int               = Retriever(int32,        default = 0)
    land_percent: int               = Retriever(int32,        default = 0)
    unused_id: int                  = Retriever(int32,        default = 0)

    num_lands: int                  = Retriever(uint32,       default = 0, on_read = [set_lands_repeat], on_write = [sync_repeats])
    _land_ptr: bytes                = Retriever(Bytes[4],     default = b"\x00" * 4)
    lands: list[MapLand]            = Retriever(MapLand,      default_factory = MapLand, repeat = 0)

    num_terrains: int               = Retriever(uint32,       default = 0, on_read = [set_terrains_repeat])
    _terrain_ptr: bytes             = Retriever(Bytes[4],     default = b"\x00" * 4)
    terrains: list[MapTerrain]      = Retriever(MapTerrain,   default_factory = MapTerrain, repeat = 0)

    num_units: int                  = Retriever(uint32,       default = 0, on_read = [set_units_repeat])
    _unit_ptr: bytes                = Retriever(Bytes[4],     default = b"\x00" * 4)
    units: list[MapUnit]            = Retriever(MapUnit,      default_factory = MapUnit, repeat = 0)

    num_elevations: int             = Retriever(uint32,       default = 0, on_read = [set_elevations_repeat])
    _elevation_ptr: bytes           = Retriever(Bytes[4],     default = b"\x00" * 4)
    elevations: list[MapElevation]  = Retriever(MapElevation, default_factory = MapElevation, repeat = 0)
    # @formatter:on
