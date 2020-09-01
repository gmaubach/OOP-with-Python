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
# Folgende Zeile fuer VisualStudio Code
os.environ['QT_PLUGIN_PATH'] = "D:\Selfcoding\WillmsBis040920\scara64anaconda"

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

def testAnAllenSeiten():
     Scara.starteSzenario(b"AnAllenSeiten", 0);
     # Scara.starteSzenario(b"AnAllenSeiten", 1);
     # Scara.starteSzenario(b"AnAllenSeiten", 2);
     # Scara.starteSzenario(b"AnAllenSeiten", 3);

def loeseAnAllenSeiten():
    Scara.starte(b"AnAllenSeiten");
    if (Scara.istVorneAbgrund()):
        if (Scara.istVorneAbgrund()):
            Scara.dreheLinks();
            if (Scara.istVorneAbgrund()):
                Scara.dreheLinks();
                if(Scara.istVorneAbgrund()):
                    Scara.dreheLinks();
    gehe2();
    Scara.beende();

#-----------------------------------------------------------------------------

def loeseWieWeitNoch():
    Scara.starte(b"WieWeitNoch");
    for i in range(4):
        if (Scara.istVorneAbgrund()):
           break;        
        else:
            Scara.gehe();
    Scara.beende();
            
def loeseWieWeitNoch_Musterloesung():
    Scara.starte(b"WieweitNoch");
    Scara.gehe();
    if Scara.istVorneAbgrund() == False: Scara.gehe();
    if Scara.istVorneAbgrund() == False: Scara.gehe();
    if Scara.istVorneAbgrund() == False: Scara.gehe();
    Scara.beende();     

#-----------------------------------------------------------------------------

def loeseAnAllenSeiten2():
    Scara.starte(b"AnAllenSeiten");
    while (Scara.istVorneAbgrund()):
        Scara.dreheLinks();
    gehe2();
    Scara.beende();
    
#-----------------------------------------------------------------------------

def loeseDerLinksKnick(szenario = 1):
    Scara.starte(b"DerLinksKnick", szenario);
    while(Scara.istVorneAbgrund()) == 0:
        Scara.gehe();
    Scara.dreheLinks();
    while(Scara.istVorneAbgrund() == 0):
        Scara.gehe();
    Scara.beende();

def loeseDerLinksKnick_Musterloesung():
    Scara.starte(b"DerLinksKnick");
                 
    geheBisAbgrund();
    Scara.dreheLinks();
    geheBisAbgrund();
    
    Scara.beende();
    
#-----------------------------------------------------------------------------

def loeseWechselknick(szenario = 1):
    Scara.starte(b"Wechselknick", szenario);
    
    geheBisAbgrund();
    Scara.dreheLinks();
    if (Scara.istVorneAbgrund() == True):
        Scara.dreheLinks();
        Scara.dreheLinks();
    geheBisAbgrund();
    
    Scara.beende();
    
def loeseWechselknick_Musterloesung(szenario = 1):
    Scara.starte(b"Wechselknick", szenario);
    
    geheBisAbgrund();
    Scara.dreheLinks();
    if (Scara.istVorneAbgrund() == True):
        dreheUm();
    geheBisAbgrund();
    
    Scara.beende();

#-----------------------------------------------------------------------------

def loeseVorUndZurueck(szenario = 3):
    Scara.starte(b"VorUndZurueck", szenario);
    
    while(Scara.stehtAufAnkh() == 0):
        while (Scara.istVorneAbgrund() == 1):
            Scara.dreheLinks();
        Scara.gehe();

    Scara.beende();
    
def loeseVorUndZurueck_Musterloesung():
    Scara.starte(b"VorUndZurueck");
    
    while (not Scara.stehtAufAnkh()):
        if (Scara.istVorneAbgrund()):
            dreheUm();
        Scara.gehe();
        
    Scara.beende();
    
#-----------------------------------------------------------------------------

def loeseImKreisHerum():
    pass

#-----------------------------------------------------------------------------

def loeseAllgemein():
    while (not Scara.stehtAufAnkh()):
        if (Scara.istVorneAbgrund()):
            dreheUm();
        Scara.gehe();

def loeseDieLiegendeAcht():
    Scara.starte(b"DieLiegendeAcht");
    
    loeseAllgemein();
        
    Scara.beende();   
    
    # Funktioniert nicht. Es wird ein Flag gebraucht,
    # das den Käfer auch mal nach rechts dreht,
    # damit er alle Weg ausprobiert.
    
#-----------------------------------------------------------------------------

def loeseNachLinksUndRechts():
    Scara.starte(b"NachLinksUndRechts");
    
    while not(Scara.stehtAufAnkh()):
        if (Scara.istVorneAbgrund()):
            Scara.dreheLinks();
        else:
            Scara.gehe();
            
    # Funktioniert nicht.

    Scara.beende();

def loeseNachLinksUndRechts_Musterloesung():
    Scara.starte(b"NachLinksUndRechts");
    
    while not(Scara.stehtAufAnkh()):
        dreheRechts();
        while Scara.istVorneAbgrund():
            Scara.dreheLinks();
        Scara.gehe();

    Scara.beende();
    
def loeseNachLinksUndRechts2():
    Scara.starte(b"NachLinksUndRechts");
    
    while not(Scara.stehtAufAnkh()):
        if (Scara.istVorneAbgrund()):
            Scara.dreheLinks();
        else:
            Scara.gehe();
    
    # geht nicht

