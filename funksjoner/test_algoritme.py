# Eksempel på hvordan å løse et problem gjennom å dele problemet i deler
# og løse hver del for seg, en etter en.
#
# Tegn en "diamant" med oppgitt størrelse. Eksempel med størrelse 4:
# ...*...
# ..*.*..
# .*...*.
# *.....*
# .*...*.
# ..*.*..
# ...*...
#
# Foreløpig kode: Tegner opp sida øverst til venstre.
print("Diamant eksempel")
storrelse = int(input("Størrelse: "))
for y in range(storrelse):
    for x in range(storrelse):
        if x == storrelse-y-1:
            print("*", end="")
        else:
            print(" ", end="")
    for x in range(storrelse-1):
        if x == y-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for y in range(1, storrelse):
    for x in range(storrelse):
        if x == y:
            print("*", end="")
        else:
            print(" ", end="")
    for x in range(storrelse):
        if x == storrelse-y-2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
