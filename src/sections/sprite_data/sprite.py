from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import (
    FixedLenStr, Bytes, str16, uint16, uint32, bool8, int8, int16, FixedLenArray,
    float32, uint8, int32
)

from src.sections.sprite_data.sprite_attack_sound import SpriteAttackSound
from src.sections.sprite_data.sprite_delta import SpriteDelta


class Sprite(BaseStruct):
    @staticmethod
    def set_deltas_repeat(_, instance: Sprite):
        Retriever.set_repeat(Sprite.deltas, instance, instance.num_deltas)

    @staticmethod
    def set_attack_sound_repeat(_, instance: Sprite):
        if instance.angles_have_attack_sounds:
            Retriever.set_repeat(Sprite.attack_sounds, instance, instance.num_graphic_angles)

    @staticmethod
    def sync_num_deltas(_, instance: Sprite):
        instance.num_deltas = len(instance.deltas)

    @staticmethod
    def sync_num_attack_sounds(_, instance: Sprite):
        if (n := len(instance.attack_sounds)) > 0:
            instance.angles_have_attack_sounds = True
            instance.num_graphic_angles = n

    # @formatter:off
    _name_aoe1: str                          = Retriever(FixedLenStr[21], min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = "")
    _file_name_aoe1: str                     = Retriever(FixedLenStr[13], min_ver = Version((3, 7)), max_ver = Version((3, 7)), default = "")

    _str_sign1_de1: bytes                    = Retriever(Bytes[2],        min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = b"\x60\x0A")
    _name_de1: str                           = Retriever(str16,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = "")
    _str_sign2_de1: bytes                    = Retriever(Bytes[2],        min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = b"\x60\x0A")
    _file_name_de1: str                      = Retriever(str16,           min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = "")
    first_frame: int                         = Retriever(uint16,          min_ver = Version((4, 5)), max_ver = Version((4, 5)), default = 0)

    _name_aoe2: str                          = Retriever(FixedLenStr[21], min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = "")
    _file_name_aoe2: str                     = Retriever(FixedLenStr[13], min_ver = Version((5, 7)), max_ver = Version((5, 7)), default = "")

    _name_swgb: str                          = Retriever(FixedLenStr[25], min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = "")
    _file_name_swgb: str                     = Retriever(FixedLenStr[25], min_ver = Version((5, 9)), max_ver = Version((5, 9)), default = "")

    _str_sign1_de2: bytes                    = Retriever(Bytes[2],        min_ver = Version((7, 1)),                            default = b"\x60\x0A")
    _name_de2: str                           = Retriever(str16,           min_ver = Version((7, 1)),                            default = "")
    _str_sign2_de2: bytes                    = Retriever(Bytes[2],        min_ver = Version((7, 1)),                            default = b"\x60\x0A")
    _file_name_de2: str                      = Retriever(str16,           min_ver = Version((7, 1)),                            default = "")
    _str_sign3: bytes                        = Retriever(Bytes[2],        min_ver = Version((7, 1)),                            default = b"\x60\x0A")
    particle_effect_name: str                = Retriever(str16,           min_ver = Version((7, 1)),                            default = "")

    slp_id: int                              = Retriever(int32,                             default = -1)
    is_loaded: bool                          = Retriever(bool8,                             default = False)
    force_player_color: int                  = Retriever(int8,                              default = 0)
    layer: int                               = Retriever(int8,                              default = 0)
    color_table: int                         = Retriever(int16,                             default = -1)
    transparent_selection: bool              = Retriever(bool8,                             default = False)
    bounding_box: list[int]                  = Retriever(FixedLenArray[uint16, 4],          default_factory = lambda _: [0] * 4)
    num_deltas: int                          = Retriever(uint16,                            default = 0, on_read = [set_deltas_repeat], on_write = [sync_num_deltas])
    sound_id: int                            = Retriever(int16,                             default = -1)
    wwise_sound_id: int                      = Retriever(int32, min_ver = Version((7, 1)),  default = 0)

    angles_have_attack_sounds: bool          = Retriever(bool8,                             default = False, on_write = [sync_num_attack_sounds])
    num_frames: int                          = Retriever(uint16,                            default = 0)
    num_graphic_angles: int                  = Retriever(uint16,                            default = 0, on_read = [set_attack_sound_repeat])

    speed_mult: float                        = Retriever(float32,                           default = 0)
    frame_rate: float                        = Retriever(float32,                           default = 0)
    replay_delay: float                      = Retriever(float32,                           default = 0)
    sequence_type: int                       = Retriever(uint8,                             default = 0)
    id: int                                  = Retriever(int16,                             default = -1)
    mirroring_mode: int                      = Retriever(uint8,                             default = 0)
    editor_flag: int                         = Retriever(int8,   min_ver = Version((5, 7)), default = 0)

    deltas: list[SpriteDelta]                = Retriever(SpriteDelta,                       default_factory = SpriteDelta)
    attack_sounds: list[SpriteAttackSound]   = Retriever(SpriteAttackSound,                 default_factory = SpriteAttackSound, repeat = 0)

    name: str      = RetrieverCombiner(_name_de2, _name_aoe2, _name_de1, _name_aoe1, _name_swgb)
    file_name: str = RetrieverCombiner(_file_name_de2, _file_name_aoe2, _file_name_de1, _file_name_aoe1, _file_name_swgb)
    # @formatter:on