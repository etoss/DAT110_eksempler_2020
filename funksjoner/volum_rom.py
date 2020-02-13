# Regner ut volumet av et rom


# def funksjonsnavn(parametre): blokk
def les_inn_flyttall(representerer="Tall"):
    tall_streng = input(representerer + ": ")
    tall = float(tall_streng)
    while tall <= 0:
        print(representerer + " må være positiv!")
        tall_streng = input(representerer + ": ")
        tall = float(tall_streng)
    return tall


def volum_av_rom():
    print("Volumet til et rom:")
    lengde = les_inn_flyttall("Lengde")
    bredde = les_inn_flyttall("Bredde")
    hoyde = les_inn_flyttall("Høyde")
    volum = lengde*bredde*hoyde
    print("Volumet er: ", str(volum))


if __name__ == "__main__":
    print("Kjører main koden")
    volum_av_rom()
