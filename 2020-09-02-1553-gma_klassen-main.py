# -*- coding: utf-8 -*-
"""
Created on Wed Sep 2 13:25:10 2020

@author: Georg Maubach
"""

from bruch import *

b = Bruch(22, 7)
# print(b._zaehler, "/", b._nenner)
# man sollte nicht auf die Attribute direkt zugreifen.

b.ausgabe();
# Hier greife ich auf die Attribute ueber die Methode ausgabe() zu.
# Die Ausgabe ist identisch mit der Ausgabe des vorhergehenden
# Befehls.

x = Bruch(2, 7)
x.ausgabe()

y = Bruch(1, 2)
y.ausgabe()

print(x.var)
print(y.var)

x.var = 5
print(x.var)

y.var = 7
print(y.var)

x.setZaehler(5)
x.setNenner(2)

y.setZaehler(9)
y.setNenner(3)

x.getZaehler()
y.getZaehler()

x.ausgabe()
y.ausgabe()

#--------------------------

#---- Call by Value, für normale Variablen

def fkt(x):
    x = 20

y = 10
fkt(y)
print(y)

#---- Call by Reference, weil Objekt
def fkt(x):
    x.setZaehler(10)

y = Bruch(5,5)
fkt(y)
y.ausgabe()

#--- Copy Objekte
# Wenn ich das Objekt kopieren will
# brauche ich copy() aus dem copy-Modul
# copy = nur Objekt wird kopiert
# deepcopy = Objekt und Objektreferenzen innerhalb des Objekts wird kopiert

# Der "==" Operator prüft auf die Identität, ist es dasselbe Objekt.
# == und is macht dasselbe. Nur wenn ich mit __eq__ den == Operator
# ändere, machen == und is etwas unterschiedliches.

# EOF .
