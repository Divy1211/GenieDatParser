from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import float32, int16, int8, uint32, Array16, FixedLenArray

from src.sections.unit_data import UnitTask


class TaskInfo(BaseStruct):
    # @formatter:off
    default_task_id: int                      = Retriever(int16,                                                                         default = -1)
    search_radius: float                      = Retriever(float32,                                                                       default = 0)
    work_rate: float                          = Retriever(float32,                                                                       default = 0)

    _drop_sites_aoe1_de1_aoe2_swgb: list[int] = Retriever(FixedLenArray[int16, 2], min_ver = Version((3, 7)), max_ver = Version((5, 9)), default_factory = lambda _: [])
    _drop_sites_de2: list[int]                = Retriever(FixedLenArray[int16, 3], min_ver = Version((7, 1)),                            default_factory = lambda _: [])

    drop_sites: list[int]                     = RetrieverCombiner([_drop_sites_de2, _drop_sites_aoe1_de1_aoe2_swgb])

    task_swap_group: int                      = Retriever(int8,                                                                          default = 0)
    attack_sound_id: int                      = Retriever(int16,                                                                         default = -1)
    mvoe_sound_id: int                        = Retriever(int16,                                                                         default = -1)

    wwise_attack_sound_id: int                = Retriever(uint32, min_ver = Version((7, 1)),                                             default = 0)
    wwise_move_sound_id: int                  = Retriever(uint32, min_ver = Version((7, 1)),                                             default = 0)

    run_mode: int                             = Retriever(int8,                                                                          default = 0)

    _tasks_aoe1_de1: list[UnitTask]           = Retriever(Array16[UnitTask], min_ver = Version((3, 7)), max_ver = Version((4, 5)),       default = [])
    _tasks_de2: list[UnitTask]                = Retriever(Array16[UnitTask], min_ver = Version((7, 1)),                                  default = [])

    tasks: list[UnitTask]                     = RetrieverCombiner([_tasks_aoe1_de1, _tasks_de2])
    # @formatter:on
