import turtle

turtle.bgcolor("black")


t = turtle.Turtle()

t.speed("fastest")
t.hideturtle()
t.pencolor("white")


for number in range(4000):
    t.forward(number+1)
    t.right(89)
    


turtle.done()

