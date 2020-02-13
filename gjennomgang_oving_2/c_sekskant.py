import turtle


# Funksjonen som tegner en sekskant, oppgave c)
def sekskant(storrelse=50, fyllfarge="blue"):
    turtle.fillcolor(fyllfarge)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(6):
        turtle.forward(storrelse)
        turtle.right(60)
    turtle.end_fill()


# Testekode for å teste at funksjonen virker før jeg gjør oppgave d)
if __name__ == "__main__":
    sekskant(100, "red")
    turtle.done()
