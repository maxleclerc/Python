# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:59:14 2019

@author: Maxence
"""

import sys
from random import randrange
from time import sleep

LONGUEUR_LIGNE = 76 # Nombre de caractères par ligne
LIGNES_TRANS = 25 # Nombre de lignes

def lignesTrans():
    ligne = ''
    for i in range(0, LONGUEUR_LIGNE):
        ligne += str(randrange(10)) + ' ' # Ajoute un nombre aléatoire de 0 à 9 (avec un espace)
    return ligne

def transition():
    # Appelle LIGNES_TRANS fois une ligne aléatoire avec 0.03 sec d'écart
    print('\n' * 5)
    for i in range(0, LIGNES_TRANS):
        print(lignesTrans())
        print()
        sleep(0.03)
    print('\n' * 5)

def loco():
    while True:
        f1 = open('.\loc0.txt', 'r')
        f2 = open('.\loc1.txt', 'r')
        f3 = open('.\loc2.txt', 'r')
        print('\n' * 3)
        print(f1.read())
        sleep(0.25)
        print('\n' * 3)
        print(f2.read())
        sleep(0.25)
        print('\n' * 3)
        print(f3.read())
        sleep(0.25)
        
        temp = input()
        if temp != '':
            break

def dieu():
    f = open('.\dieu.txt', 'r')
    print(f.read())
    input()

def copernic():
    f = open('.\copernic.txt', 'r')
    print(f.read())
    input()

def dieuTriste():
    f = open('.\dieutriste.txt', 'r')
    print(f.read())
    input()

def lune():
    f = open('.\lune.txt', 'r')
    print(f.read())
    input()

def kepler():
    f = open('.\kepler.txt', 'r')
    print(f.read())
    input()

def pomme():
    f = open('.\pomme.txt', 'r')
    print(f.read())
    input()

def science():
    f = open('.\science.txt', 'r')
    print(f.read())
    input()

def louis():
    f = open('.\louis.txt', 'r')
    print(f.read())
    input()

def engrenage():
    f = open('.\engrenage.txt', 'r')
    print(f.read())
    input()

def bateau():
    f = open('.\\bateau.txt', 'r') # \\ parce que \b ça marche pas
    print(f.read())
    input()

def ble():
    f = open('.\\ble.txt', 'r') # \\ parce que \b ça marche pas
    print(f.read())
    input()

def voiture():
    print('''
                                                                               .                                                                                                                .       
                                                                             .....                                                                                                            .....     
             ........                                                       ......                                            .......                                                        ......     
           .............                                                ..........                                          ............                                                 ..........     
        .................                                             ............                                        ................                                             ............     
       ...................                                         .............                                        ............ .....                                           .............      
       ...................                                       ............                                           ..................                                        .............         
        ................      ......                          ..............                                            .................                                       .............           
        .............   ..++==-+##**++==--::..               ............       .. .........:::::-----::::.........      ..............                                       ............              
           ........     .=@@@@@@@@@@@@@@@@@@%.               .............::-==++*##%%%@@@@@@@@@@@@@@@@@@@@@@@%%#*++=-:.............                                          .........                 
                        .-@@@@@@@@@@@@@@@@@@@-             ...:-==+**#%%@@@@@@@%#**+@@=--:::........::::--==+**#%@@@@@@@%#+=:...                                              .......                   
                         ....::--==+#@@@*:.:::::--==++*##%%@@@@@@@@@@@@@@@@@@@+.   .@%.                          ..:-=*#%@@@@@%*+-..                                                                    
                       .-+======+*#%%@@@@@@@@@@@@@@@@@@@@@@@@@%#*++**#@@@@@@@@@@+:.-@#.                               ....:=+#@@@@@%#+-..                                                               
                      .=*..-+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=..*%@@@@@@@@@@@@@@@@**@+..........                            ...:=*%@@@@@%*=:..                                                          
                      .#:+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-.=@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%####****++=====----::::...........:=#@@@@@@%*+++******+=-:...                                          
                     .#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:.-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%####@@@@@@@@@@@@@@@@@@@@@%#*=-...                                    
                     =@@@@@@@@@@@@@@@@@%#*+++++*#%@@@@@@@@@@@@@%...#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*+++++*#%@@@@@@@@@@@@%*+-...                               
                   .:@@@@@@@@@@@@@@%+==+##%@@@%%#+==+%@@@@@@@@@@%...*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*==+#%%@@@@%#*==+#@@@@@@@#+=:-=++=:...                          
                   .%@@@@@@@@@@@@#-=#@@%*+=====+*%@@%=-*@@@@@@@@@#...-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%--#@@@#+=====+*%@@%+:*@@@@@@@@@@#*=-=**=..                        
                   .@@@@@@@@@@@@=-%@@*-=**+*@*+**=-*@@%--@@@@@@@@@*.  :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:#@@#--***+@#+**=-+@@@=-%@@@@@@@@@@@@@#+*%#-..                     
                   .-@@@@@@@@@@=-@@%:=%=.  -@=. .-%=:%@@=-@@@@@@@@@+.  .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:@@@--%+...:@+...-#+.#@@=:@@@@@@@@@@@@@@@@@@@@+.                    
                   ..=@@@@@@@@%.%@@--@*+++***##++*#@=:@@@.*@@@@@@@@@=  ..=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.#@@=:@#+++****#+=*#@+.@@@:*@@@@@@@@@@@@@@@@@@@@#.                   
                     *@@@@@@@@*.@@@.*#..-@#...*%:..+*.@@@:+@@@@@@@@@@-. .....:---==++**###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.@@@:=%..:%%. .+%-..+%.%@@-=@@@@@@@@@@@@@@@@@@@@+.                   
                     +@@@@@@@@%.#@@=:@:..*@#+#@*..:%--@@%.#@@@@@@@@@@@****++++=====---:::::....::--==++**###%%@@@@@@@@@@@@@@@@@@@@@.*@@+.%-..+@%+*@*...%=:@@@.*@@@@@@@@@@@@@@@@@@@*.                    
                     .:=*%@@@@@+:@@@=-#*#*:...:#*+#--@@@-=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%#####******###%%%@@@@@@@@@@*.%@@=:#**#:....**+#--%@@--@@@@@@@@@@@@@@@@@@@@=.                    
                     ......:----.:#@@#=-+*+++++*+-=#@@#:.=++++++++++++++****************###############%%%%%%%%%%%%%%%@@@@@@@@@@@@@@*:*@@%=-=*+++++*+--#@@%-=@@@@@@@@@@@@@@@@@@@@@@+.                   
                   ......         .:*%@@%#*++++*%@@@*-..              .......                                     .....................:+%@@%#*++++*%@@@*-..:::::::::--------------:. ........          
                .........            .:=+*#%%%#*+=:.               ............                                                  .........:-+*##%%#*+=:..                          .............        
              ...........                                         ........ .......                                              ..........                                        ........  ......      
            ............                                        ............ ......                                          ...........                                         ............ .....     
         ............ .                                         .... ..  ..........                                        ............                                          .......   ........     
       .............                                            .... .............                                      ............                                             .... ............      
     .............                                              ...............                                       ............                                               ..............         
     ..........                                                   ...........                                         .........                                                    ..........           
     ........                                                        .....                                            .......                                                         ....              
       ...                                                                                                              ..                                                                              
''')
    input()

def monopoly():
    f = open('.\monopoly.txt', 'r')
    print(f.read())
    input()

def ordi():
    while True:
        f1 = open('.\ordi1.txt', 'r')
        f2 = open('.\ordi2.txt', 'r')
        print(f1.read())
        sleep(0.5)
        print(f2.read())
        sleep(0.5)
        
        temp = input()
        if temp != '':
            break

def menu():
    # Permet d'accéder à une image
    choix = int(input('''Selection de l'image:
        Dieu: 1
        Copernic: 2
        Lune: 3
        Kepler: 4
        Pomme: 5
        Patate triste: 6
        Science: 7
        Louis XIV: 8
        Engrenage: 9
        Locomotive: 10
        Bateau: 11
        Blé: 12
        Monopoly: 13
        Ordinateur: 14
        
        Aller à: '''))
    
    if choix == 1:
        dieu()
    elif choix == 2:
        copernic()
    elif choix == 3:
        lune()
    elif choix == 4:
        kepler()
    elif choix == 5:
        pomme()
    elif choix == 6:
        dieuTriste()
    elif choix == 7:
        science()
    elif choix == 8:
        louis()
    elif choix == 9:
        engrenage()
    elif choix == 10:
        loco()
    elif choix == 11:
        bateau()
    elif choix == 12:
        ble()
    elif choix == 13:
        monopoly()
    elif choix == 14:
        ordi()
    else:
        print("C'est pas entre 1 et 14 ça")

def main():
    print('\n' * 40)
    a = input('\t' * 10 + 'L\'épanouissement de la pensée scientifique' + '\n' * 25)
    
    if a != '':
        # Ouvre le menu pour accéder à une image directement après le titre.
        menu()
        sys.exit(0)
    
    print('Chargement en cours...' + '\n' * 6)
    sleep(2)
    transition()
    dieu()
    transition()
    copernic()
    transition()
    lune()
    transition()
    kepler()
    transition()
    pomme()
    transition()
    dieuTriste()
    transition()
    science()
    transition()
    louis()
    transition()
    engrenage()
    transition()
    loco()
    transition()
    bateau()
    transition()
    ble()
    transition()
    monopoly()
    transition()
    ordi()

if __name__ == '__main__': # Lance la fonction main()
    main()
    