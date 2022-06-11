"""
A test file to create semi defined .atl files for test runs
"""

import struct
import binascii

class Casting:
    DITCH_BINARY_START = 2
    BYTE_SIZE = 8
    @staticmethod
    def int_to_bin(val = 0, bit_count = 0) -> str:
        
        return bin(val)[Casting.DITCH_BINARY_START:Casting.DITCH_BINARY_START+bit_count]

    @staticmethod
    def bin_to_ascii(val = "") -> str:
        if len(val) % 8 != 0:
            val = "0" * val % 8 + val
        # print(f"val {val}")
        new_list = [val[i:i+Casting.BYTE_SIZE] for i in range(0, len(val), Casting.BYTE_SIZE)]
        new_list = [chr(int(i,2)) for i in new_list]
        
        return "".join(new_list)

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
        Casting.bin_to_ascii(f'{self.atl_mode:08b}')
        base_str = f"ATL{Casting.bin_to_ascii(f'{self.atl_mode:08b}')}{Casting.bin_to_ascii(f'{self.frames_count:032b}')}"
        for index in self.index_table:
            base_str += Casting.bin_to_ascii(format(index, f"0{self.atl_mode}b"))
        base_str += Casting.bin_to_ascii(f"{self.colormode:08b}")
        base_str += Casting.bin_to_ascii(format(self.overflow_count, f"0{atl_header.OVERFLOW_BIT_SIZE}b"))
        for index in self.overflowTable:
            base_str += Casting.bin_to_ascii(format(index, f"0{atl_header.OVERFLOW_BIT_SIZE}b"))

        return base_str

PATH = "test.atl"
ATL_HEADER = atl_header(8, 2, [25, 61], 1, 0, [])
def main():
    with open(PATH, 'w') as filep:
        filep.write(str(ATL_HEADER))
        # print(str(ATL_HEADER))

if __name__ == "__main__":
    main()