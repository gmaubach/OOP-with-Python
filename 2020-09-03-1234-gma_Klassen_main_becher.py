# -*- coding: utf-8 -*-

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")
from becher import *

# Test Becher
a = Becher(500, 200)
a.ausgabe()

b = Becher(300)
b.ausgabe()

# c = Becher(-100)
# d = Becher(100, -200)

# Test auffuellen()
## Menge passt
a = Becher(200, 0)
menge = a.auffuellen(100)
print(menge)
a.ausgabe()

## Menge zu gross

# Test entnehmen()
## Menge vorhanden

## Menge zu klein



# EOF .
