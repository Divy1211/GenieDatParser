from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import u32, Bytes

from sections.map_data.map_info2 import MapInfo2
from sections.map_data.map_info1 import MapInfo1


def map_repeats():
    return [
        set_repeat(ret(MapData.map_info1)).from_(MapData.num_maps),
        set_repeat(ret(MapData.map_info2)).from_(MapData.num_maps),
    ]

class MapData(BaseStruct):
    # @formatter:off
    num_maps: int             = Retriever(u32,      default = 0, on_read = map_repeats)
    _map_ptr: bytes           = Retriever(Bytes[4], default = b"\x00" * 4)
    map_info1: list[MapInfo1] = Retriever(MapInfo1, default_factory = lambda _ver: [], repeat = 0) # does this need to be synced with map_info2?
    map_info2: list[MapInfo2] = Retriever(MapInfo2, default_factory = lambda _ver: [], repeat = 0)
    # @formatter:on
