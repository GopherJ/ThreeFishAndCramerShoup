#!/usr/bin/python3  
# -*- coding: UTF-8 -*-

from   util   import *
from   md5    import *
from   cramer import encrypt
from   cramer import encryptFile
from   cramer import decrypt
from   cramer import decryptFile
from   signal import signal
from   signal import SIGINT
from   fish   import cipher_threefish_msg
from   fish   import cipher_threefish_file
from   fish   import decipher_threefish_msg
from   fish   import decipher_threefish_file
import keyboard
import os
import sys

# definition of constants
dictMenu = {
    "Chiffrement Symétrique ThreeFish" : [
         {
           "Chiffrement D'un Message" : [
                            { 
                                "ECB" : ["Saisir Votre Message:"]
                            },{
                                "CBC" : ["Saisir Votre Message:"]
                            }
                    ]
         },{
           "Chiffrement D'un Fichier" : [   
                            {
                                "ECB" : ["Saisir Le Nom Du Fichier:"]
                            },{
                                "CBC" : ["Saisir Le Nom Du Fichier:"]
                            }
                    ]
         }
     ],
    "Chiffrement De Cramer-Shoup" : [
         {
           "Chiffrement D'un Message" : ["Saisir Votre Message:"] 
         },{
           "Chiffrement D'un Fichier" : ["Saisir Le Nom Du Fichier:"]
         }
     ],
    "Hashage" : [
         {
            "Hashage D'un Message" : ["Saisir Votre Message:"]
         },{
            "Hashage D'un Fichier" : ["Saisir Le Nom Du Fichier:"]
         }  
     ],  
    "Déciffrement Symétrique ThreeFish" : [
         {
            "Déchiffrement D'un Message" : [
                            { 
                                   "ECB" : ["Saisir Votre Message:"]
                            },{
                                   "CBC" : ["Saisir Votre Message:"]
                            }
                    ]
         },{
            "Déchiffrement D'un Fichier" : [   
                            { 
                                   "ECB" : ["Saisir Votre Message:"] 
                            },{
                                   "CBC" : ["Saisir Votre Message:"]
                            }
                    ]
         }
    ],
    "Déchiffrement De Cramer-Shoup" : [
         {
            "Déchiffrement D'un Message" : ["Saisir Votre Message:"]  
         },{
            "Déchiffrement D'un Fichier" : ["Saisir Le Nom Du Fichier:"]
         }
    ], 
    "Vérification D'un Hash" : [
         "Saisir Votre Message:",
         "Saisir Votre Hashage:"
    ]
}

S = magenta("""
\x1b[2J
Three Fish && Cramer Shoup - Cheng JIANG && Shunjie TU\n
""")

E = magenta("""
Press 'up' and 'down' to choose\nPress 'left' to back and 'right' to next 
Press ESC to exit
""")


M = list(dictMenu)     # F menu
m = []                 # store menus except the F menu, 
n = []                 # store idx which has been chosen by user
idx = 0                # store idx for now, which sign that '=> ' should be at which line
menu = [dictMenu]      # store complete menu
rs = []                # rs answers of user

L = lambda arr: (arr[len(arr) - 1])
F = lambda arr: (arr[0])

def cls(arr):
    while len(arr) > 0:
        arr.pop()

def ask(arr):
    n = len(arr)
    while len(arr) > 0:
        if len(arr) == n:
            rs.append(input('\n-> ' + arr.pop() + '  '))
        else:
            rs.append(input('-> '   + arr.pop() + '  '))
    
# print menu which is m[len(m) - 1] or M
def show():
    s = S
    if len(m) == 0:
        for i in M:
            if M.index(i) == idx:
                s += green('=> ') + cyan(i) + '\n'
            else:
                s += green('   ') + cyan(i) + '\n'
    else:
        for i in m[len(m) - 1]:
            if m[len(m) - 1].index(i) == idx:
                s += green('=> ') + cyan(i) + '\n'
            else:
                s += green('   ') + cyan(i) + '\n'
    s += E
    print(s)

