from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import float32, int16, int8, uint32, Array16, FixedLenArray

from src.sections.unit_data import UnitTask


class TaskInfo(BaseStruct):
    # @formatter:off
    default_task_id: int                      = Retriever(int16,                                                                         default = -1)
    search_radius: float                      = Retriever(float32,                                                                       default = 0)
    work_rate: float                          = Retriever(float32,                                                                       default = 0)

    _drop_sites_aoe1_de1_aoe2_swgb: list[int] = Retriever(FixedLenArray[int16, 2], min_ver = Version((3, 7)), max_ver = Version((7, 1)), default_factory = lambda _: [-1] * 2)
    _drop_sites1_de2: list[int]               = Retriever(FixedLenArray[int16, 3], min_ver = Version((7, 2)), max_ver = Version((7, 7)), default_factory = lambda _: [-1] * 3)
    _drop_sites2_de2: list[int]               = Retriever(Array16[int16],          min_ver = Version((7, 8)),                            default_factory = lambda _: [])

    drop_site_unit_ids: list[int]             = RetrieverCombiner([_drop_sites2_de2, _drop_sites1_de2, _drop_sites_aoe1_de1_aoe2_swgb])

    task_swap_group: int                      = Retriever(int8,                                                                          default = 0)
    attack_sound_id: int                      = Retriever(int16,                                                                         default = -1)
    move_sound_id: int                        = Retriever(int16,                                                                         default = -1)

    wwise_attack_sound_id: int                = Retriever(uint32, min_ver = Version((7, 1)),                                             default = 0)
    wwise_move_sound_id: int                  = Retriever(uint32, min_ver = Version((7, 1)),                                             default = 0)

    run_mode: int                             = Retriever(int8,                                                                          default = 0)

    _tasks_aoe1_de1: list[UnitTask]           = Retriever(Array16[UnitTask], min_ver = Version((3, 7)), max_ver = Version((4, 5)),       default_factory = lambda _: [])
    _tasks_de2: list[UnitTask]                = Retriever(Array16[UnitTask], min_ver = Version((7, 2)),                                  default_factory = lambda _: [])

    tasks: list[UnitTask]                     = RetrieverCombiner([_tasks_aoe1_de1, _tasks_de2])
    # @formatter:on
