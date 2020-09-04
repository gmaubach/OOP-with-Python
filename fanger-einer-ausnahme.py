
try:
    x = int(input("Ganzahl eingeben: "))
    print("Gut gemacht")

except ValueError as e:
    print("Falsche Eingabe")
    print(e)

#--

x = int(input("Ganzahl eingeben: "))

if x < 0:
    raise ValueError("Falsch gemacht")

print("Programmende")
