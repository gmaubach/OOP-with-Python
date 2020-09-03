# -*- coding: utf-8 -*-
"""
Created on Wed Sep 3 12:07:10 2020

@author: Georg Maubach

Programmieren Sie eine Klasse Becher, die Volumen und Fullmenge
des Bechers in Milliliter als Fliesskommazahl speichert.

Schreiben Sie einen Konstruktor für Volumen und Fullmenge,
setzen Sie fur leere Becher ein Standardagrument ein.

Schreiben Sie eine ausgabe-Methode.

Implementieren Sie Getter für die Attribute (keine Setter).

Prüfen Sie auf gültigen Zustand.
"""

class Becher:
    def __init__(self, v, f = 0):
        if (v <= 0):
            raise ValueError("Volumen muss >0 sein.")
        elif (f > v):
            raise ValueError("Die Füllmenge ist groesser als der Becher")
        else:
            self._volumen = v
        if (f < 0):
            raise ValueError("F muss >=0 sein.")
        else:
            self._fuellmenge = f

    def ausgabe(self):
        print("Volumen: ", self._volumen,
              "Füllmenge: ", self._fuellmenge)

    def getFuellmenge(self):
        return(self._fuellmenge)

    def getVolumen(self):
        return(self._volumen)

# https://www.python.org/dev/peps/pep-0008/

# EOF .


    
