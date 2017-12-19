from prime import *
from md5 import md5
from time import time
from util import *
from pathlib import Path
import os
import re

P = Q = A1 = A2 = X = Y = W = 0
HOME = str(Path.home())
DIR  = ".cramershoup"
PUBKEY  = "id_cramer_pub"
SECKEY  = "id_cramer"

def H(b1, b2, c):
    return md5("".join([hex(i).replace("0x", "") for i in [b1, b2, c]]))

def GetTwoPrime(bits):
    q = GetPrimeFromExe(bits)
    p = 2*q + 1
    while isProbablePrimeFromExe(p, 20) != True:
        q = GetPrimeFromExe(bits)
        p = 2*q + 1
    return q, p

def GetTwoGenerator(p, q):
    rg = []
    rs = []

    start = time()
    while len(rs) < 2:
        a = rand(2, p-1)
        if pow(a, 2, p) != 1 and pow(a, q, p) != 1 and (a not in rg):
            rs.append(a)
        if a not in rg:
            rg.append(a)
        if len(rg) == p-2 or (time() - start)>3:
            break 
    return rs

def keySchedule(n):
    global P, Q, A1, A2, X, Y, W

    P, Q = GetTwoPrime(n)
    rs = GetTwoGenerator(P, Q)
    while len(rs) < 2:
        P, Q = GetTwoPrime(n)
        rs = GetTwoGenerator(P, Q)
    A1, A2 = rs

    x1, x2, y1, y2, w = [rand(0, P-1) for i in range(5)]

    X = pow(A1, x1, P) * pow(A2, x2, P) % P
    Y = pow(A1, y1, P) * pow(A2, y2, P) % P
    W = pow(A1, w, P) % P

    pubkey = (X, Y, W, A1, A2, P)
    seckey = (x1, x2, y1, y2, w)

    strPub = "{{}}".join([hex(i).replace("0x", "") for i in pubkey])
    strSct = "{{}}".join([hex(i).replace("0x", "") for i in seckey])

    os.chdir(HOME)

    if not IsExistDir(DIR):
        os.mkdir(DIR)
    os.chdir(DIR)

    with open(PUBKEY, "w+") as f:
        f.write(base64Encode(strPub))

    with open(SECKEY, "w+") as f:
        f.write(base64Encode(strSct))

    print('\n---BEGIN CRAMER PUBLICKEY---\n' + magenta(re.sub(r'{{}}', '\n', strPub)) + '\n---END   CRAMER PUBLICKEY---')

def encrypt(s):
    os.chdir(HOME)

    if IsExistDir(DIR):
        os.chdir(DIR)
        if not IsExistFile(SECKEY):
            keySchedule(128)
    else:
        keySchedule(128)
        os.chdir(DIR)
    
    with open(PUBKEY, "r") as f:
        pubkey = re.split("{{}}", base64Decode(f.read()))
    

    X, Y, W, A1, A2, P = [int(i, 16) for i in pubkey]
 
    b  = rand(0, P-1)
    B1 = pow(A1, b, P)
    B2 = pow(A2, b, P)

    c = int("".join([padRight(bin(pow(W, b, P) * i).replace("0b", ""), "0", 8) for i in bytes(s, encoding="utf8")]), 2)
    bt = int(H(B1, B2, c), 16)
    print(bt)

    v = (pow(X, b, P) % P * pow(Y, b * bt, P) % P) % P
    
    return base64Encode("{{}}".join([hex(i).replace("0x", "") for i in [B1, B2, c, v, P]]))

def encryptFile(fic):
    s = ""
    with open(fic, "r") as f:
        s = f.read()
    with open(fic, "w+") as f:
        f.write(encrypt(s))

def decrypt(s):
    os.chdir(HOME)
    if IsExistDir(DIR):
        os.chdir(DIR)
        if IsExistFile(SECKEY):
            with open(SECKEY, 'r') as f:
                seckey = re.split("{{}}", base64Decode(f.read()))
                msg   = re.split("{{}}", base64Decode(s))

                B1, B2, c, v, P = [int(i, 16) for i in msg]

                ch =  msg[2]

                x1, y1, x2, y2, w = [int(i, 16) for i in seckey]
                
                bt = int(H(B1, B2, c), 16)
                print(bt)
                V = pow(B1, x1, P) * pow(B2, x2, P) % P * pow((pow(B1, y1, P) * pow(B2, y2, P) % P), bt, P) % P

                if v == V:
                    print("ok")
                    b = byteFromHex(ch)
                    #m = bin(pow(B1, P-1-w, P) * c).replace("0b", 0)
                    return  str(byteFromHex("".join([hex(pow(B1, P-1-w, P) * i).replace("0x", "") for i in b])), encoding="utf8")
        else:
            return ""
    else:
        return ""

def decryptFile(fic):
    s = ""
    with open(fic,"r") as f:
        s = f.read()
    with open(fic, "w+") as f:
        f.write(decrypt(s))
