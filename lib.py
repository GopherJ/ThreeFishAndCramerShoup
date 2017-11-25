#!/usr/bin/python3

'''
lib
'''

def rotl(x,n):
    return (x << n) or (x >> (64 - n))

def rotr(x, n):
    return (x >> n) or (x << (64 - n))

def per(list, pi):
    t = list[0:len(list)]
    for i in range(len(list)):
        list[i] = t[pi[i]]

print(rotl(10,2))