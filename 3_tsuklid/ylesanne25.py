import turtle
sides = int(input("Mitu külge? "))
length = int(input("Külje pikkus? "))
if sides < 3:
    print("Hulknurgal peab olema vähemalt 3 külge.")
else:
    t = turtle.Turtle()
    angle = 360 / sides
    i = 0
    while i < sides:
        t.forward(length)
        t.right(angle)
        i += 1
    turtle.done()
