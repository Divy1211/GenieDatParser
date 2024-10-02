## GenieDatParser

This library is a tool for parsing `.dat` files for games like `AoE2` that use the Genie Engine. The implementation has been tested on AoK, AoC, HD/DLCs, and DE2.

## Usage

```py
from src.sections.datfile_sections import DatFile

dat = DatFile.from_file(r"/path/to/empires2_x2_p1.dat")

# make your modifications

dat.to_file("/path/to/empires2_x2_p1_out.dat")
```