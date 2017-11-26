#!/usr/bin/python3

def change(list):
    list[0] = 2

def per(list, pi):
    t = list[0:len(list)]
    for i in range(len(list)):
        list[i] = t[pi[i]]




pi = (0,2,3,1)
l = [2,6,7,8]
per(l,pi)

print(l)
