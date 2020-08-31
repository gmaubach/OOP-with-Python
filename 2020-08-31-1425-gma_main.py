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

from my_scara_loesungen import *;

if __name__ == "__main__":
    # loeseUndRechtsHerum();
    # loeseUmEckenHerum();
    # loeseQualderWahl();
    # loeseEntwederOder();
    
    # testAnAllenSeiten();        
    # loeseAnAllenSeiten();
    
    # loeseWieWeitNoch(); # funktioniert nicht
    # loeseWieWeitNoch_Musterloesung();
    
    loeseAnAllenSeiten2();
    pass
     
# EOF .
