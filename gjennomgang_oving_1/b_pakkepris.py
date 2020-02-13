# Testing: Test hver vei gjennom en kode (if-setning)
print("Finner prisen til en pakke")
vekt_streng = input("Vekten til pakken i kilo: ")
vekt_flyttall = float(vekt_streng)
pakkepris = 0
if vekt_flyttall < 0.0:
    print("Pakken kan ikke ha en negativ vekt!")
elif vekt_flyttall <= 10:
    pakkepris = 149
elif vekt_flyttall <= 25:
    pakkepris = 268
elif vekt_flyttall <= 35:
    pakkepris = 381
else:
    print("Pakker over 35 kilo er ikke tillatt!")
if pakkepris != 0:
    print("En pakke på " + str(vekt_flyttall) + " koster " + str(pakkepris))
