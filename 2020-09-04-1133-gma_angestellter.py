# -*- coding: utf-8 -*-

"""
Klasse Angestellter

Ergeänzen Sie die Klasse "Angestellter" um ein Attribut
"monatsgehalt" und die Methoden "getMonatsgehalt" und
"getJahresgehalt".
"""

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")

from person import *

class Angestellter(Person):
    def __init__(self, vorname, nachname, alter, monatsgehalt):
        super().__init__(vorname, nachname, alter)
        self._monatsgehalt = monatsgehalt
        # Hier kein Attribut "Jahresgehalt" anlegen,
        # weil das Jahresgehalt sehr leicht aus
        # Monatsgehalt berechnet werden kann.
        # Das Attribut "Jahresgehalt" wäre hier
        # Speicherplatzverschwendung.
        # Nur wenn die Berechnung so kompliziert ist,
        # dass die permanente Neuberechnung zu lange
        # dauert, dann würde ich ein Attribut
        # "Jahresgehalt" anlegen, um die Rechnenzeit
        # zu sparen. Ich opfere dann jedoch etwas
        # Speicherplatz.

    def getMonatsgehalt(self):
        return(self._monatsgehalt)

    def getJahresgehalt(self):
        return(self._monatsgehalt * 12)

    # In Python muss ich eine statische Methode
    # definieren, wenn ich mehrere Konstruktoren
    # haben will, da Python nur einen Konstruktor
    # pro Klasse zulasst.
    # Ich brauche hier eine statische Methode,
    # weil ich ja über den Klassennamen auf die
    # Methode zugreifen will, ohne dass ein
    # Objekt erzeugt sein muss.
    @staticmethod
    def createFromPerson(person, monatsgehalt):
        return(
            Angestellter(person.getVorname(),
                         person.getNachname(),
                         person.getAlter(),
                         monatsgehalt)
            )
    

# EOF .
