from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import uint32, Bytes

from src.sections.map_data.map_info2 import MapInfo2
from src.sections.map_data.map_info1 import MapInfo1


class MapData(BaseStruct):
    @staticmethod
    def set_map_repeats(_, instance: MapData):
        Retriever.set_repeat(MapData.map_info1, instance, instance.num_maps)
        Retriever.set_repeat(MapData.map_info2, instance, instance.num_maps)

    # @formatter:off
    num_maps: int             = Retriever(uint32,   default = 0, on_set = [set_map_repeats])
    _map_ptr: bytes           = Retriever(Bytes[4], default = b"\x00" * 4)
    map_info1: list[MapInfo1] = Retriever(MapInfo1, default_factory = lambda _: []) # does this need to be synced with map_info2?
    map_info2: list[MapInfo2] = Retriever(MapInfo2, default_factory = lambda _: [])
    # @formatter:on
