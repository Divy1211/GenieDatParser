from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i16, f32, i8, u8


class MovementInfo(BaseStruct):
    # @formatter:off
    walking_sprite_id: int                        = Retriever(i16,                          default = -1)
    running_sprite_id: int                        = Retriever(i16,                          default = -1)
    rotation_speed: float                         = Retriever(f32,                          default = 0)
    old_size_class: int                           = Retriever(i8,                           default = 0)
    trailing_unit_id: int                         = Retriever(i16,                          default = -1)
    trail_mode: int                               = Retriever(u8,                           default = 0)
    trail_spacing: float                          = Retriever(f32,                          default = 0)
    old_move_algorithm: int                       = Retriever(i8,                           default = 0)

    rotation_radius: float                        = Retriever(f32, min_ver = Version(5, 7), default = 0)
    rotation_radius_speed: float                  = Retriever(f32, min_ver = Version(5, 7), default = 3.402823466e+38) # f32::max
    max_yaw_per_sec_walking: float                = Retriever(f32, min_ver = Version(5, 7), default = 3.402823466e+38) # f32::max
    standing_yaw_revolution_time: float           = Retriever(f32, min_ver = Version(5, 7), default = 0)
    max_yaw_per_sec_standing: float               = Retriever(f32, min_ver = Version(5, 7), default = 3.402823466e+38) # f32::max

    min_collision_size_multiplier: float          = Retriever(f32, min_ver = Version(7, 1), default = 1)
    # @formatter:on
