import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

l = turtle.Turtle()
l.color("red")

l.penup()
l.goto(-50, -50)
l.pendown()
for i in range(4):
    l.forward(100)
    l.left(90)

l.penup()
l.goto(-50, 50)
l.pendown()
sides = 0
while sides < 3:
    l.forward(100)
    l.left(120)
    sides += 1

l.hideturtle()
turtle.done()
