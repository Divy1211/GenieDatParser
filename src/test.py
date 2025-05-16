from src.sections.datfile_sections import DatFile
from src.utils import timed


def main():
    with timed("read"):
        dat = DatFile.from_file(r"../empires2_x2_p1.dat")

    with timed("write"):
        DatFile.to_file(r"../dat.dat", dat)

if __name__ == "__main__":
    main()
