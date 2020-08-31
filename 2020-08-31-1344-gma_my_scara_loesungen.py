# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:41:45 2020

@author: U2-User02
"""

# Ab Python 3.8 müssen dlls als vertrauenswürdig markiert werden. 
# Deshalb ab 3.8.x von den unteren beiden Anweisungen den 
# Kommentar entfernen und den Pfad zum Projektverzeichnis 
# korrekt angeben 
import os 
os.add_dll_directory("D:\Selfcoding\WillmsBis040920\scara64anaconda") 

import ctypes
Scara = ctypes.cdll.scara

from my_scara_funcs import *;

#-----------------------------------------------------------------------------

def loeseUndRechtsHerum():
    Scara.starte(b"UndRechtsHerum");

    Scara.gehe();

    dreheRechts();
    Scara.gehe();
    Scara.gehe();
    dreheRechts();

    Scara.gehe();

    Scara.beende();

#-----------------------------------------------------------------------------

def loeseUmEckenHerum():
     Scara.starte(b"UmEckenHerum");
     
     dreheUm();
     gehe3();
     dreheRechts();
     gehe2();
     Scara.dreheLinks();
     gehe3();
     Scara.dreheLinks();
     gehe2();
     
     Scara.beende();

#-----------------------------------------------------------------------------

def loeseQualderWahl():
    Scara.starte(b"QualderWahl");
    # Scara.starteSzenario("QualderWahl", 1); # Auwahl des Szenarios in einem Setting
    if (Scara.istVorneAbgrund()):
         Scara.dreheLinks();
    for i in range(2):
        Scara.gehe();
    Scara.beende();
    
def loeseEntwederOder():
    # Test Szenario, um zu wissen, wie das Spielfeld aussieht
    # Scara.starteSzenario(b"EntwederOder", 1);
    Scara.starte(b"EntwederOder");
    if (Scara.istVorneAbgrund()):
        Scara.dreheLinks();
        Scara.gehe();
        dreheRechts();
        Scara.gehe();
    else:
        Scara.gehe();
        Scara.dreheLinks();
        Scara.gehe();
    Scara.beende();

#-----------------------------------------------------------------------------

# EOF .

