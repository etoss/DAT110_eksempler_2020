def les_inn_tekst_fra_bruker(filnavn):
    fil_referanse = open(filnavn, "a", encoding="UTF-8")
    print("Skriv inn en tekst. Avslutt med tom linje.")
    linja = input("> ")
    fil_referanse.write(linja + "\n")
    while linja != "":
        linja = input("> ")
        if linja == "":
            break
        fil_referanse.write(linja + "\n")
    fil_referanse.close()


if __name__ == "__main__":
    les_inn_tekst_fra_bruker("test_encoding.txt")
