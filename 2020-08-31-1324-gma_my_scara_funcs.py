# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:14:43 2020

@author: Georg Maubach
"""

# Ab Python 3.8 müssen dlls als vertrauenswürdig markiert werden. 
# Deshalb ab 3.8.x von den unteren beiden Anweisungen den 
# Kommentar entfernen und den Pfad zum Projektverzeichnis 
# korrekt angeben 
import os 
os.add_dll_directory("D:\Selfcoding\WillmsBis040920\scara64anaconda") 

import ctypes
Scara = ctypes.cdll.scara

def gehe2():
    Scara.gehe();
    Scara.gehe();

def gehe3():
    # Scara.gehe();
    # Scara.gehe();
    # Scara.gehe();
    
    # besser Code-Verdopplung vermeiden und
    # das, was ich schon habe, verwednen.
    gehe2();
    Scara.gehe();

def dreheRechts():
    for i in range(3):
        Scara.dreheLinks();

def dreheUm():
    Scara.dreheLinks();
    Scara.dreheLinks();

# EOF .
