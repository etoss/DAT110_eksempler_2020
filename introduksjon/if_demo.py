tallet_streng = input("Skriv inn et tall: ")
tallet = float(tallet_streng)
# if betingelse:
#   blokk
# else:
#   blokk
if tallet < 0:
    print("Tallet er negativt")
elif tallet == 0:
    print("Tallet er null")
else:
    print(str(tallet))
print("Avslutter")
