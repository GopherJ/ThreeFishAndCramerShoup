#!/usr/bin/python3 

#chr(ascii) ->char   ascii(0~255)
#unichr(unicode)->char  
#ord(char) ->ascii

#print(ord('c'))   char->ascii 
#print(bin(ord('c'))) char->ascii->0b 

#'sep'.join(seq) 
#str.replace(old, new[, max])

lfsr_mode = [ [1,4], 
            [1,3],
            [3,4,5,7],
            [1,4,7] 
          ]


        
lfsr_init_str = ['0','1','0','1','0','1','1']

def encode(s): 
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
   # return ' '.join([bin(ord(c)) for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

def lfsr(lfsr_init_str):
    key = lfsr_init_str
    while len(key) < 65 :
        key.append( key[(len(key)-1)]^key[(len(key)-3)])
        #print(key)
    print("key generated de 64 bits:")
    print(key)
    return key 


def lfsr_64bits(lfsr_init_str, l_mode):
    key = lfsr_init_str[0:len(lfsr_init_str)]
    new_bit = lfsr_init_str[l_mode[0]]
    print(len(lfsr_init_str),len(key))
    while len(key) < 64 :
        for i in range(1,len(l_mode)): 
            new_bit = str(int(new_bit)^int(key[(len(key)-l_mode[i])]))
        key.append(new_bit)

       # print(key)
    #print("key generated de 64 bits:")
    #print(key)
    str_key=''.join(key)
    #print(str_key)
    #######transfer str to binary 
    
    sum, base = 0, 1
    for i in range(len(str_key)):
        sum += int(str_key[-i])*base
        base *= 2
    return sum 

#def bin2list(binary):
 #   str=str(bin(binary)).replace('0b','')
  #  return [str[i] for i in range(len(str))]



def key_generation(nb_key):
    k = [None]*nb_key
    for j in range(nb_key):
        k[j] = lfsr_64bits(lfsr_init_str,lfsr_mode[j])
    return k


        


keys=key_generation(3)
print(keys)

