# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:51:26 2019

@author: Maxence
"""

guess_me = input("Entrez un nombre (ps: \
vraiment juste un nombre, rien d'autre):")

try:
    guess_me = int(guess_me)

    if guess_me < 7:
        print('Too low\n')
    elif guess_me > 7:
        print('Too high\n')
    else:
        print('Just right\n')
except:
    print("HEUREUSEMENT QUE J'AI DEMANDÉ \
          UN NOMBRE\n")

guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('Too low\n')
    elif guess_me > 7:
        print('Oops\n')
        break
    else:
        print('Found it!\n')
        break
    start += 1
    
list = [3, 2, 1, 0]
i = 0
while i <= (len(list) - 1): #-1 car len commence à 1 et pas 0
    print(list[i])
    i += 1

list_even_number = [number for number in range(10) if number % 2 == 0]
#voir page 85 (107 sur 483)
print('\n', list_even_number, '\n')

squares = {number: (number * number) for number in range(10)}
print(squares, '\n')
#magie

set_odd_numbers = {number for number in range(10) if number % 2 == 1}
print(set_odd_numbers, '\n')

generator = (number for number in range(10))
for numbers in generator:
    print('Got', numbers)
#les deux arguments 'number' et 'numbers' sont indépendants

def good():
    another_list = ['Harry', 'Ron', 'Hermione']
    return another_list
print('\n', good(), '\n')

def get_odds():
    for number in range(10):
        if number % 2 == 1:
            yield number
temp = 0
for number in get_odds():
    if temp == 2: #permet d'avoir la troisième valeur
        print(number)
    temp += 1
    
def test(func):
    def nouvelle_fonction(*args, **kwargs):
        print('Start\n')
        print('Running function :', func.__name__)
        result = func(*args, **kwargs)
        print('Result :', result)
        print('End\n')
        return result
    return nouvelle_fonction
retest = test(good)
print(retest())

class OopsException(Exception):
    pass
try:
    raise OopsException('caught an oops')
except OopsException as exc:
    print(exc)

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A hunted yarn shop']
movies = dict( zip(titles, plots))
print('\n', movies)