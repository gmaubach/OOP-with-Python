# -*- coding: utf-8 -*-
"""
Created on Wed Sep 3 12:07:10 2020

@author: Georg Maubach

Programmieren Sie eine Klasse Becherhalter,
die maximal zwei Becher halten kann.
Implementieren Sie einen Konstruktor mit
entsprechenden Standardargumenten.
Implementieren Sie die Zugriffsmethoden
getPlatz1 und getPlatz2.
Verwenden Sie zur Verwaltung der Becher
normale Attribute, keine Arrays oder
Collections.
"""

import os
os.chdir("D:\Selfcoding\WillmsBis040920\scara64anaconda\Klassen")
from becher import *

class Becherhalter:
    def __init__(self, becher1 = None, becher2 = None):
        self._platz1 = becher1
        self._platz2 = becher2

    def setPlatz1(self, becher):
        if (self._platz1 == None):
            self._platz1 = becher
            return(True)
        else:
            return(False)

    def setPlatz2(self, becher):
        if (self._platz2 == None):
            self._platz2 = becher
            return(True)
        else:
            return(False)

    # Merke: get-Methode ist holen der Informtionen
    # über das Objekt, NICHT das physische Entfernen
    # des Objekts aus einem anderen Objekt, z. B.
    # Entfernen des Bechers aus dem Becherhalter.

    def getPlatz1(self):
        return(self._platz1)

    def getPlatz2(self):
        return(self._platz2)

    # Implementieren Sie für die Klasse Becherhalter
    # die Methoden
    # fuegeBecherHinzu(becher)
    # entferneBecher(Becher)
    # Die Methoden sollen funktionieren, d. h. Fehler
    # sollen abgefangen werden.

    def entferneBecher(self, becher):
        if (self._platz1 == becher):
            self._platz1 == None
            return(True)
        elif (self._platz2 == becher):
            self._platz2 == None
            return(True)
        else:
            return(False)

    def fuegeBecherHinzu(self, becher):
        if (self._platz1 == None):
            self._platz1 = becher
            return(True)
        elif (self._platz2 == None):
            self._platz2 = becher
            return(True)
        else:
            return(False)

    # Musterloesung
    def fuegeBecherHinzu(self, b):
        
        if self._platz1 is None and self._platz2 is not b:
            # es wird geprüft, ob derselbe Becher nicht schon
            # auf dem Platz steht und ich nicht versehentlich
            # denselben Becher auf zwei Plätze setze, was in
            # der Realität nicht vorkommt, aber in der
            # Programmierung schon.
            self._platz1 = b 
            return True 

        if self._platz2 is None and self._platz1 is not b:
            # Selber Kommentar wie in der vorherigen if-Bedingung.  
            self._platz2 = b 
            return True 

        return False 

    def entferneBecher(self, b): 
        if self._platz1 is b: 
            self._platz1 = None 
            return True 

        if self._platz2 is b: 
            self._platz2 = None 
            return True 
         
        return False

    # Implementieren Sie für die Klasse Becherhalter die Methoden
    # getBecherAnzahl()
    # getGesamtFullmenge()

    def getBecherAnzahl(self):
        anzahl = 0
        if (self._platz1 is not None): anzahl += 1
        if (self._platz2 is not None): anzahl += 1
        return(anzahl)

    def getGesamtFuellmenge(self):
        gesamtmenge = 0
        if (self._platz1 is not None)):
            gesamtmenge += self._platz1.getFuellmenge()
        if (self._platz2 is not None)):
            gesamtmenge += self._platz2.getFuellmenge()
        
# EOF .

