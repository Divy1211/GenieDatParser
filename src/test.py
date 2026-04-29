from pprint import pprint

from sections.dat_versions import DE_LATEST
from sections.tech import Tech
from sections.tech_effect import TechEffect
from src.sections.civilization.type_info import UnitType
from src.sections.datfile_sections import DatFile
from src.utils import timed, format_bytes

def main():
    with timed("read"):
        dat = DatFile.from_file(r"../empires2_x2_p1.dat")

    with timed("write"):
        dat.to_file("../empires2_x2_p1_2.dat")

    # dat = DatFile.from_json(r"../dtest.json")
    # dat = DatFile()
    # dat2 = DatFile.from_file(r"../empires2_x2_p1_unmodified.dat")
    # dat1.to_file(r"../empires2_x2_p1_unmodified.dat")

    # with open("../empires2_x2_p1_unmodified.dat", "rb") as f, open("../empires2_x2_p1.dat", "rb") as g:
    #     b1 = DatFile._decompress(f.read())
    #     b2 = DatFile._decompress(g.read())
    #
    # with open("../test1.txt", "w") as file:
    #     file.write(format_bytes(b1))
    #
    # with open("../test2.txt", "w") as file:
    #     file.write(format_bytes(b2))

    # with timed("write_json"):
    #     dat.to_json("../dtest.json")

if __name__ == "__main__":
    main()
