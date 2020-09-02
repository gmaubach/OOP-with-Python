# -*- coding: utf-8 -*-
"""
Created on Wed Sep 2 11:24:10 2020

@author: Georg Maubach

Schreiben Sie eine Funktion isSchaltjahr(), der ein Jahr übergeben wird
und die dann zurückgibt, ob das Jahr ein Schaltjahr ist oder nicht.

Definition Schaltjahr:
- Wenn ein Jahr durch 4 teilbar ist, ist es ein Schaltjahr.
- Wenn das Jahr durch 100 teilbar ist, dann ist es kein Schaltjahr, aber wenn
  es durch 400 teilbar ist, dann ist es doch eins.
"""

def istSchaltjahr(jahr):
    schaltjahr = False;

    if(jahr % 4 == 0): schaltjahr = True;
    if(jahr % 100 != 0): schaltjahr = False;
    if(jahr % 400 == 0): schaltjahr = True;

    return(schaltjahr);

def istSchaltjahr(jahr):                         # Musterlösung
    if ((jahr % 100 == 0 and jahr % 400 != 0) or
    jahr % 4 != 0):
        return False;
    else:
        return True;

if __name__ == "__main__":
    print("Schaltjahr ", schaltjahr);
