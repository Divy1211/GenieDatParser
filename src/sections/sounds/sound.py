from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, uint16, int32

from src.sections.sounds.sound_item import SoundItem


class Sound(BaseStruct):
    @staticmethod
    def set_sound_item_repeat(_, instance: Sound):
        Retriever.set_repeat(Sound.sound_items, instance, instance.file_count)

    # @formatter:off
    id: int                        = Retriever(int16,                                                           default = 0)
    play_delay: int                = Retriever(uint16,                                                          default = 0)
    file_count: int                = Retriever(uint16,                                                          default = 0, on_set = [set_sound_item_repeat])
    cache_time: int                = Retriever(int32,                                                           default = 300000)
    total_probability1: int        = Retriever(int16,     min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 100)
    total_probability2: int        = Retriever(int16,     min_ver = Version((7, 1)),                            default = 100)
    sound_items: list[SoundItem]   = Retriever(SoundItem,                                                       default = SoundItem)
    # @formatter:on