def loeseEinNormalesLabyrinth():
    Scara.starte(b"EinNormalesLabyrinth");
    pass;
    Scara.beende();
    
#-----------------------------------------------------------------------------

def loesePalettenIntro():
    """
    Mit istVornePalette wird geprüft, ob eine oder mehrere Paletten vor Scara liegen.
    Mit nimmPalette hebt Scara die vor ihm liegende Palette auf. Liegt dort keine Palette, gibt es einen Fehler.
    Mit legePalette legt Scara die getragene Palette vor ihm ab. Ist vor ihm kein erlaubter Platz, gibt es einen Fehler.
    Mit holePalettenhoehe kann die Höhe des Stapels vor Scara bestimmt werden, aber nur, wenn dort auch Paletten liegen.
    """
    Scara.starte(b"PalettenIntro");
    
    dreheUm();
    if (Scara.istVornePalette()):
        Scara.nimmPalette();
    dreheUm();
    geheBisAbgrund();
    Scara.legePalette();
    geheBisAbgrund();

    Scara.beende();

#-----------------------------------------------------------------------------

def loeseDerAbgrund():
    Scara.starte(b"DerAbgrund");
    
    dreheUm();
    while(Scara.istVornePalette() == 0):
        Scara.gehe();
    if(Scara.istVornePalette()):
        Scara.nimmPalette();
    dreheUm();
    geheBisAbgrund();
    Scara.legePalette();
    geheBisAbgrund();

    Scara.beende();   

#-----------------------------------------------------------------------------

def loeseJenseitsDesAbgrunds_Musterloesung(szenario):
    Scara.starte(b"JenseitsDesAbgrunds");

    geheBisAbgrund();

    if not Scara.stehtAufAnkh():
        dreheUm();

        while Scara.istVornePalette() == False: 
            Scara.gehe() 
 
        Scara.nimmPalette() 
        dreheUm() 
        geheBisAbgrund() 
 
        Scara.legePalette() 
        geheBisAbgrund() 

    Scara.beende();

#-----------------------------------------------------------------------------

def loeseJenseitsDesAbgrunds(szenario = 1):
    Scara.starte(b"JenseitsDesAbgrunds", szenario);
    habePalette = False;

    dreheUm();
    geheBisAbgrund();
    dreheUm();
    Scara.gehe();
    dreheUm();
    if(Scara.istVornePalette()):
        Scara.nimmPalette();
        habePalette = True;
    dreheUm();
    geheBisAbgrund();
    if(habePalette == True):
        Scara.legePalette();
    geheBisAbgrund();

    Scara.beende();

#-----------------------------------------------------------------------------

def loeseDerWanderndeAnkh(szenario):
    Scara.starte(b"DerWanderndeAnkh");
    habePalette = False;

    while not(Scara.stehtAufAnkh() and Scara.istVornePalette()):
        if(Scara.istVornePalette()):
            Scara.nimmPalette();
            habePalette = True;
            dreheUm();
        Scara.gehe();

    Scara.beende();

def loeseDerWanderndeAnkh_Musterloesung(szenario):
    Scara.starte(b"DerWanderndeAnkh");

    while (not Scara.stehtAufAnkh() 
           and not Scara.istVorneAbgrund()): 
        Scara.gehe() 
 
    if not Scara.stehtAufAnkh(): 
        dreheUm() 
 
        while Scara.istVornePalette() == False: 
            Scara.gehe() 
 
        Scara.nimmPalette() 
        dreheUm() 
        geheBisAbgrund() 
        Scara.legePalette() 
     
        while not Scara.stehtAufAnkh(): 
            Scara.gehe() 
 
    Scara.beende()

#-----------------------------------------------------------------------------

def loeseWoIstDerAnkh_Musterloesung(szenario):
    Scara.starte(b"WoIstDerAnkh", szenario);

    geheBisAbgrund();
    dreheUm();

    while Scara.istVorneAbgrund() == False and \
    Scara.stehtAufAnkh() == False:
        Scara.gehe();

    Scara.beende();

#-----------------------------------------------------------------------------

def loeseImKreisOhneAnkh(szenario):
    """
    Testszenarien: 2, 13, 341, 6201
    """
    Scara.starte(b"ImKreisOhneAnkh");

    i = 0;

    while(not Scara.stehtAufAnkh() 
    and not Scara.istVorneAbgrund()
    and i > 4):
        Scara.gehe();
        if(Scara.istVorneAbgrund()):
            pass;
    # nicht fertig

    Scara.beende();

def loeseImKreisOhneAnkh_Musterloesung(szenario):
    Scara.starte(b"ImKreisOhneAnkh");

    drehungen = 0;

    while (Scara.stehtAufAnkh() == False and \
        drehungen < 4):
        if Scara.istVorneAbgrund():
            dreheRechts();
            drehungen += 1;
        else:
            Scara.gehe();
    
    Scara.beende();

#-----------------------------------------------------------------------------

def loeseFesteEntfernung():
    Scara.starte(b"FesteEntfernung");

    for i in range(10):
        Scara.gehe();

    Scara.beende();

def loeseFesteEntfernung_Musterloesung():
    Scara.starte(b"FesteEntfernung");

    x = 1;

    while x <= 10:
        Scara.gehe();
        x += 1;
    
    # Hier hat x den Wert 11.
    
    Scara.beende();

#-----------------------------------------------------------------------------

# EOF .

