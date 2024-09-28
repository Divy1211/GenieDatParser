from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import Array16, bool32

from src.sections.sprite_data.sprite import Sprite

# todo: remove this file
class SpriteData(BaseStruct):
    @staticmethod
    def set_sprite_repeat(_, instance: SpriteData):
        num = sum(instance.sprites_exist)
        Retriever.set_repeat(SpriteData.sprites, instance, num)

    # @formatter:off
    sprites_exist: list[bool]                     = Retriever(Array16[bool32], default_factory = lambda _: [], on_read = [set_sprite_repeat])
    sprites: list[Sprite]                         = Retriever(Sprite,          default_factory = lambda _: [], repeat = 0)
    # @formatter:on
