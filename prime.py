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

"""
// GenPrime.go
// https://github.com/golang/go/blob/master/src/crypto/rand/util.go
package main

import (
  "crypto/rand"
  "fmt"
  "math/big"
  "os"
  "strconv"
)

func main() {
    var p *big.Int
    var bits int
    var err error

    if len(os.Args) == 1 {
         bits = 1024
    } else {
        bits, err = strconv.Atoi(os.Args[1])
        if err != nil {
             panic(err)
        }
    }

    p, err = rand.Prime(rand.Reader, bits)

    if err != nil {
        panic(err)
    }

    fmt.Printf("%x", p)

}
"""

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

"""
// isProbablePrime.go
// https://github.com/golang/go/blob/master/src/math/big/prime.go
package main

import (
    "fmt"
    "math/big"
    "os"
    "strconv"
)

func main(){
    s, b, n := os.Args[1], os.Args[2], os.Args[3]
    p := new(big.Int)
    i, err := strconv.Atoi(b)
    p.SetString(s, i)
    i, err = strconv.Atoi(n)
    if err != nil {
        panic("Error")
    }
    fmt.Printf("%t", p.ProbablyPrime(i))
}
"""
