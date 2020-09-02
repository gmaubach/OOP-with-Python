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
       return(wert1);
    else:
        return(wert2);

def maximum3(x, y, z):
    return(maximum(maximum(x, y), z));

# LIT: Knuth: The Art of Computer Programming

#------------------------------------------------------------------------------

if __name__ == "__main__":
    print("Maximum: ", maximum3(1, 2, 3));
    print("Maximum: ", maximum3(100, 50, 1));
    print("Maximum: ", maximum3(5, 7, 9));
    print("Maximum: ", maximum3(2, 2, 2));        

# EOF .
