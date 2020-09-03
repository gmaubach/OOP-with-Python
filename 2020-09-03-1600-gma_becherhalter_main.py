# -*- coding: utf-8 -*-

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")
from becher import *
from becherhalter import *

print("-- Test - Objekt --")
b1 = Becher(500, 300)
b2 = Becher(400)

halter1 = Becherhalter(b1, b2)
halter2 = Becherhalter(b1)

print("-- Test - getter --")
c = halter1.getPlatz1()
c.ausgabe()
d = halter2.getPlatz2()
# d.ausgabe()

print("-- Test - entferne/fuegeHinzu --")

a = Becher(100)
b = Becher(200)
c = Becher(300)

bh1 = Becherhalter(a)
ergebnis = bh1.fuegeBecherHinzu(b)
print(ergebnis)

ergebnis = bh1.fuegeBecherHinzu(c)
print(ergebnis)

ergebnis = bh1.entferneBecher(c)
print(ergebnis)

ergebnis = bh1.entferneBecher(a)
print(ergebnis)

print("-- Test - getBecherAnzahl() --")
a = Becher(100,100)
b = Becher(200,150)

bh = Becherhalter(a, b)
print(bh.getBecherAnzahl())

print("-- Test - getGesamtFuellmenge --")
print("Füllmenge a = ", a.getFuellmenge())
print("Füllmenge b = ", b.getFuellmenge())
print("Gesamtfüllmenge = ", bh.getGesamtFuellmenge())

# EOF .
