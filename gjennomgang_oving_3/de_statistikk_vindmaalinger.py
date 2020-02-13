# Fila er sortert på dato. Det er derfor bare nødvendig å sjekke for om datoen endrer seg
# og skrive ut til ut-fila etter hvert, man trenger ingen samlingsobjekter. Å bruke
# samlingsobjekter, lagre alle resultatene udnerveis, og skrive ut alt etterpå er en alternativ løsning her.
try:
    with open("csv_frivillig_oving_3.txt", "r") as fila:
        with open("statistikk_frivillig.txt", "w") as ut_fil:
            antall_maalinger = 0
            sum_maalinger = 0
            maks = -1
            min = 100000
            dato = ""
            for linje in fila:
                verdier = linje.strip().split(";")
                if len(verdier) != 3:                       # Feilsjekk: Hver linje skal ha 3 innslag. Noe annet er feil.
                                                            # Hopper til neste linje ved feil.
                    continue
                if verdier[0] != dato and dato != "":       # Hvis dato har endret seg siden sist linje:
                    if antall_maalinger != 0:               # Hvis det er gjort målinger på forrige dato
                        # Skriver ut resultatene til fila
                        gjennomsnitt = sum_maalinger/antall_maalinger
                        ut_fil.write(f"Dato: {dato}\n")
                        ut_fil.write(f"Antall: {antall_maalinger}\n")
                        ut_fil.write(f"Gjennomsnitt: {gjennomsnitt:8.4f}\n")
                        ut_fil.write(f"Maksimum: {maks:8.4f}\n")
                        ut_fil.write(f"Minimum: {min:8.4f}\n\n")
                    # Resetter statistikken for neste dato
                    antall_maalinger = 0
                    sum_maalinger = 0
                    maks = -1
                    min = 100000
                    dato = verdier[0]
                elif dato == "":                            # Er dette første linje, sett datoen uten å resette
                    dato = verdier[0]
                vind_flyttall = float(verdier[2])
                if vind_flyttall > 200:                     # Feilsjekk: Er vinden for høy er det feil, hopp til neste linje
                    continue
                antall_maalinger += 1
                if vind_flyttall > maks:
                    maks = vind_flyttall
                if vind_flyttall < min:
                    min = vind_flyttall
                sum_maalinger += vind_flyttall
            gjennomsnitt = sum_maalinger/antall_maalinger
except IOError as e:
    print("Feil under håndtering av en av filene: " + str(e))
except UnicodeDecodeError as e:
    print("Feil tekstformat i input fila: " + str(e))

# IOError hvis det er problem med en av filene
# ValueError hvis det er et problem å konvertere til flyttall
