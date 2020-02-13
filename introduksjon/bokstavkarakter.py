prosent_streng = input("Skriv inn prosentscore: ")
prosent = int(prosent_streng)
if prosent >= 90:
    print("A")
elif prosent >= 80:
    print("B")
elif prosent >= 60:
    print("C")
elif prosent >= 50:
    print("D")
elif prosent >= 40:
    print("E")
else:
    print("F")
