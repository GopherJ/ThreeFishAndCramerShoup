#!/usr/bin/python3  

import lib
import keyboard
import os

# definition of constant
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
    "Hashage D'un Message" : [
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

startInstruction = lib.magenta("""\x1b[2J\nThree Fish && Cramer Shoup - Cheng JIANG && Shunjie TU
\n""")
endInstruction = lib.magenta("\nPress ESC to stop\nPress 'left' and 'right' to choose")


_m_ = list(dictMenu)   # 一级目录
m = []                 # 存储各级menu，从二级开始
n = []                 # 存储已经选定的index
idx = 0                # 当前 '=> ' 所在的条目
menu = [dictMenu]      # 按下enter后重新计算
record = []            # 记录用户输入

def last(arr):
    return arr[len(arr) - 1]

# 判断是字典还是列表
def isPlainList(unkown):
    if type(unkown) == list:
        if type(unkown[0]) == str:
            return True
        if type(unkown[0]) == dict:
            return False
    
# 打印菜单
def pr():
    s = startInstruction
    if len(m) == 0:
        for i in _m_:
            if _m_.index(i) == idx:
                s += lib.green('=> ') + lib.cyan(i) + '\n'
            else:
                s += lib.green('   ') + lib.cyan(i) + '\n'
    else:
        for i in m[len(m) - 1]:
            if m[len(m) - 1].index(i) == idx:
                s += lib.green('=> ') + lib.cyan(i) + '\n'
            else:
                s += lib.green('   ') + lib.cyan(i) + '\n'
    s += endInstruction
    print(s)


def init():
    global menu
    if n[0] == 5:
            qa = last(menu)[_m_[n[0]]]
            record.append(input('\n' + qa[0]))
            if len(record) == 1:
                record.append(input('\r' + qa[1]))
            print(record)
            os._exit(0)
            # rs = cipher.hash(record)
            # if rs == True:
            #     print(lib.green(str(rs))
            # else:
            #     print(lib.red(str(rs)))
            # exit(0)
    elif len(n) == 1 and len(m) == 0:
        menu.append(last(menu)[_m_[n[0]]])
        m.append(lib.dechunk([list(i) for i in last(menu)]))
    elif len(n) > len(m):
        t = m[len(m) - 1][n[len(n) - 1]]
        for i in last(menu):
            if list(i) == t:
                menu.append(i[t])
                m.append(lib.dechunk([list(j) for j in last(menu)]))
        
        if n[0] in [1,2] and len(n) == 2:
            record.append(n[1])
            # n[1] == 0 => msg
            # n[1] == 1 => fic
            if len(record) == 1:
                record.append(input(last(last(menu))))
            # print(cipher.cramershoup(record))
        elif n[0] in [0,3] and len(n) == 3:
            record.append(n[1])
            # n[1] == 0 => msg
            # n[1] == 1 => fic
            # n[2] == 0 => ecb
            # n[2] == 1 => cbc
            record.append(n[2])
            if len(record) == 1:
                record.append(input(last(last(menu))))


# 监听 left
def onLeft():
    global idx
    try:
        m.pop()
        n.pop()
        menu.pop()
        idx = 0
        init()
        pr()
    except IndexError:
        pr()

# 监听 right
def onRight():
    global idx
    n.append(idx)
    idx = 0
    init()

# 监听 up
def onUp():
    global idx
    if idx - 1 < 0:
        idx = (len(_m_) - 1) if len(n) == 0 else (len(m[len(m) - 1]) - 1)
    else:
        idx = idx - 1
    pr()

def onDown():
    global idx
    idx =  ((idx + 1) % len(_m_)) if len(n) == 0 else ((idx + 1) % len(m[len(m) - 1]))
    pr()

pr()
keyboard.add_hotkey(72, onUp, args=[])
keyboard.add_hotkey(80, onDown, args=[])
keyboard.add_hotkey(75, onLeft, args=[])
keyboard.add_hotkey(77, onRight, args=[])
keyboard.wait('esc')





