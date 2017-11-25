#!/usr/bin/python3

import constants

t = []
x = []
y = []
k = []

vd = []
ed = []
fd = []
ksd = []

class cipher:
    def __init__(self, blockSize, nr, key, tweak):
        if not blockSize in [256, 512, 1024]:
            print("Error: blockSize must be of [256, 512, 1024]")
            exit(0)

        if not nr in [72, 76, 80]
            print("Error: nr must be of [72, 76, 80]")
            exit(0)

        self.blockSize = blockSize or constants.BLOCK_SIZE_BITS_512
        self.nr = nr or constants.ROUNDS_76
        self.nw = blockSize/64

        if nw == 4
            self.pi = constants.PI4_NW_4
            self.rpi = constants.RPI4_NW_4
            self.r = constants.R4_4_4
        elif nw == 8
            self.pi = constants.PI8_NW_8
            self.rpi = constants.RPI8_NW_8
            self.r = constants.R8_8_8
        elif nw == 16
            self.pi = constants.PI16_NW_16
            self.rpi = constants.RPI16_NW_16
            self.r = constants.R16_16_16
        
        self.depth = constants.DEPTH_OF_D_IN_R


        
    t[]

   
