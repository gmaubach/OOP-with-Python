# -*- coding: utf-8 -*-
"""
Created on Wed Sep 2 13:26:10 2020

@author: Georg Maubach
"""

class Bruch:

    var = 1

    def __init__(self, z, n):                    # Konstruktor
        self._zaehler = z                        # Der Konstruktur muss genauso
        self._nenner = n                         # geschrieben werden, sonst ist
                                                 # es kein Konstruktor.
# Getter/Setter    
    def getZaehler(self):
        return self._zaehler
    
    def setZaehler(self, wert):
        if wert >= 0: self._zaehler = wert
        # nur positive Brueche
        # man kann nicht durch Null teilen
    
    def getNenner(self):
        return self._nenner
    
    def setNenner(self, wert):
        if wert >= 0: self._nenner = wert
        # nur positive Brueche

# Der Unterstrich "_" ist nur eine Bitte an den Verwender der Klasse,
# nicht direkt auf das Attribut von aussen zuzugreifen.
# Damit wird eine "theoretische" Datenkapselung erreicht, die bei anderen
# Programmiersprachen physisch realisiert wird.
#
# Will ich, dass ein Attribut mit gleichem Namen in Subklassen verwendet werden
# kann, muss ich das Attribut mit 2 Unterstrichen "__" beginnen kennzeichnen.
#
# Damit man auf die privaten Attribute von aussen zugreifen kann, erstellt man
# Methoden, die die Attribute aendern.

# Konstruktoren definieren, Objektvariablen. Objektvariablen definieren die
# Eigenschaften der Exemplare, die je Exemplar unterschiedlich sind.

# Klassenvariablen bleiben für alle Exemplare der Klasse gleich. Über#
# Klassenvariablen können die Objekte miteinander kommunizieren. 

    def ausgabe(self):
        """
        Schreiben Sie eine Methode ausgabe(), die den Bruch in der Form
        zaehler / nenner
        auf dem Bildschirm ausgibt.
        """
        print(self._zaehler, "/", self._nenner, sep=" ")

# Neben privaten Attributen, die mit "_" und "__" gekennzeichnet werden,
# kann ich auch private Methoden definieren, die mit "_" und "__" 
# gekennzeichnet werden.

# EOF .
