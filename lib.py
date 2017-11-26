#!/usr/bin/python3

"""
lib
"""

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

def fileToBytes(filename):
    fo = open(filename, 'r')
    str = fo.read()
    fo.close()
    return str.encode("utf-8")