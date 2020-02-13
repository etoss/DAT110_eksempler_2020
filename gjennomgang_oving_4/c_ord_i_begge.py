try:
    # Lager mengde med ordene i oving3.txt
    ord_i_oving_3 = set()
    with open("oving3.txt", "r", encoding="UTF-8") as fil_referanse:
        for linje in fil_referanse:
            linje = linje.strip()
            ordene = linje.split()
            for ord in ordene:
                ord = ord.strip(".:;,()")
                ord_i_oving_3.add(ord)

    # Lager mengde med ordene i oving4.txt
    ord_i_oving_4 = set()
    with open("oving4.txt", "r", encoding="UTF-8") as fil_referanse:
        for linje in fil_referanse:
            linje = linje.strip()
            ordene = linje.split()
            for ord in ordene:
                ord = ord.strip(".:;,()")
                ord_i_oving_4.add(ord)

    # Gjør intersection for å finne ordene som er i begge
    ord_i_begge = ord_i_oving_3.intersection(ord_i_oving_4)

    # Skriver ut ordene
    for ord in ord_i_begge:
        print(ord)
except IOError as e:
    print("Feil under lesing av fil: " + str(e))
except UnicodeDecodeError as e:
    print("Feil i koding av tekstfil: " + str(e))
