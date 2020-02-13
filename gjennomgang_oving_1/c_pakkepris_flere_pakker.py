print("Finner totalpris for flere pakker")
vekt_streng = input("Vekten til pakken i kilo: ")
total_pris = 0             # Akkumulator, en verdi legges til for hver gang gjennom løkka
while vekt_streng != "":
    vekt_flyttall = float(vekt_streng)
    pakkepris = 0
    if vekt_flyttall <= 0.0:
        break
    elif vekt_flyttall <= 10:
        pakkepris = 149
    elif vekt_flyttall <= 25:
        pakkepris = 268
    elif vekt_flyttall <= 35:
        pakkepris = 381
    else:
        print("Pakker over 35 kilo er ikke tillatt!")
    total_pris += pakkepris
    vekt_streng = input("Vekten til pakken i kilo: ")
print("Total pris: " + format(total_pris, "7d"))
