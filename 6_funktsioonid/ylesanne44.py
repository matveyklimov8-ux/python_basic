# Ülesanne 44. Tähtede muster
import tkinter as tk
import math

def joonista_taht(canvas, x, y, suurus, varv):
    tipud = []
    for i in range(10):
        nurk = -math.pi / 2 + i * math.pi / 5
        raadius = suurus if i % 2 == 0 else suurus * 0.42
        tipud.extend([x + math.cos(nurk) * raadius, y + math.sin(nurk) * raadius])
    canvas.create_polygon(tipud, fill=varv, outline="white")

aken = tk.Tk()
aken.title("Tähistaevas")
tahvel = tk.Canvas(aken, width=650, height=400, bg="midnightblue")
tahvel.pack()
varvid = ["white", "yellow", "lightblue", "gold"]
for i in range(24):
    x = 20 + (i * 79) % 610
    y = 20 + (i * 53) % 350
    suurus = 5 + i % 4 * 2
    joonista_taht(tahvel, x, y, suurus, varvid[i % len(varvid)])
aken.mainloop()
