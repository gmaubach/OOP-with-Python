# -*- coding: utf-8 -*-

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")

from filialleiter import *

# Test - Konstruktor
angestellter = Filialleiter("Georg", "Maubach", 50, 2500, 500)
print(angestellter.getNachname())

print(angestellter.getJahresgehalt())

# EOF .