def init():
    global menu
    if F(n) == 5:
            ask(L(menu)[M[n[0]]])
            if verify(F(rs), L(rs)):
                print(green("\n\tOk!"))
            else:
                print(red("\n\tError!"))
            os._exit(0)
    elif len(n) == 1 and len(m) == 0:
        menu.append(L(menu)[M[n[0]]])
        m.append(dechunk([list(i) for i in L(menu)]))
    elif len(n) > len(m):
        t = L(m)[L(n)]
        for i in L(menu):
            if F(list(i)) == t:
                menu.append(i[t])
                m.append(dechunk([list(j) for j in L(menu)]))
        
        if F(n) in [1,2,4] and len(n) == 2:
            rs.append(n[1])
            ask([L(L(menu))])
            if F(n) == 2:
                if F(rs) == 0:
                    print(green(md5(L(rs))))
                elif F(rs) == 1:
                    try:
                        md5fic(L(rs))
                        print(green("Ok!"))
                    except FileNotFoundError:
                        print(magenta("No Such File!"))
            elif F(n) == 1:
                if F(rs) == 0:
                    print(green(encrypt(L(rs))))
                elif F(rs) == 1:
                    try:
                        print(L(rs))
                        encryptFile(L(rs))
                        print(green("Ok!"))
                    except FileNotFoundError:
                        print(magenta("No Such File!"))
            elif F(n) == 4:
                if F(rs) == 0:
                    print(green(decrypt(L(rs))))
                elif F(rs) == 1:
                    try:
                        decryptFile(L(rs))
                        print(green("Ok!"))
                    except FileNotFoundError:
                        print(magenta("No Such File!"))
            os._exit(0)
        elif F(n) in [0,3] and len(n) == 3:
            rs.append(n[1])
            rs.append(n[2])
            ask([L(L(menu))])

            if F(n) == 0:
                MSG_FILE, ECB_CBC, s = rs
                if  MSG_FILE == 0:
                    if ECB_CBC == 0:
                        print(green(cipher_threefish_msg(s, cts.MODE_ECB)))
                    elif ECB_CBC == 1:
                        print(green(cipher_threefish_msg(s, cts.MODE_CBC)))
                elif MSG_FILE == 1:
                    if ECB_CBC == 0:
                        try:
                            cipher_threefish_file(s, cts.MODE_ECB)
                            print(green("Ok!"))
                        except FileNotFoundError:
                            print(magenta("No Such File!"))
                    elif ECB_CBC == 1:
                        try:
                            cipher_threefish_file(s, cts.MODE_CBC)
                            print(green("Ok!"))
                        except FileNotFoundError:
                            print(magenta("No Such File!"))
            elif F(n) == 3:
                MSG_FILE, ECB_CBC, s = rs
                if  MSG_FILE == 0:
                    if ECB_CBC == 0:
                        print(green(decipher_threefish_msg(s, cts.MODE_ECB)))
                    elif ECB_CBC == 1:
                        print(green(decipher_threefish_msg(s, cts.MODE_CBC)))
                elif MSG_FILE == 1:
                    if ECB_CBC == 0:
                        try:
                            decipher_threefish_file(s, cts.MODE_ECB)
                            print(green("Ok!"))
                        except FileNotFoundError:
                            print(magenta("No Such File!"))
                    elif ECB_CBC == 1:
                        try:
                            decipher_threefish_file(s, cts.MODE_CBC)
                            print(green("Ok!"))
                        except FileNotFoundError:
                            print(magenta("No Such File!"))
            os._exit(0)

# listen left
def onLeft():
    global idx
    try:
        m.pop()
        n.pop()
        menu.pop()
        cls(rs)
        idx = 0
        init()
        show()
    except IndexError:
        show()

# listen right
def onRight():
    global idx
    n.append(idx)
    idx = 0
    init()
    show()

# listen up
def onUp():
    global idx
    if idx - 1 < 0:
        idx = (len(M) - 1) if len(n) == 0 else (len(m[len(m) - 1]) - 1)
    else:
        idx = idx - 1
    show()

# listen down
def onDown():
    global idx
    idx =  ((idx + 1) % len(M)) if len(n) == 0 else ((idx + 1) % len(m[len(m) - 1]))
    show()

# print start menu
show()

keyboard.add_hotkey(72, onUp)    # up clicked
keyboard.add_hotkey(80, onDown)  # down clicked
keyboard.add_hotkey(75, onLeft)  # left clicked
keyboard.add_hotkey(77, onRight) # right clicked


def handler(signal, frame):
    print(green("\n\tBye!"))
    sys.exit(0)
signal(SIGINT, handler)

# if 'esc' clicked, exit programme
keyboard.wait('esc') 
