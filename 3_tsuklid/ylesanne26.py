import turtle
t = turtle.Turtle()
length = 5
i = 0
while i < 40:
    t.forward(length)
    t.right(90)
    length += 5
    i += 1
turtle.done()
