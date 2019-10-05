# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:48:01 2019

@author: Maxence
"""

years_list = [1999, 2000, 2001, 2002, 2003, 2004]
print(years_list, '\n')

print(years_list[3], '\n')

print(years_list[-1], '\n')

things = ["mozzarella", "cinderella", "salmonella"]
print(things, '\n')

things[1].capitalize()
print(things, '\n')

things[0].upper()
print(things, '\n')

things.pop() #pop le dernier mot
print(things, '\n')

surprise = ["Groucho", "Chico", "Harpo"]
print(surprise, '\n')

temp = ' '.join(surprise[2:]) #prend Harpo
temp = temp.lower() #le met en minuscule
temp = temp[::-1] #le lit à l'envers
temp = temp.upper() #le met en majuscule
print(temp, '\n')

e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f["walrus"], '\n')

temp = list(e2f.items()) #crée une liste de e2f temporaire
f2e = {} #crée le dictionnaire f2e vide
i = 0
while i < 3:
    f2e[temp[i][-1]] = temp[i][0] #duo i de temp, deuxième mot en premier et premier mot en deuxième dans f2e
    i += 1
print(f2e, '\n')

print(f2e["chien"], '\n')

english_set = set(e2f)
print(english_set, '\n')

cats = ['Henri', 'Grumpy', 'Lucy']
octopi = {}
emus = {}
animals = {'Cats': cats, 'Octopi': octopi, 'Emus': emus}
plants = {}
other = {}
life = {'Animals': animals, 'Plants': plants, 'Other': other}
print(life.keys(), '\n') #les clés de life
print(life['Animals'].keys(), '\n') #les clés de Animals dans life
print(life['Animals']['Cats'], '\n') #miaou