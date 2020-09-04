# -*- coding: utf-8 -*-

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")

from angestellter import *

"""
Schreiben Sie ein von "Angestellter" abgeleitete Klasse
"Filialleiter", deren Objekte zusätzlich noch Weihnachtsgeld
bekommen. Ein Filialleiter iste ein Angebstellter mit
zusätzlichem Weihnachtsgeld.
Lassen Sie die Problematik der getJahresgehalt-Methode
unberücksichtigt.
"""

class Filialleiter(Angestellter):
    def __init__(self, vorname, nachname, alter, monatsgehalt, weihnachtsgeld):
        super().__init__(vorname, nachname, alter, monatsgehalt)
        self._weihnachtsgeld = weihnachtsgeld

    def getWeihnachtsgeld(self):
        return(self._weihnachtsgeld)

    def getJahregehalt(self):
        """
        Die Methode so zu definieren, dass das Jahresgehalt
        neue berechnet wird, ist suboptimal, weil es die
        Berechnung in der Superklasse "Angestellter" schon
        gibt. Es wäre deshalb besser, auf die Methode
        "getJahresgehalt" aus der Superklasse "Angestellter"
        zuzugreifen. Das machen wir in der Definition
        der Methode "getJahresgehalt" in der auf diese Methode
        folgende Methode.

        Merke: Es gilt immer die zulettzt mit einem Namen
               definierte Methode. Vorhergehende Methoden
               mit demselben Namen werden überschrieben.
        """
        return(
            self._getMonatsgehalt() * 12 + self._weihnachtsgeld
            )

    def getJahresgehalt(self):
        return(
            super().getJahresgehalt() + self._weihnachtsgeld
            )

# EOF .
