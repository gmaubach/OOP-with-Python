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
        #-- Volumen
        if (v <= 0):
            raise ValueError("Volumen muss >0 sein.")
        elif (f > v):
            raise ValueError("Die Füllmenge ist groesser als der Becher")
        else:
            self._volumen = v

        #-- Fuellmenge
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

    #----------------------------
    # Eergänzen Sie die Klasse Becher um die Methode aufuellen() und
    # entnehmen().
    # Den Methoden werden die aufzufüllenden bzw. zu entnehmenden
    # Milliliter übergeben.
    # Die Methoden liefern zurück, wie viele ml tatsächlich
    # aufgefüllt/entnommen wurden.

    def auffuellen(self, menge):
        if (self._volumen >= (self._fuellmenge + menge)):
            menge_ergaenzt = self._volumen - self._fuellmenge
            self._fuellmenge = self._volumen
            return(menge_ergaenzt)
        else:
            self._fuellmenge += menge
            return(menge)
          
    def entnehmen(self, menge):
        if(self._fuellmenge < menge):
            entnommene_menge = self._fuellmenge
            self._fuellmenge = 0
            return(entnommene_menge)
        else:
            self._fuellmenge -= menge
            return(menge)

# https://www.python.org/dev/peps/pep-0008/

# EOF .


    
