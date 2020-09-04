# -*- coding: utf-8 -*-

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")

from angestellter import *

# Test - Konstruktor
a = Angestellter("Georg", "Maubach", 50, 2500)
print(a.getName())
print(a.getMonatsgehalt())
print(a.getJahresgehalt())

b = Person("Georg", "Maubach", 50)
print(b.getNachname())

# Angestellter auf Basis einer bestehenden Person definieren
p = Person("Georg", "Maubach", 50)
a = Angestellter.createFromPerson(p, 2500)
print(a.getJahresgehalt())

# EOF .
