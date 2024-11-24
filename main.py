import turtle

screen = turtle.Screen()
screen.bgcolor("Black")

t = turtle.Turtle()
t.pensize(5)
t.pencolor("White")
t.speed(5)
t.shape("arrow")

for _ in range(4) :
    t.forward(100)
    t.right(90)

t.hideturtle()
turtle.done()