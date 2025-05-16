from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i8


class LootingTable(BaseStruct):
    # @formatter:off
    stone_loot_switch: int = Retriever(i8, default = 0)
    wood_loot_switch: int  = Retriever(i8, default = 0)
    ore_loot_switch: int   = Retriever(i8, default = 0)
    gold_loot_switch: int  = Retriever(i8, default = 0)
    food_loot_switch: int  = Retriever(i8, default = 0)
    goods_loot_switch: int = Retriever(i8, default = 0)
    # @formatter:on
