from src.sections.datfile_sections import DatFile


def main():
    dat = DatFile.from_file(r"C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\dat\empires2_x2_p1.dat", strict = False)

if __name__ == "__main__":
    main()
