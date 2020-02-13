# Funksjon som leser inn vekt fra bruker og håndterer feil i brukerinput
def les_inn_vekt_kilo():
    vekt_flyttall = -1.0
    while vekt_flyttall < 0.0:
        vekt_streng = input("Vekten til pakken i kilo: ")
        try:
            vekt_flyttall = float(vekt_streng)
            if vekt_flyttall < 0.0:
                print("Vekta kan ikke være negativ!")
        except ValueError:
            if vekt_streng == "":
                vekt_flyttall = 0.0
            else:
                print("Vekta må være et lovlig flyttall! Prøv på nytt!")
                vekt_flyttall = -1.0
    return vekt_flyttall


# Endring av tidligere script for å bruke funksjonen
print("Finner totalpris for flere pakker. Avslutt med tom streng eller tallet 0.0")
total_pris = 0
while True:
    vekt_flyttall = les_inn_vekt_kilo()         # Kaller funksjonen og lagrer resultatet i variabelen vekt_flyttall
    if vekt_flyttall == 0.0:                    # Sjekker om takket er 0 og man skal avslutte.
        break                                   # Avslutter while-løkka
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
    print("Foreløpig total: " + format(total_pris, "7d"))
print("Total pris: " + format(total_pris, "7d"))
