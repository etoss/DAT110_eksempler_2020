fil_til_lesing = open("test.txt", "r")
fil_til_skriving = open("splittet_ord.txt", "w")
for linje in fil_til_lesing:
    ordene = linje.split()
    for ord in ordene:
        fil_til_skriving.write(ord + "\n")
fil_til_lesing.close()
fil_til_skriving.close()
