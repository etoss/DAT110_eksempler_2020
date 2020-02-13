import turtle
from gjennomgang_oving_2.c_sekskant import sekskant


# Oppgave d)
def sekskantmoenster(storrelse, avstand, kolonner, rader):
    for y in range(rader):
        for x in range(kolonner):
            if (x + y) % 2 == 0:
                sekskant(storrelse)
            else:
                sekskant(storrelse, "red")
            turtle.penup()
            turtle.forward(avstand)
        turtle.backward(avstand*kolonner)
        turtle.right(90)
        turtle.forward(avstand)
        turtle.left(90)


if __name__ == "__main__":
    kolonner = int(input("Antall sekskanter horisontalt? "))
    rader = int(input("Antall sekskanter vertikalt? "))
    sekskantmoenster(30, 70, kolonner, rader)
    turtle.done()
