from   prime   import *
from   util    import *
from   md5     import md5
from   time    import time
from   pathlib import Path
import os
import re

#================================
P = Q = A1 = A2 = X = Y = W = 0
HOME             = str(Path.home())
DIR              = ".cramershoup"
PUBKEY           = "id_cramer_pub"
SECKEY           = "id_cramer"
CANTFOUNDKEYDIR  = "Can't found {0} in {1}".format(DIR, HOME)
CANTFOUNDSECKEY  = "Can't found {0} in {1}".format(SECKEY, DIR)
#================================

# hash
def H(b1, b2, c):
    return md5("".join([hex(i).replace("0x", "") for i in [b1, b2, c]]))

# generate a secure prime
def GetTwoPrime(bits):
    q = GetPrimeFromScript(bits)
    p = 2*q + 1
    while isProbablePrimeFromScript(p, 20) != True:
        q = GetPrimeFromScript(bits)
        p = 2*q + 1
    return q, p

# find two generators
def GetTwoGenerator(p, q):
    g = []
    start = time()
    while len(g) < 2:
        a = rand(2, p-2)
        if pow(a, 2, p) != 1 and pow(a, q, p) != 1 and (a not in g):
            g.append(a)
        if time()-start>3:
            break 
    return g

# generate key in home dir
def keySchedule(n):
    global P, Q, A1, A2, X, Y, W

    P, Q = GetTwoPrime(n)
    g = GetTwoGenerator(P, Q)
    A1, A2 = g

    x1, x2, y1, y2, w = [rand(0, P-1) for i in range(5)]

    X = pow(A1, x1, P) * pow(A2, x2, P) % P
    Y = pow(A1, y1, P) * pow(A2, y2, P) % P
    W = pow(A1, w, P)

    pubkey = (X, Y, W, A1, A2, P)
    seckey = (x1, x2, y1, y2, w)

    Pub = "{{}}".join([hex(i).replace("0x", "") for i in pubkey])
    Sec = "{{}}".join([hex(i).replace("0x", "") for i in seckey])

    os.chdir(HOME)

    if not IsExistDir(DIR):
        os.mkdir(DIR)
    os.chdir(DIR)

    with open(PUBKEY, "w+") as f:
        f.write(base64Encode(Pub))

    with open(SECKEY, "w+") as f:
        f.write(base64Encode(Sec))

    print('\n---BEGIN CRAMER PUBLICKEY---\n' + magenta(re.sub(r'{{}}', '\n', Pub)) + '\n---END   CRAMER PUBLICKEY---')

# chiffrer a message
def encrypt(s):
    os.chdir(HOME)

    if IsExistDir(DIR):
        os.chdir(DIR)
        if not IsExistFile(SECKEY):
            keySchedule(1024)
    else:
        keySchedule(1024)
        os.chdir(DIR)
    
    with open(PUBKEY, "r") as f:
        pubkey = re.split("{{}}", base64Decode(f.read()))
    

    X, Y, W, A1, A2, P = [int(i, 16) for i in pubkey]
 
    b  = rand(0, P-1)
    B1 = pow(A1, b, P)
    B2 = pow(A2, b, P)

    c = int("".join([padRight(hex(m).replace("0x", ""), "0", 2) for m in bytes(s, encoding="utf8")]), 16) * pow(W, b, P)
    bt = int(H(B1, B2, c), 16)

    v  = pow(X, b, P) * pow(Y, b * bt, P) % P
    
    return base64Encode("{{}}".join([hex(i).replace("0x", "") for i in [B1, B2, c, v, P]]))

# dechiffrer a message
def decrypt(s):
    os.chdir(HOME)
    if IsExistDir(DIR):
        os.chdir(DIR)
        if IsExistFile(SECKEY):
            with open(SECKEY, 'r') as f:
                sec = re.split("{{}}", base64Decode(f.read()))
                msg = re.split("{{}}", base64Decode(s))

                B1, B2, c, v, P   = [int(i, 16) for i in msg]
                x1, x2, y1, y2, w = [int(i, 16) for i in sec]

                bt = int(H(B1, B2, c), 16)
                V  = pow(B1, x1 + y1 * bt, P) * pow(B2, x2 + y2 * bt, P) % P 

                if v == V:
                    return bytes([int(i, 16) for i in chunk(hex(c // pow(B1, w, P)).replace("0x", ""), 2)]).decode("utf8", "strict")
        else:
            raise Exception(CANTFOUNDSECKEY)
    else:
        raise Exception(CANTFOUNDKEYDIR)

# chiffrer a file
def encryptFile(fic):
    with open(fic, 'r') as f:
        s = f.read()
        if s == "":
            print("File Vide!")
    with open(fic, 'w+') as f:
        f.write(encrypt(s))

# dechiffrer a file
def decryptFile(fic):
    with open(fic,'r') as f:
        s = f.read()
        if s == "":
            print("File Vide!")
    with open(fic, 'w+') as f:
        f.write(decrypt(s))
