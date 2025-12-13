from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import Array16

from sections.color_data.player_color_data1 import PlayerColorData1
from sections.color_data.player_color_data2 import PlayerColorData2


class ColorData(BaseStruct):
    # @formatter:off
    player_color_data_age1: list[PlayerColorData1] = Retriever(Array16[PlayerColorData1], max_ver = Version(4, 5),  default_factory = lambda ver: [PlayerColorData1(ver) for _ in range(16)])
    """aoe1_de1"""
    player_color_data_age2: list[PlayerColorData2] = Retriever(Array16[PlayerColorData2], min_ver = Version(5, 7),  default_factory = lambda ver: [PlayerColorData2(ver) for _ in range(16)])
    """aoe2_swgb_de2"""
    # @formatter:on
