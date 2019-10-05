d# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:56:19 2019

@author: Maxence
"""

class Person():
    def __init__(self, name):
        self.name = name
    pass

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name
    pass

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"
    pass

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
    pass

hunter = Person("Elmer Fudd")

print("The mighty hunter : ", hunter.name)

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(lawyer.name)

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name, bob.email)

class Car():
    def exclaim(self):
        print("I'm a car !")
    pass

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo ! Much like a car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here ?")
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Daffy'
print(fowl.name)

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.diameter)

class DuckDuck(Duck):
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

ducky = DuckDuck('Howard')
print(ducky.name)
ducky.name = 'Donald'
print(ducky.name)

#ducky.__name ne marche pas (donne une erreur)
#pour voir __name il faut utiliser
print(ducky._DuckDuck__name)

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A !")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

CoyoteWeapon.commercial()

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm huntting wabbits")
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
    
brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("self.text")' #PAS COMPRIS LE MANUEL

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)

first
print(first)

class Bill():
    def __init__(self, descrition):
        self.description = descrition

class Tail():
    def __init__(self, length):
        self.length = length

class Duck3():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail.')

a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck3(a_bill, a_tail)
duck.about()

#EXERCICES

class Thing():
    pass
print(Thing)

example = Thing()
print(example)

class Thing2():
    def letters(self):
        self.letters = 'abc'
print(Thing2.letters)

class Thing3():
    def letters(self):
        self.letters = 'xyz ?'

class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
    def __str__(self):
        return self.name + ' ' + self.symbol + ' ' #+ self.number

element1 = Element('Hydrogen', 'H', 1)
print(element1.name)
print(element1.symbol)
print(element1.number)

dict_hydrogen = {'name':'Hydrogen', 'symbol':'H', 'number': 1}
temp1 = dict_hydrogen['name']
temp2 = dict_hydrogen['symbol']
temp3 = dict_hydrogen['number']
hydrogen = Element(temp1, temp2, temp3)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

print(hydrogen)

class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

nounours = Bear()
print(nounours.eats())

lapin = Rabbit()
print(lapin.eats())

octodad = Octothorpe()
print(octodad.eats())

class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self, weapon):
        self.weapon = weapon
    def does(self):
        print('He', self.weapon.does())

laser_robot = Robot(Laser())
print(laser_robot.does())

claw_robot = Robot(Claw())
print(claw_robot.does())

telefon_robot = Robot(SmartPhone())
print(telefon_robot.does())
 D:\