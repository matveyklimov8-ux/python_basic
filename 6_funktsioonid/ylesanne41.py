# Ülesanne 41. Värvilised ringid
import tkinter as tk

def joonista_ring(canvas, x, y, raadius, varv):
    canvas.create_oval(x - raadius, y - raadius, x + raadius, y + raadius,
                       fill=varv, outline="black")

aken = tk.Tk()
aken.title("Värvilised ringid")
tahvel = tk.Canvas(aken, width=600, height=300, bg="white")
tahvel.pack()
varvid = ["red", "blue", "green", "orange", "purple"]
for i in range(10):
    joonista_ring(tahvel, 35 + i * 58, 100 + (i % 2) * 55, 15 + i % 4 * 3, varvid[i % len(varvid)])
aken.mainloop()
