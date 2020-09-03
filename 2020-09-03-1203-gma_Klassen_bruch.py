# -*- coding: utf-8 -*-
"""
Created on Wed Sep 3 09:33:10 2020

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

    # Schreiben Sie eine Methode kuerzen(), die den aufrufenden Bruch kürzt
    # b.kuerzen().
    # Um zu kürzen, benötigt man den größten gemeinsamen Teiler für den
    # Zähler und den Nenner. Mit dem größten gemeinsamen Teiler werden
    # Zähler und Nenner dividiert.
    # Beide Funktionalitäten sollen als Methode in der Klasse Bruch
    # verfügbar sein.

    #------------------------------------------------------------------------------
    # Funktion liefert falsches Ergebnis, bitte überarbeiten

##    def my_ggT(self, zahl1: int, zahl2: int):
##        teiler1 = [] # Teiler für Zahl1
##        teiler2 = [] # Teiler für Zahl2
##
##        for i in range(zahl1):
##            if(zahl1 % (i + 1) == 0): teiler1.append(i)
##    
##        for i in range(zahl2):
##            if(zahl2 % (i + 1) == 0): teiler2.append(i)
##    
##        ggT = max(set(teiler1 + teiler2))
##
##        return(ggT)

    #------------------------------------------------------------------------------
    # Musterloesung

##    def ggT(self, x, y):
##        x = abs(x)
##        y = abs(y)
##
##        if x < y:
##            a = x
##        else:
##            a = y
##        if a == 0: return(1)
##
##        while (x % a != 0) or (y % a != 0):
##            a-=1
##    
##        return(a)

    #------------------------------------------------------------------------------
    # ggT kann bisher nur über ein Objekt der Klasse Bruch aufgerufen werden.
    # Damit ich ggT auch benutzen kann, ohne vorher ein Objekt zu definieren,
    # muss ich die Methode als Klassenmethode definieren, die dann über den
    # Klassennamen aufgerufen werden kann.
    # ACHTUNG: self entfällt bei Klassenmethoden.
    
    @staticmethod
    def ggT(x: int, y: int):
        x = abs(x)
        y = abs(y)

        if x < y:
            a = x
        else:
            a = y
        if a == 0: return(1)

        while (x % a != 0) or (y % a != 0):
            a-=1
    
        return(a)

    def kuerzen(self):
        ggT = self.ggT(self._zaehler, self._nenner)

        self._zaehler //= ggT
        self._nenner //= ggT

    #------------------------------------------------------------------------------
    # Schreibe eine Methode, die einen Bruch übernimmt und ein Bruch-Objekt
    # mit einem gekürztten Bruch zurückliefert.

    def getGekuerzt(self):
        ggT = self.ggT(self._zaehler, self._nenner)

        zaehler_gekuerzt = self._zaehler // ggT
        nenner_gekuerzt = self._nenner // ggT

        return(Bruch(zaehler_gekuerzt, nenner_gekuerzt))

     #------------------------------------------------------------------------------
     # Musterloesung
     # Die Musterloesung hat den Vorteil, dass die Funktionalität des Kürzens
     # nicht noch einmal implementiert werden muss, sondern nur an einer Stelle
     # steht und deshalb nur an einer Stelle gewartet werden muss.

     def getGekuerzt(self):
         temp = Bruch(self._zaehler, self._nenner)
         temp.kuerzen()
         return(temp)
        
   
# EOF .
