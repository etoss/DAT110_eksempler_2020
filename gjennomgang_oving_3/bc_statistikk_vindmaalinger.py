# Generell syntaks:  with ressurs as variabel.
#
# Sørger for at ressurs alltid lukkes når blokka er ferdig,
# uansett hvordan man går ut av blokka
try:
    with open("tall_filtrert.txt", "r") as fila:
        antall_maalinger = 0
        sum_maalinger = 0
        maks = -1
        min = 100000
        for linje in fila:
            try:
                vind_flyttall = float(linje)
            except ValueError:
                continue
            antall_maalinger += 1
            if vind_flyttall > maks:
                maks = vind_flyttall
            if vind_flyttall < min:
                min = vind_flyttall
            sum_maalinger += vind_flyttall
        gjennomsnitt = sum_maalinger/antall_maalinger
    with open("statistikk_vindmaalinger.txt", "w") as ut_fil:
        ut_fil.write(f"Antall: {antall_maalinger}\n")
        ut_fil.write(f"Gjennomsnitt: {gjennomsnitt:8.4f}\n")
        ut_fil.write(f"Maksimum: {maks:8.4f}\n")
        ut_fil.write(f"Minimum: {min:8.4f}")
except IOError as e:
    print("Feil under håndtering av en av filene: " + str(e))
except UnicodeDecodeError as e:
    print("Feil tekstformat i input fila: " + str(e))

# IOError hvis det er problem med en av filene. Hvis det er et problem, er det ikke noe poeng å fortsette.
# Derfor er omtrent all koden inni denne try-en. Blir det en feil, hopper den helt til slutten og avslutter.
#
# ValueError hvis det er et problem å konvertere til flyttall. Er det et problem med ei linje er det bare
# å hoppe til neste linje. Denne try-en er derfor lagt inni koden og bruker continue for å gå til neste linje.
