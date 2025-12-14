from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner, ret
from bfp_rs.combinators import set_repeat, if_, set_, if_len
from bfp_rs.types.le import (
    Bytes, str16, u16, i8, i16, Array, f32, u8, i32, NtStr, bool8
)

from sections.sprite_data.facet_attack_sound import FacetAttackSound
from sections.sprite_data.sprite_delta import SpriteDelta

def set_repeats():
    return [
        set_repeat(ret(Sprite.deltas)).from_(Sprite.num_deltas),
        if_(Sprite.facets_have_attack_sounds).then(set_repeat(ret(Sprite.facet_attack_sounds)).from_(Sprite.num_facets))
    ]

def sync_repeats():
    return [
        set_(ret(Sprite.num_deltas)).from_len(ret(Sprite.deltas)),
        if_len(ret(Sprite.facet_attack_sounds)).gt(0).then(
            set_(Sprite.facets_have_attack_sounds).to(True),
            set_(Sprite.num_facets).from_len(ret(Sprite.facet_attack_sounds))
        ),
    ]

class Sprite(BaseStruct):
    # @formatter:off
    _name_aoe1: str                             = Retriever(NtStr[21],     min_ver = Version(3, 7), max_ver = Version(3, 7),    default = "")
    _file_name_aoe1: str                        = Retriever(NtStr[13],     min_ver = Version(3, 7), max_ver = Version(3, 7),    default = "")

    _str_sign1_de1: bytes                       = Retriever(Bytes[2],      min_ver = Version(4, 5), max_ver = Version(4, 5),    default = b"\x0A\x60")
    _name_de1: str                              = Retriever(str16,         min_ver = Version(4, 5), max_ver = Version(4, 5),    default = "")
    _str_sign2_de1: bytes                       = Retriever(Bytes[2],      min_ver = Version(4, 5), max_ver = Version(4, 5),    default = b"\x0A\x60")
    _file_name_de1: str                         = Retriever(str16,         min_ver = Version(4, 5), max_ver = Version(4, 5),    default = "")
    first_frame: int                            = Retriever(u16,           min_ver = Version(4, 5), max_ver = Version(4, 5),    default = 0)

    _name_aoe2: str                             = Retriever(NtStr[21],     min_ver = Version(5, 7), max_ver = Version(5, 7, 2), default = "")
    _file_name_aoe2: str                        = Retriever(NtStr[13],     min_ver = Version(5, 7), max_ver = Version(5, 7, 2), default = "")

    _name_swgb: str                             = Retriever(NtStr[25],     min_ver = Version(5, 9), max_ver = Version(5, 9),    default = "")
    _file_name_swgb: str                        = Retriever(NtStr[25],     min_ver = Version(5, 9), max_ver = Version(5, 9),    default = "")

    _str_sign1_de2: bytes                       = Retriever(Bytes[2],      min_ver = Version(7, 1),                             default = b"\x0A\x60")
    _name_de2: str                              = Retriever(str16,         min_ver = Version(7, 1),                             default = "")
    _str_sign2_de2: bytes                       = Retriever(Bytes[2],      min_ver = Version(7, 1),                             default = b"\x0A\x60")
    _file_name_de2: str                         = Retriever(str16,         min_ver = Version(7, 1),                             default = "")
    _str_sign3: bytes                           = Retriever(Bytes[2],      min_ver = Version(7, 1),                             default = b"\x0A\x60")
    particle_effect_name: str                   = Retriever(str16,         min_ver = Version(7, 1),                             default = "")

    slp_id: int                                 = Retriever(i32,                                                                default = -1)
    is_loaded: bool                             = Retriever(bool8,                                                              default = False)
    force_player_color: int                     = Retriever(i8,                                                                 default = 0)
    layer: int                                  = Retriever(i8,                                                                 default = 0)
    color_table: int                            = Retriever(i16,                                                                default = -1)
    transparent_selection: int                  = Retriever(i8,                                                                 default = 2)
    bounding_box: list[int]                     = Retriever(Array[4][u16],                                                      default_factory = lambda _ver: [0] * 4)
    num_deltas: int                             = Retriever(u16,                                                                default = 0, on_write = sync_repeats)
    sound_id: int                               = Retriever(i16,                                                                default = -1)
    wwise_sound_id: int                         = Retriever(i32,           min_ver = Version(7, 1),                      default = 0)

    facets_have_attack_sounds: bool             = Retriever(bool8,                                                              default = False)
    num_frames: int                             = Retriever(u16,                                                                default = 0)
    num_facets: int                             = Retriever(u16,                                                                default = 0, on_read = set_repeats)

    speed_mult: float                           = Retriever(f32,                                                                default = 0)
    frame_rate: float                           = Retriever(f32,                                                                default = 0)
    replay_delay: float                         = Retriever(f32,                                                                default = 0)
    sequence_type: int                          = Retriever(u8,                                                                 default = 0)
    id: int                                     = Retriever(i16,                                                                default = -1)
    mirroring_mode: int                         = Retriever(u8,                                                                 default = 0)
    editor_mode: int                            = Retriever(i8,            min_ver = Version(5, 7),                             default = 0)

    deltas: list[SpriteDelta]                   = Retriever(SpriteDelta,                                                        default_factory = SpriteDelta,      repeat = 0)
    facet_attack_sounds: list[FacetAttackSound] = Retriever(FacetAttackSound,                                                   default_factory = FacetAttackSound, repeat = 0)

    name: str      = RetrieverCombiner(_name_de2, _name_aoe2, _name_de1, _name_aoe1, _name_swgb)
    file_name: str = RetrieverCombiner(_file_name_de2, _file_name_aoe2, _file_name_de1, _file_name_aoe1, _file_name_swgb)
    # @formatter:on
