import turtle


def rect( side) :
    for n in range(4) :
        turtle.forward(side)
        turtle.left(90)

side = 100
for i in range(10) :
    rect( side)
    turtle.left(10)
    side -= 10

turtle.exitonclick()

