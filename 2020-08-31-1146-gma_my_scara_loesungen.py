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

from my_scara_funcs import dreheRechts; # alle Funktionen einbinden mit "*"

#-----------------------------------------------------------------------------
def loeseUndRechtsHerum():
    Scara.starte(b"UndRechtsHerum");

    Scara.gehe();

    dreheRechts();
    Scara.gehe();
    Scara.gehe();
    dreheRechts();

    Scara.gehe();

    Scara.beende()
#-----------------------------------------------------------------------------
