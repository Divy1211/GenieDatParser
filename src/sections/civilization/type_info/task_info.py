from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverCombiner
from bfp_rs.types.le import f32, i16, i8, u32, Array16, Array

from sections.unit_data import UnitTask


class TaskInfo(BaseStruct):
    # @formatter:off
    default_task_id: int                      = Retriever(i16,                                                                 default = -1)
    search_radius: float                      = Retriever(f32,                                                                 default = 0)
    work_rate: float                          = Retriever(f32,                                                                 default = 0)

    _drop_sites_aoe1_de1_aoe2_swgb: list[int] = Retriever(Array[2][i16],     min_ver = Version(3, 7), max_ver = Version(7, 1), default_factory = lambda _ver: [-1] * 2)
    _drop_sites1_de2: list[int]               = Retriever(Array[3][i16],     min_ver = Version(7, 2), max_ver = Version(7, 7), default_factory = lambda _ver: [-1] * 3)
    _drop_sites2_de2: list[int]               = Retriever(Array16[i16],      min_ver = Version(7, 8),                          default_factory = lambda _ver: [])

    drop_site_unit_ids: list[int]             = RetrieverCombiner(_drop_sites2_de2, _drop_sites1_de2, _drop_sites_aoe1_de1_aoe2_swgb)

    task_swap_group: int                      = Retriever(i8,                                                                  default = 0)
    attack_sound_id: int                      = Retriever(i16,                                                                 default = -1)
    move_sound_id: int                        = Retriever(i16,                                                                 default = -1)

    wwise_attack_sound_id: int                = Retriever(u32,               min_ver = Version(7, 1),                          default = 0)
    wwise_move_sound_id: int                  = Retriever(u32,               min_ver = Version(7, 1),                          default = 0)

    run_mode: int                             = Retriever(i8,                                                                  default = 0)

    _tasks_aoe1_de1: list[UnitTask]           = Retriever(Array16[UnitTask], min_ver = Version(3, 7), max_ver = Version(4, 5), default_factory = lambda _ver: [])
    _tasks_de2: list[UnitTask]                = Retriever(Array16[UnitTask], min_ver = Version(7, 2),                          default_factory = lambda _ver: [])

    tasks: list[UnitTask]                     = RetrieverCombiner(_tasks_aoe1_de1, _tasks_de2)
    # @formatter:on
