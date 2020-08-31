# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:14:10 2020

@author: Georg Maubach
"""

"""
print("Hallo", "Welt", sep = ", ", end = ":", flush = True)
sep: Trennzeichen zwischen Paramtern
end: Endezeichen nach Ausgabe der Parameter
flush: Schreibe nicht in den Ausgabepuffer, sondern gebe die Zeichen direkt und ohne Puffer aus.
"""

print("Hallo", "Welt", sep = ", ", end = ":", flush = True);
print("Nächste Ausgabe wird direkt hinter Ausgabe 1 geschrieben,", end = " ");
print("weil end = ':' ist.");

"""
Um Zeichen auszugeben, die im String nicht vorkommen dürfen, brauche
ich Escape-Sequenzen:
    
Esc.Sequenz	Bedeutung
\'	Das Zeichen '
\"	Das Zeichen "
\\	Das Zeichen \
\a	BEL (bell), akustisches Signal
\b	BS (backspace), Cursorposition ein Zeichen nach links (Zeichen wird gelöscht)
\f	FF (formfeed), Seitenvorschub
\n	NL (new line), Cursorposition wird auf Anfang der nächsten Zeile gesetzt.
\N{name}	Das Unicode-Zeichen mit dem Namen name
\r	CR (carriage return), Cursorposition wird auf Anfang der aktuellen Zeile gesetzt.
\t	HT (horizontal tab), nächste horizontale Tabulatorposition
\v	VT (vertical tab), nächste vertikale Tabulatorposition
\uxxxx	Unicode-Zeichen in vierstelliger hexadezimaler Darstellung (Nur u""-Strings)
\uxxxxxxxx	Unicode-Zeichen in achtstelliger hexadezimaler Darstellung (Nur u""-Strings)
\ooo	Zeichen in dreistelliger oktaler Darstellung
\xhh	Zeichen in zweistelliger hexadezimaler Darstellung

"""

# EOF .
