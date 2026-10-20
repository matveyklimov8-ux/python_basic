# Ülesanne 40. Ruutude joonistamine
import tkinter as tk

def joonista_ruut(canvas, x, y, suurus, varv):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill=varv, outline="black")

aken = tk.Tk()
aken.title("Värvilised ruudud")
tahvel = tk.Canvas(aken, width=500, height=300, bg="white")
tahvel.pack()
ruudud = [(20, 20, 50, "red"), (100, 30, 70, "blue"), (210, 20, 90, "green"), (330, 40, 55, "orange"), (400, 150, 40, "purple")]
for x, y, suurus, varv in ruudud:
    joonista_ruut(tahvel, x, y, suurus, varv)
aken.mainloop()
