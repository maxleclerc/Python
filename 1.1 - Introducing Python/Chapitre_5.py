c# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:37:42 2019

@author: Maxence
"""

from sources import zoo
zoo.hours()

from sources import zoo as menagerie
menagerie.hours()

from sources.zoo import hours as info
info()

plain = {"a":1, "b":2, "c":3}
for truc in plain:
    print(truc)

from collections import OrderedDict, defaultdict

fancy = OrderedDict(plain)
for truc in fancy:
    print(truc)
def list():
    return "Something for a"

dict_of_lists = defaultdict(list)
dict_of_lists['a']
print(dict_of_lists['a'])