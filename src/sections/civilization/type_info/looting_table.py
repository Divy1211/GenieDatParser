from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int8


class LootingTable(BaseStruct):
    # @formatter:off
    stone_loot_switch: int      = Retriever(int8,       default = 0)
    wood_loot_switch: int       = Retriever(int8,       default = 0)
    ore_loot_switch: int        = Retriever(int8,       default = 0)
    gold_loot_switch: int       = Retriever(int8,       default = 0)
    food_loot_switch: int       = Retriever(int8,       default = 0)
    goods_loot_switch: int      = Retriever(int8,       default = 0)
    # @formatter:on
