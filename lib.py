#!/usr/bin/python3

'''
lib
'''

def rotl(x,n):
    return (x << n) or (x >> (64 - n))

def rotr(x, n):
    return (x >> n) or (x << (64 - n))
