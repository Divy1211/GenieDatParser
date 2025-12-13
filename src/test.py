from src.sections.civilization.type_info import UnitType
from src.sections.datfile_sections import DatFile
from src.utils import timed, format_bytes

def main():
    with timed("read"):
        dat1 = DatFile.from_file(r"../empires2_x2_p1.dat")

    for unit in dat1.civilizations[1].units:
        if unit is None:
            continue
        if unit.base_class < UnitType.Creatable:
            continue

        print(f"======== {unit.name} ========")

        print(f"==== Attack ====")
        for attack in unit.combat_info.attacks:
            print(f"class = {attack.id = }, amount = {attack.amount = }")

        print(f"==== Armor ====")
        for armor in unit.combat_info.armors:
            print(f"class = {armor.id}, amount = {armor.amount = }")

        print(f"{unit.hit_points = }")
        print(f"{unit.combat_info.reload_time = }")

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
