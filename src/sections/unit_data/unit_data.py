from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import Array16, Array32, Option8

from sections.unit_data.unit_line import UnitLine
from sections.unit_data.unit_task import UnitTask


class UnitData(BaseStruct):
    unit_lines: list[UnitLine]         = Retriever(Array16[UnitLine],                   min_ver = Version(5, 9), max_ver = Version(5, 9), default_factory = lambda _ver: [])
    tasks: list[list[UnitTask] | None] = Retriever(Array32[Option8[Array16[UnitTask]]], min_ver = Version(5, 7),                          default_factory = lambda _ver: [])
