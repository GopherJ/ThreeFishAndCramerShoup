#!/usr/bin/python3

import constants
import lib

t = [None] * 2
x = [None] * 2
y = [None] * 2
k = []

vd = []
ed = []
fd = []
ksd = []

class cipher_threefish:
    def __init__(self, blockSize, nr, keys, tweak, mode):
        if blockSize not in [256, 512, 1024]:
            print("Error: blockSize must be of [256, 512, 1024]")
            exit(0)

        if nr not in [72, 76, 80]:
            print("Error: nr must be of [72, 76, 80]")
            exit(0)
        
        if len(tweak) != 2:
            print("Error: tweak must be an array of 2 items")
            exit(0)

        self.blockSize = blockSize or constants.BLOCK_SIZE_BITS_512
        self.nr = nr or constants.ROUNDS_76
        self.nw = blockSize/64
        self.mode = mode

        if self.nw == 4:
            self.pi = constants.PI4_NW_4
            self.rpi = constants.RPI4_NW_4
            self.r = constants.R4_4_4
        elif self.nw == 8:
            self.pi = constants.PI8_NW_8
            self.rpi = constants.RPI8_NW_8
            self.r = constants.R8_8_8
        elif self.nw == 16:
            self.pi = constants.PI16_NW_16
            self.rpi = constants.RPI16_NW_16
            self.r = constants.R16_16_16
        
        self.depth = constants.DEPTH_OF_D_IN_R
        t[0], t[1] = tweak[0], tweak[1]
        t.append(tweak[0]^tweak[1])

        self.nk = nr/4 + 1

    # self -> instance of cipher_threefish, decalage r origine de tableR[d][j]
    def mix(self, d, j):
        y[0] = x[0] + x[1]
        y[1] = y[0] ^ (lib.rotl(x[1], self.r[d % self.depth][j]))

    def demix(self, d, j):
        y[1] = y[1] ^ y[0]
        x[1] = lib.rotr(y[1], self.r[d % self.depth][j])
        x[0] = y[0] - x[1]
    
    
        

"""
cl = cipher_threefish(256, 76, 0, [1,2])
       
x[0], x[1] = 18, 25
cl.mix(2,1)
print(y[0], y[1])

cl.demix(2,1)
print(x[0], x[1])
"""
        
        

        


   
