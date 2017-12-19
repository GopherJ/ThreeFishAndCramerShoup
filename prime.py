from random import randint
from datetime import datetime

from cts import sps

from subprocess import Popen
from subprocess import PIPE


def rand(min, max):
    return randint(min, max)

def randNbit(n):
    arr = ["1"]
    for i in range(1, n):
        arr.append(str(rand(0,1)))
    return int("".join(arr), 2)

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    rt = math.floor(math.sqrt(n))
    for i in range(2, rt):
        if n & i == 0:
            return False
    return True

def modExp(x, n, p):
    if n == 0:
        return 1

    t = pow((x*x)%p, int(n/2), p)
    if n&1 != 0:
        t = (t*x)%p

    return t

def isProbablePrime(n, p):
    if n == 1:
        return False
    if n == 2:
        return True
    if n & 1 == 0:
        return False

    for i in sps:
        if n % p == 0:
            return False

    s = 0
    d = n - 1
    while d & 1 == 0:
        s = s + 1
        d = int(d/2)

    if pow(2, n-1, n) != 1:
        return False
            
    def rabinTest(a):
        ct = 0
        for i in range(s):
            if pow(a, d, n) != 1 and modExp(a, 2**i*d, n) != n-1:
                ct = ct + 1
                continue
            else:
                break
        if ct == s:
            return False
        else:
            return True

    for i in range(p):
        a = rand(1, n-1)
        if rabinTest(a) != True:
            return False
    return True

def GetPrime(bits, p):
    n = randNbit(bits)
    while isProbablePrime(n, p) != True:
        n = randNbit(bits)
    return n

def GetPrimeFromExe(n):
    b = Popen(["cmd", "/C", "GenPrime.exe {0}".format(n)], stdout=PIPE).communicate()[0]
    arr = []
    for i in b:
        arr.append(i)
    return int("".join([chr(i) for i in arr]), 16)

def isProbablePrimeFromExe(n, p):
    s = bin(n).replace("0b", "")
    t = Popen(["cmd", "/C", "isProbablePrime.exe {0} {1} {2}".format(s, 2, p)], stdout=PIPE).communicate()[0]
    rs = "".join([chr(i) for i in t])
    if rs == "true":
        return True
    elif rs == "false":
        return False
