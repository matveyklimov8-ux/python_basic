import turtle

kulgi = int(input("Mitu külge? "))
pikkus = int(input("Külje pikkus? "))

if kulgi < 3 or pikkus <= 0:
    print("Külgede arv peab olema vähemalt 3 ja pikkus positiivne.")
else:
    nurk = 360 / kulgi
    i = 0
    while i < kulgi:
        turtle.forward(pikkus)
        turtle.right(nurk)
        i = i + 1
    turtle.done()
