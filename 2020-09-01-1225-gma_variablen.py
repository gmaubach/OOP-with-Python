'''
Created on 01.09.2020

@File: variablen.py
@author: Georg Maubach
'''

def frageNachName():
    nname = input("Nachname: ");
    vname = input("Vorname: ");

    print("Sie heissen {} {}.".format(vname, nname));
    print("Sie heissen", vname, nname, "."); # Der Punkt ist dann wegen sep="" abgesetzt.
    print("Sie heissen ", vname, " ", nname, ".", sep = "");
    print("Sie heissen", vname, nname, "."); # Der Punkt ist wieder abgesetzt.
    print("Sie heissen ", vname, " ", nname, ".", sep = "");
    print(f"Sie heissen {vname} {nname}."); # f-Strings in print() sind am einfachsten.

def quadriere():
    # zahl = int(input("Gebe bitte eine Zahl ein: ")); # input liefert String, nicht Zahl als int() oder float()
    # deshalb:
    zahl = int(float(input("Gebe bitte eine Zahl ein: "))); # String erst in float() und dann in int() umwandeln
    int("Zahl als int", int(5.0));
    print("Deine Zahl zum Quadrat ist", zahl**2);

def gebeRestAus():
    zahl1 = int(float(input("Gebe Zahl 1 ein: ")));
    zahl2 = int(float(input("Gebe Zahl 2 ein: ")));

    print(f"Das Ergebnis von {zahl1}/{zahl2} ist {int(zahl1//zahl2)}, Rest {zahl1 % zahl2}."); # Wichtig: Ganzahldivision // verwenden

def gebeRestAus_Musterloesung():
    x = int(input("Zahl1: "));
    y = int(input("Zahl2: "));

    quotient = x // y;
    rest = x % y;

    print("Das Ergebnis von {0}/{1} ist {2}, Rest {3}.".format(zahl1, zahl2, quotient, rest)); 
    # Mit 0, 1, 2, 3 kann auf die einzelnen Argumente aus .format() zugegriffen werden, z.B.
    # um ein Argument mehrfach zu verwenden oder
    # um die Reihenfolge zu ändern.

def testGeradeUngerade():
    x = int(input("Zahl: "));

    if (x % 2 == 0):
        print("Zahl ist gerade.");
    else:
        print("Zahl ist ungerade.");

def FahrenheitInCelsius():
    fahrenheit = int(float(input("Grad Fahrenheit: ")));
    celsius = round((5/9)*(fahrenheit - 32), 1); 
    # Python macht eine Fliesskommezahl aus der Division. Andere Sprachen machen daraus denselben
    # Datentyp wie die Eingabe. 5/9 ist dann Null. Um das zu vermeiden:
    # 1. erst immer im Term multiplizieren.
    # 2. erst nach allen Multiplikationen dividieren.
    # Deshalb ist das besser:
    celsius = round((5 * (fahrenheit - 32) / 9), 1);
    print(f"{fahrenheit} Grad Fahrenheit sind {celsius} Grad Celsius.");
    # Mathematische Funktionen stehen im "math" Package.
    # Mathematische Funktionen:
    # round(wert):             runden
    # round(wert, praezision): runden auf bestimmte Stelle
    # floor(wert):             abrunden auf nächste ganze Zahl
    # ceil(wert):              aufrunden auf nächste ganze Zahl


if __name__ == "__main__":
    # frageNachName();
    # quadriere();
    # gebeRestAus();
    # testGeradeUngerade();
    FahrenheitInCelsius();

# EOF .
