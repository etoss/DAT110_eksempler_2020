import turtle

RUTESTORRELSE = 50
RUTER_HORISONTALT = 6
RUTER_VERTIKALT = 3

for y in range(RUTER_VERTIKALT):
    for x in range(RUTER_HORISONTALT):
        for i in range(4):
            turtle.forward(RUTESTORRELSE)
            turtle.right(90)
        turtle.forward(RUTESTORRELSE)
    turtle.backward(RUTESTORRELSE*RUTER_HORISONTALT)
    turtle.right(90)
    turtle.forward(RUTESTORRELSE)
    turtle.left(90)
turtle.done()
