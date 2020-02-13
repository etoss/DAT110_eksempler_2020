hoyde = int(input("Høyde: "))
bredde = int(input("Bredde: "))
for y in range(hoyde):
    for x in range(bredde):
        print("*", end="")      # Kjører hoyde*bredde ganger!
    print()
