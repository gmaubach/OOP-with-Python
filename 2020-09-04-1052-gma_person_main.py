# -*- coding: utf-8 -*-

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")

from person import *

# Test Person - Konstruktor
a = Person(v = "Georg", n = "Maubach", a = 50)
print(a.getVorname())
print(a.getNachname())
print(a.getAlter())

# Test Person - Getter/Setter
a.setVorname("Asterix")
print(a.getVorname())

a.setNachname("Gallier")
print(a.getNachname())

a.setName("Obelix", "Dicker")
print(a.getName())

a.setAlter(500)
print(a.getAlter())

print(a.baueNamen())

# Bis hier Methoden OK !!!

# EOF .
