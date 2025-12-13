from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner, ret
from bfp_rs.combinators import set_repeat, set_
from bfp_rs.types.le import i16, u16, i32

from sections.sounds.sound_file import SoundFile

def sound_file_repeat():
    return [
        set_repeat(ret(Sound.sound_files)).from_(Sound.num_sound_files)
    ]

def sync_sound_file_repeat():
    return [
        set_(Sound.num_sound_files).from_len(ret(Sound.sound_files)),
    ]


class Sound(BaseStruct):
    # @formatter:off
    id: int                        = Retriever(i16,                                                         default = 0)
    play_delay: int                = Retriever(u16,                                                         default = 0)
    num_sound_files: int           = Retriever(u16,                                                         default = 0, on_read = sound_file_repeat, on_write = sync_sound_file_repeat)
    cache_time: int                = Retriever(i32,                                                         default = 300000)
    _total_probability_de1: int    = Retriever(i16,       min_ver = Version(4, 5), max_ver = Version(4, 5), default = 100)
    _total_probability_de2: int    = Retriever(i16,       min_ver = Version(7, 1),                          default = 100)
    sound_files: list[SoundFile]   = Retriever(SoundFile,                                                   default_factory = SoundFile, repeat = 0)

    total_probability: int         = RetrieverCombiner(_total_probability_de2, _total_probability_de1)
    # @formatter:on
