# package for output font colored in cmd
from   time     import time
from   colorama import init
from   colorama import Fore, Back, Style
init(autoreset=True) 
import random
import math
import base64
import os
import cts

def rotl(x,n):
    return (x << n) or (x >> (64 - n))

def rotr(x, n):
    return (x >> n) or (x << (64 - n))

def per(list, pi):
    t = list[0:len(list)]
    for i in range(len(list)):
        list[i] = t[pi[i]]

def utf8ToBytes(str):
    return str.encode("utf-8")

def bytesToUtf8(str):
    return str.decode("utf-8", "strict")

def base64Encode(str):
    b = base64.b64encode(bytes(str, encoding="utf8"))
    return "".join([chr(i) for i in b])

def base64Decode(str):
    b = base64.b64decode(bytes(str, encoding="utf8"))
    return "".join([chr(i) for i in b])
    
def padLeft(s, char, n):
    return ('{:' + char + '<' + str(n) + '}').format(s)

def padCenter(s, char, n):
    return ('{:' + char + '^' + str(n) + '}').format(s)

def padRight(s, char, n):
    return ('{:' + char + '>' + str(n) + '}').format(s)
     
def chunk(arr, n):
    newArr = []
    idx = 0
    length = len(arr)
    while idx < length:
        newArr.append(arr[idx:idx+n])
        idx += n
    return newArr

def dechunk(arr):
    return [i for sublist in arr for i in sublist]

def clearZero(arr):
    l = len(arr) - 1
    while arr[l] == 0:
        arr.pop()
        l -= 1
    return arr

def readFile(filename, blockSize):
    # read file and encode with utf-8
    fo = open(filename, 'r')
    str = fo.read()
    fo.close()
    str_utf8 = str.encode("utf-8")

    # initialisation 
    numBlockByte = int(blockSize / 8)

    # transfer bytes to arr of byte
    arr = []
    for i in range(len(str_utf8)):
        arr.append(str_utf8[i])
    
    # completion according to blockSize
    length = len(arr)
    if length % numBlockByte != 0:
        if length < numBlockByte:
            decalage = numBlockByte - length
            for k in range(decalage):
                arr.append(0)
        if length > numBlockByte:
            decalage = int(numBlockByte - (length % numBlockByte))
            for j in range(decalage):
                arr.append(0)

    # divise arr in subArr of 8 items
    newArr = chunk(arr, 8)

    # join subArr
    for j in range(len(newArr)):
        newArr[j] = ''.join([padRight(bin(c).replace('0b', ''), '0', 8) for c in newArr[j]])
    
    # return arr of decimal
    numBlock = int(blockSize / 64)
    return chunk([int('0b' + el, 2) for el in newArr], numBlock)

def writeFile(filename, arr):
    fo = open(filename, 'w')
    newArr = dechunk([chunk(padRight(bin(el).replace('0b', ''), '0', 64), 8) for el in dechunk(arr)])

    # padRight char '0' to get 8 bits
    for i in range(len(newArr)):
        newArr[i] = padRight(newArr[i], '0', 8)

    # print(type(bytesToUtf8(bytes([int('0b' + el, 2) for el in newArr]))))

    fo.write(bytesToUtf8(bytes(clearZero([int('0b' + el, 2) for el in newArr]))))
    return fo.close()

# writeFile('test.py', readFile('README.md',256))

def readMsg(str, blockSize):
    str_utf8 = str.encode("utf-8")

    # initialisation 
    numBlockByte = int(blockSize / 8)

    # transfer bytes to arr of byte
    arr = []
    for i in range(len(str_utf8)):
        arr.append(str_utf8[i])
    
    # completion according to blockSize
    length = len(arr)
    if length % numBlockByte != 0:
        if length < numBlockByte:
            decalage = numBlockByte - length
            for k in range(decalage):
                arr.append(0)
        if length > numBlockByte:
            decalage = int(numBlockByte - (length % numBlockByte))
            for j in range(decalage):
                arr.append(0)

    # divise arr in subArr of 8 items
    newArr = chunk(arr, 8)

    # join subArr
    for j in range(len(newArr)):
        newArr[j] = ''.join([padRight(bin(c).replace('0b', ''), '0', 8) for c in newArr[j]])
    
    # return arr of decimal
    numBlock = int(blockSize / 64)
    return chunk([int('0b' + el, 2) for el in newArr], numBlock)

def writeMsg(arr):
    newArr = dechunk([chunk(padRight(bin(el).replace('0b', ''), '0', 64), 8) for el in dechunk(arr)])

    # padRight char '0' to get 8 bits
    for i in range(len(newArr)):
        newArr[i] = padRight(newArr[i], '0', 8)

    # print(type(bytesToUtf8(bytes([int('0b' + el, 2) for el in newArr]))))
    return bytesToUtf8(bytes(clearZero([int('0b' + el, 2) for el in newArr])))

def magenta(str):
    return Fore.MAGENTA + str

def green(str):
    return Fore.GREEN + str

def cyan(str):
    return Fore.CYAN + str

def red(str):
    return Fore.RED + str

def IsExistDir(path):
    return os.path.isdir(path)

def IsExistFile(path):
    return os.path.exists(path)

def byteFromHex(str):
    return bytearray.fromhex(str)

