# Sammenlikningsfunksjon for frivillig oppgave f)
def sammenlikning(tuppel):
    return tuppel[1]

# Oppgave b)
filnavn = input("Skriv inn navn på fila: ")
try:
    ord_dict = {}
    with open(filnavn, "r", encoding="UTF-8") as fil_referanse:
        for linje in fil_referanse:
            linje = linje.strip()
            ordene = linje.split()
            for ord in ordene:
                ord = ord.strip(".:;,()")
                if ord in ord_dict:
                    teller = ord_dict[ord]
                    teller += 1
                    ord_dict[ord] = teller
                else:
                    ord_dict[ord] = 1
    for ord in ord_dict:
        print(f"Ordet \"{ord}\" forekommer {ord_dict[ord]} ganger")

    # Frivillig oppgave e)
    ordene = ord_dict.keys()        # Henter ut nøklene i dictionariet som en mengde
    ordene = list(ordene)           # Konverterer mengden til ei liste slik at den kan sorteres
    ordene.sort()                   # Sorterer lista. Siden lista inneholder strenger blir den sortert alfabetisk
    print("Sortert alfabetisk")
    for ord in ordene:
        print(f"Ordet '{ord}' forekommer {ord_dict[ord]} ganger")

    # Frivillig oppgave f)
    print("Sortert etter antall forekomster")
    ordene = []
    for ord in ord_dict:
        ordene.append((ord, ord_dict[ord]))         # Lager ei liste med (nøkkel, verdi) tupler
    ordene.sort(key=sammenlikning)                  # Sorterer lista med bruk av "sammenlikning" funksjonen
    for tuppel in ordene:
        print(f"Ordet '{tuppel[0]}' forekommer {tuppel[1]} ganger")

# Exception-håndteringa for oppgave b)
except IOError as e:
    print("Feil under lesing av fil: " + str(e))
except UnicodeDecodeError as e:
    print("Feil i koding av tekstfil: " + str(e))
