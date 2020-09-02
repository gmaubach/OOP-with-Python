# -*- coding: utf-8 -*-
"""
Created on Wed Sep 2 11:38:10 2020

@author: Georg Maubach

Schreiben Sie eine Funktion istPrim(), die einen
ganzzahligen Wert übergeben bekommt und die dann
zurückliefert, ob der Wert eine Primzahl ist oder
nicht.

Definition Primzahl:
- Zahl ist NUR durch 1 und durch sich selbst teilbar.
"""

def istPrim(wert):                               # Meine Lösung
    x = 2
    primzahl = True;

    while(x < wert):
        if(wert % x == 0):
            primzahl = False;
        x += 1
    
    return(primzahl);

def istPrin(wert):
    if (wert == 1) return False;

    max = wert / 2; # wenn der Teiler größer als die Hälfte ist,
                    # muss die Division nur noch ungerade Werte
                    # liefern.
    y = 2;
    while y <= max:
        if((x % y) == 0: return False; # alle weiteren Werte muss
                                       # ich dann nicht mehr weiter
                                       # prüfen. Damit das Programm
                                       # schneller.
        y += 1
    return True;


if __name__ == "__main__":
    print("Primzahl ", istPrim(2));    
    print("Primzahl ", istPrim(5));
    print("Primzahl ", istPrim(10));    
    print("Primzahl ", istPrim(99));

    pass
