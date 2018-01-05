from   random     import randint
from   subprocess import Popen
from   subprocess import PIPE
from   platform   import system
import os

DIR = os.path.dirname(os.path.realpath(__file__))

def rand(min, max):
    return randint(min, max)

def GetPrimeFromScript(n):
    s = "{0}\script\GenPrime".format(DIR) 

    if system() == "Windows":
        s += ".exe"
        s = os.path.abspath(s)
        arr = ["cmd", "/C", "{0} {1}".format(s, n)]
    elif system() == "Darwin":
        s += "_darwin"
        s = os.path.abspath(s)
        arr = ["{0} {1}".format(s, n)]
    elif system() == "Linux":
        s += "_linux"
        s = os.path.abspath(s)
        arr = ["{0} {1}".format(s, n)]

    b = Popen(arr, stdout=PIPE).communicate()[0]
    arr = []
    for i in b:
        arr.append(i)
    return int("".join([chr(i) for i in arr]), 16)

def isProbablePrimeFromScript(n, p):
    s = "{0}\script\isProbablePrime".format(DIR)
    b = bin(n).replace("0b", "")

    if system() == "Windows":
        s += ".exe"
        s = os.path.abspath(s)
        arr = ["cmd", "/C", "{0} {1} {2} {3}".format(s, b, 2, p)]
    elif system() == "Darwin":
        s += "_darwin"
        s = os.path.abspath(s)
        arr = ["{0} {1} {2} {3}".format(s, b, 2, p)]
    elif system() == "Linux":
        s += "_linux"
        s = os.path.abspath(s)
        arr = ["{0} {1} {2} {3}".format(s, b, 2, p)]

    t = Popen(arr, stdout=PIPE).communicate()[0]
    T = "".join([chr(i) for i in t])
    if T == "true":
        return True
    elif T == "false": 
        return False
