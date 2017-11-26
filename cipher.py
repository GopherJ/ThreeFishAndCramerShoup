#!/usr/bin/python3

import constants
import lib

t = [3,4] 
k = [None]  

'''vd = []
ed = []
fd = []
ksd = []
'''
r_x=5 
r_y=4

#nr number of round 
#mode ecb or cbc  
#
class cipher_threefish:
    def __init__(self, blockSize, nr, key_originate, tweak, mode, key, c_bloc):

        if blockSize not in [256, 512, 1024]:
            print("Error: blockSize must be of [256, 512, 1024]")
            exit(0)

        if nr not in [72, 76, 80]:
            print("Error: nr must be of [72, 76, 80]")
            exit(0)
        
        if len(tweak) != 2:
            print("Error: tweak must be an array of 2 items")
            exit(0)

        self.t = [None]*3
        self.t[0], self.t[1] = tweak[0], tweak[1]
        self.t[2] =  tweak[0] ^ tweak[1]
        self.blockSize = blockSize or constants.BLOCK_SIZE_BITS_512
        #nr is the total number of rounds 
        self.nr = nr or constants.ROUNDS_76
        #nw is the total number of words 
        self.nw  = blockSize/64
        self.mode = mode

        #c_bloc is the bloc of bytes to cipher
        self.c_bloc = c_bloc        
        #generation of the first round's sub key calculated by the key and tweak 
        self.sub_key = key[0:len(key)]
        self.k = key
        # k is the copy ot the originate key used by key_update()
        for i in range(self.nw-3):
            self.sub_key[i] = key[i]
        self.sub_key[self.nw-3] = ( key[self.nw-3] + self.t[0] ) % 2**64
        self.sub_key[self.nw-2] = ( key[self.nw-2] + self.t[1] ) % 2**64
        self.sub_key[self.nw-1] = key[self.nw-1] 

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
    '''def mix(self, d, j):
        y[0] = x[0] + x[1]
        y[1] = y[0] ^ (lib.rotl(x[1], self.r[d % self.depth][j]))
    '''

    def mix(self, r_x, r_y, np):
        self.c_bloc[np] = self.c_bloc[np] + self.c_bloc[np+1]
        self.c_bloc[np] = self.c_bloc[np]^ (lib.rotl(self.c_bloc[np+1], self.r[r_x % self.depth][r_y]))

    
    '''
    def demix(self, d, j):
        y[1] = y[1] ^ y[0]
        x[1] = lib.rotr(y[1], self.r[d % self.depth][j])
        x[0] = y[0] - x[1]
    '''
    def demix(self, r_x, r_y, np):
        self.c_bloc[np] = self.c_bloc[np] ^ self.c_bloc[np+1]
        self.c_bloc[np+1] = lib.rotr(self.c_bloc[np], self.r[r_x % self.depth][r_y])
        self.c_bloc[np] = self.c_bloc[np] - self.c_bloc[np+1]

    # update the subkey (executed after the end of one round's calculation) for the next round
    def key_update(self, c_round):
        for i in range(self.blockSize-3):
            self.sub_key[i] = self.k[(c_round+i)%(self.blockSize+1)]
        self.sub_key[self.nw-3] = ( self.k[(c_round+self.nw-3)%(self.blockSize+1)] + self.t[c_round%3] ) % (2**64)
        self.sub_key[self.nw-2] = ( self.k[(c_round+self.nw-2)%(self.blockSize+1)] + self.t[(c_round+1)%3] ) % (2**64)
        self.sub_key[self.nw-3] = ( self.k[(c_round+self.nw-3)%(self.blockSize+1)] + c_round ) % (2**64)
         



 
        

"""
cl = cipher_threefish(256, 76, 0, [1,2])
       
x[0], x[1] = 18, 25
cl.mix(2,1)
print(y[0], y[1])

cl.demix(2,1)
print(x[0], x[1])

c_t:ciphertext

for i in range(nr): 
    if (i%4==0): 
        addition(subkey,text)
        c1.key_update(i)
    for j in range(self.blocksize/2): c1.mix(self,R_x,R_y,j)
    c1.permutation(c_t,pi)

"""
        
        

        


   
