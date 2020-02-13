def karakter_fra_prosent(prosent):
    if prosent >= 90:
        return "A"
    elif prosent >= 80:
        return "B"
    elif prosent >= 60:
        return "C"
    elif prosent >= 50:
        return "D"
    elif prosent >= 40:
        return "E"
    else:
        return "F"


prosent_streng = input("Skriv inn prosentscore: ")
prosent = int(prosent_streng)
karakter = karakter_fra_prosent(prosent)
print(karakter)
