# Filer test med full unntakshåndtering.
#
# try-blokk forsøkes utført. Oppstår det te unntak under kjøring,
# sjekker systemet om det er en except-blokk som passer og kjører den.
# Hvis det ikke er en passende except-blokk så krasjer programmet som før.
#
# Det kan fint være flere except-blokker for samme try blokk
# Eksempelkoden har separate except for IOError (feil i lesing av fil slik som
# at fila ikke fins eller ikke er ledbar), UnicodeDecodeError (at tekstfila
# ikke bruker riktig kodetabell), og ValueError (at første linje i tekstfila
# ikke kan konverteres til et tall i linje 22.
#
# with-blokken har følgende syntaks: "with ressurs as variabel". Her er ressursen
# resultatet an kallet til open-funksjonen, og variabelen er fil_referanse.
#
# En with-blokk er en blokk hvor ressursen (fila i dette tilfellet) lukkes automatisk
# når blokken er ferdig, uansett hvordan man går ut av blokken (om det skjer et
# unntak eller ikke).
try:
    with open("test.txt", "r", encoding="UTF-8") as fil_referanse:
        linje = fil_referanse.readline()
        tall = int(linje)
        print(str(tall))
        for linje in fil_referanse:
            print(linje, end="")
except IOError as e:
    print("Feil i håndtering av fil: " + str(e))
except UnicodeDecodeError as e:
    print("Feil i koding av tekstfil: " + str(e))
except ValueError as e:
    print("Fila inneholder noe i tall-posisjonen som ikke er et tall! " + str(e))
# finally:   - Gammel måte å få lukket ei fil på, en Finally blokk skjer etter try ... except,
#              og utføres uansett om det ble et unntak eller ikke.
#     try:
#         fil_referanse.close()
#     except IOError:
#         print("Feil under close")
