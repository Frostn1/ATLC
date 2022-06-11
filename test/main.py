"""
A test file to create semi defined .atl files for test runs
"""

import struct

class Casting:
    DITCH_BINARY_START = 2
    
    @staticmethod
    def int_to_bin(val = 0, bit_count = 0) -> str:
        
        return bin(val)[Casting.DITCH_BINARY_START:Casting.DITCH_BINARY_START+bit_count]



class atl_header:
    MODES = [
        8, # 8 bit -> 256 max
        16,# 16 bit
        32, # 32 bit
        64 # 64 bit
    ]
    OVERFLOW_BIT_SIZE = 64
    def __init__(self, atl_mode : int, frames_count : int, index_table : list, colormode : int, overflow_count : int, overflowTable : list) -> None:
        self.atl_mode = atl_mode
        self.frames_count = frames_count
        self.index_table = index_table
        self.colormode = colormode
        self.overflow_count = overflow_count 
        self.overflowTable = overflowTable
    
    def __str__(self) -> str:
        if self.atl_mode not in atl_header.MODES:
            print(f"error occured :\nMode .no {self.atl_mode} not existent.\nCheck current modes for further information, i.e. {', '.join(MODES)}")
            return ""
        base_str = f"ATL{self.atl_mode:08b}{self.frames_count:032b}"
        for index in self.index_table:
            base_str += format(index, f"0{self.atl_mode}b")
        base_str += f"{self.colormode:08b}"
        base_str += format(self.overflow_count, f"0{atl_header.OVERFLOW_BIT_SIZE}b")
        for index in self.overflowTable:
            base_str += format(index, f"0{atl_header.OVERFLOW_BIT_SIZE}b")

        return base_str

PATH = "test.atl"
ATL_HEADER = atl_header(8, 2, [25, 61], 1, 0, [])
def main():
    with open(PATH) as filep:
        print(str(ATL_HEADER))


if __name__ == "__main__":
    main()