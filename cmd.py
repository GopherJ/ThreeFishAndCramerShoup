#!/usr/bin/python3  

import lib
import keyboard

dictMenu = {
    "Chiffrement Symétrique ThreeFish" : [
         {
            "Chiffrement D'un Message" : {
                    "Saisir Votre Message:" : {
                            "Choisir Votre Mode" : ["ECB", "CBC"]
                        }
                }
         },{
            "Chiffrement D'un Fichier" : {   
                    "Saisir Le Nom Du Fichier:" : {
                            "Choisir Votre Mode" : ["ECB", "CBC"]
                        }
                }
         },
     ],
    "Chiffrement De Cramer-Shoup" : [
         {
            "Chiffrement D'un Message" : {
                    "Saisir Votre Message:" : {
                            "Choisir Votre Mode" : ["ECB", "CBC"]
                        }
                }
         },{
            "Chiffrement D'un Fichier" : {   
                    "Saisir Le Nom Du Fichier:" : {
                            "Choisir Votre Mode" : ["ECB", "CBC"]
                        }
                }
         },
     ],
    "Hashage D'un Message" : [
         {
            "Hashage D'un Message" : "Saisir Votre Message:"
         },{
            "Hashage D'un Fichier" : "Saisir Le Nom Du Fichier:"
         }  
     ],  
    "Déciffrement Symétrique ThreeFish" : [
         {
            "Déchiffrement D'un Message" : {
                    "Saisir Votre Message:" : {
                            "Choisir Votre Mode" : ["ECB", "CBC"]
                        }
                }
         },{
            "Déchiffrement D'un Fichier" : {   
                    "Saisir Le Nom Du Fichier:" : {
                            "Choisir Votre Mode" : ["ECB", "CBC"]
                        }
                }
         }
    ],  
    "Déchiffrement De Cramer-Shoup" : [
         {
            "Déchiffrement D'un Message" : "Saisir Votre Message:"  
         },{
            "Déchiffrement D'un Fichier" :    "Saisir Le Nom Du Fichier:"  
         },
    ], 
    "Vérification D'un Hash" :  "Saisir Votre Hashage"  
}

beforeMenu = lib.magenta("""\nThree Fish && Cramer Shoup - Cheng JIANG && Shunjie TU
\n""")
exitInstruction = lib.magenta("\nPress ESC to stop\nPress Enter to choose")

# initialisation
menu = [list(dictMenu)]
n = [1,2]
idx = 0

def prMenu():
    s = beforeMenu
    global idx
    if len(n) == 0:
        m = menu[0]
        for i in m:
            if m.index(i) == idx:
                s += lib.green('=> ') + lib.cyan(i) + '\n'
            else:
                s += '   ' + lib.cyan(i) + '\n'
        s += exitInstruction
        print('\x1b[2J' + s)
        idx = (idx + 1) % len(m)
    else:
        j = 0
        s = beforeMenu
        for i in n:
            t = menu[j] 
            k = t[i]
            m = dictMenu[k]
            if type(m) == list:
                if len(menu) <= len(n):
                    menu.append(lib.dechunk([list(item) for item in m]))
                if i == n[len(n) - 1]:
                    l = menu[len(menu) - 1]
                    for i in l:
                        if l.index(i) == idx:
                            s += lib.green('=> ') + lib.cyan(i) + '\n'
                        else:
                            s += '   ' + lib.cyan(i) + '\n'
            elif type(m) == dict:
                if len(menu) <= len(n):
                    menu.append(list(m))
                if i == n[len(n) - 1]:
                    l = menu[len(menu) - 1]
                    for i in l:
                        if l.index(i) == idx:
                            s += lib.green('=> ') + lib.cyan(i) + '\n'
                        else:
                            s += '   ' + lib.cyan(i) + '\n'
            elif type(m) == str:
                if len(menu) <= len(n):
                    menu.append(m)
                if i == n[len(n) - 1]:
                    l = menu[len(menu) - 1]
                    for i in l:
                        if l.index(i) == idx:
                            s += lib.green('=> ') + lib.cyan(i) + '\n'
                        else:
                            s += '   ' + lib.cyan(i) + '\n'
            dictMenu = m
            j = j + 1
            
            if i == n[len(n) - 1]:
                s += exitInstruction
                print('\x1b[2J' + s)
                idx = (idx + 1) % len(m)
    
def onEnter():
    global idx
    n.append[idx]
    idx = 0
    prMenu()


prMenu()
print(n, idx, menu)

"""
    s += exitInstruction
    print('\x1b[2J' + s)
    idx[0] = (idx[0] + 1) % len(menu[0])
        







def prStartMenu(idx):
    str = lib.magenta(beforeMenu)
    for key in menu[0]:
        if menu[0].index(key) == idx[0]:
            str += lib.green('=> ') + lib.cyan(key) + '\n'
        else:
            str += '   ' + lib.cyan(key) + '\n'
   str += exitInstruction
    print('\x1b[2J' + str)
    idx[0] = (idx[0] + 1) % len(menu[0])

def prMiddleMenu(n, idx):
    key = menuStart[n[0]]
    value = dictMenu[key]
    s = lib.magenta(beforeMenu)

    if type(value) == dict:
        for item in list(value):
            if list(value).index(item) == idx[0]:
                s += lib.cyan('=> ' + item) + '\n'
            else:
                s += lib.cyan('   ' + item) + '\n'
    elif type(value) == str:
        s += lib.cyan('=> ' + str) + '\n'
    elif type(value) == list:
        value = lib.dechunk([list(item) for item in value])
        for item in value:
            if value.index(item) == idx[0]:
                s += lib.cyan('=> ' + item) + '\n'
            else:
                s += lib.cyan('   ' + item) + '\n'
    
    s += exitInstruction
    print('\x1b[2J' + s)
    idx[0] = (idx[0] + 1) % len()


def pr(n):
    # start menu
    if len(n) == 0:
        prStartMenu(idx)
    elif len(n) == 1:
        prtMiddleMenu(n, idx)
        


# screen at the beginning
pr(n)

keyboard.add_hotkey(28, afterEnter, args = [n, idx])
keyboard.add_hotkey(80, pr, args=[n])
keyboard.wait('esc')
















list_menu = list(dict_menu)
#transfer the output of the keys of dict_menu to a list 

for i in range(len(list_menu)):
    print("->%i<- %s" %(i,list_menu[i]))
mode = int(input("please input your method: "))

sub_menu = dict_menu[str(list_menu[mode])]


for i in range( (len(dict_menu[str(list_menu[mode])])) ):
    print("->%i<- %s" %(i,sub_menu[i]))



option = int(print("please input your option: "))
"""




