'''
Created on 31.08.2020

@author: Georg Maubach
'''

# Ab Python 3.8 müssen dlls als vertrauenswürdig markiert werden. 
# Deshalb ab 3.8.x von den unteren beiden Anweisungen den 
# Kommentar entfernen und den Pfad zum Projektverzeichnis 
# korrekt angeben 
import os 
os.add_dll_directory("D:\Selfcoding\WillmsBis040920\scara64anaconda") 

import ctypes
Scara = ctypes.cdll.scara

from my_scara_funcs import dreheRechts; # alle Funktionen einbinden mit "*"

def loeseUndRechtsHerum():
    Scara.starte(b"UndRechtsHerum");

    Scara.gehe();

    dreheRechts();
    Scara.gehe();
    Scara.gehe();
    dreheRechts();

    Scara.gehe();

    Scara.beende()

loeseUndRechtsHerum();

