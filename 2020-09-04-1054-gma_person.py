# -*- coding: utf-8 -*-

"""
Erstellen Sie eine Klasse "Person", deren Objekte
Nachnamen
Vornamen
Alter einer Person
speichern.
Überlegen Sie sich einen sinnvollen Konstruktor und
Zugriffsmethoden.
"""

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")

class Person():
    def __init__(self, v: str, n: str, a: int):
        self._vorname = v
        self._nachname = n
        self.setName(v, n)
        self.setAlter(a)
        
    def getVorname(self):
        if (len(self._vorname) > 0):
            return(self._vorname)
        else:
            return(None)

    def setVorname(self, v):
        if (len(v) > 0):
            self._vorname = v
        else:
            raise ValueError("Vorname muss mindestens einen Buchstaben haben!")

    def getNachname(self):
        if (len(self._nachname) > 0):
            return(self._nachname)
        else:
            return(None)

    def setNachname(self, n):
        if (len(n) > 0):
            self._nachname = n
        else:
            raise ValueError("Nachname muss mindestens einen Buchstaben haben!")
        
    def setName(self, v: str, n: str):
        self._vorname = v
        self._nachname = n
        self._name = v + " " + n

    def getName(self):
        return(self._name)

    def getAlter(self):
        if (self._alter > 0):
            return(self._alter)
        else:
            return(None)

    def setAlter(self, a):
        if (a > 0):
            self._alter = a
        else:
            raise ValueError("Alter muss grösser Null sein!")

    #-- Musterloesung
    def baueNamen(self) -> str:
        return(self._vorname + " " + self._nachname)

# EOF .
