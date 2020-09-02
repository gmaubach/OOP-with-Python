# -*- coding: utf-8 -*-
"""
Created on Wed Sep 2 11:00:10 2020

@author: Georg Maubach

Schreiben Sie eine Funktion maximum, die zwei nummerische Werte
übergeben werden, und die dann den größeren der beiden Werte
zurückliefert.
"""
#------------------------------------------------------------------------------

def maximum(wert1, wert2):                      # FALSCH: Maximum zurückliefert
    if (wert1 > wert2):
        print("Maximum ist ", wert1);
    elif (wert2 > wert1):
        print("Maximum ist ", wert2);
    else:
        print("Beide Werte sind gleich groß.");

def maximum(wert1, wert2):
    if (wert1 > wert2):
        return(wert1);
    elif (wert2 > wert1):
        return(wert2);
    else:  # beide Werte gleich
        return(wert1);    

#------------------------------------------------------------------------------

if __name__ == "__main__":
    """
    maximum(1, 2);
    maximum(100, 1);
    maximum(5, 7);
    maximum(2, 2);
    """
    print("Maximum: ", maximum(1, 2));
    print("Maximum: ", maximum(100, 1));
    print("Maximum: ", maximum(5, 7));
    print("Maximum: ", maximum(2, 2));        

# EOF .
