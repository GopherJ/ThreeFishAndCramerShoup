#!/usr/bin/python3 

#chr(ascii) ->char   ascii(0~255)
#unichr(unicode)->char  
#ord(char) ->ascii



def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
   # return ' '.join([bin(ord(c)) for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
str="tushunjie"
print(encode(str))
#print(ord('c'))   char->ascii 
#print(bin(ord('c'))) char->ascii->0b 

#'sep'.join(seq) 
#str.replace(old, new[, max])s 