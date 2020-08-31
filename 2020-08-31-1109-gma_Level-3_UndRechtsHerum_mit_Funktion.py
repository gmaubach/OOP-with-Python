'''
Created on 17.06.2018

@author: André Willms
'''

# Ab Python 3.8 müssen dlls als vertrauenswürdig markiert werden. 
# Deshalb ab 3.8.x von den unteren beiden Anweisungen den 
# Kommentar entfernen und den Pfad zum Projektverzeichnis 
# korrekt angeben 
import os 
os.add_dll_directory("D:\Selfcoding\WillmsBis040920\scara64anaconda") 

import ctypes
Scara = ctypes.cdll.scara

def dreheRechts():
    for i in range(3):
        Scara.dreheLinks();

Scara.starte(b"UndRechtsHerum");

Scara.gehe();

dreheRechts();
Scara.gehe();
Scara.gehe();
dreheRechts();

Scara.gehe();

Scara.beende()
