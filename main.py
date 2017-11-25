#!/usr/bin/python3  


dict_menu = {'Chiffrement symétrique ThreeFish (3 ><(((> )' : 
            { 1 : 'option1' , 2 : 'option2', 3 : 'option3' } ,
        'Chiffrement de Cramer-Shoup' : 
            { 1 : 'option1' , 2 : 'option2', 3 : 'option3' } ,
        'Hashage d’un message' : 
            { 0 : 'option1' , 1 : 'option2', 2 : 'option3' } ,  
        'Déciffrement symétrique ThreeFish (3 ><(((> )' : 
            { 1 : 'option1' , 2 : 'option2', 3 : 'option3' } ,  
        'déchiffrement de Cramer-Shoup' : 
            { 1 : 'option1' , 2 : 'option2', 3 : 'option3' } , 
        'Vérification d’un Hash' : 
            { 1 : 'option1' , 2 : 'option2', 3 : 'option3' }   }





list_menu = list(dict_menu.keys())
#transfer the output of the keys of dict_menu to a list 

for i in range(len(list_menu)):
    print('->%i<- %s' %(i,list_menu[i]))
mode = int(input("please input your method: "))

sub_menu = dict_menu[str(list_menu[mode])]


for i in range( (len(dict_menu[str(list_menu[mode])])) ):
    print('->%i<- %s' %(i,sub_menu[i]))

option = int(print("please input your option: "))

  




