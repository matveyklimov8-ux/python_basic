# Ülesanne 42. Maja joonistamine funktsioonidega
import tkinter as tk

def joonista_sein(canvas, x, y, suurus, varv="wheat"):
    canvas.create_rectangle(x, y, x + suurus, y + suurus * 0.65, fill=varv, outline="black")
    canvas.create_rectangle(x + suurus * 0.42, y + suurus * 0.35,
                            x + suurus * 0.60, y + suurus * 0.65, fill="saddlebrown")

def joonista_katus(canvas, x, y, suurus, varv="firebrick"):
    canvas.create_polygon(x - suurus * 0.08, y, x + suurus / 2, y - suurus * 0.4,
                          x + suurus * 1.08, y, fill=varv, outline="black")

def joonista_aken(canvas, x, y, suurus):
    canvas.create_rectangle(x, y, x + suurus * 0.18, y + suurus * 0.18,
                            fill="lightblue", outline="black")

def joonista_maja(canvas, x, y, suurus, seinavarv="wheat", katusevarv="firebrick"):
    joonista_sein(canvas, x, y, suurus, seinavarv)
    joonista_katus(canvas, x, y, suurus, katusevarv)
    joonista_aken(canvas, x + suurus * 0.12, y + suurus * 0.18, suurus)
    joonista_aken(canvas, x + suurus * 0.70, y + suurus * 0.18, suurus)

aken = tk.Tk()
aken.title("Kolm maja")
tahvel = tk.Canvas(aken, width=700, height=350, bg="skyblue")
tahvel.pack()
tahvel.create_rectangle(0, 260, 700, 350, fill="lightgreen", outline="lightgreen")
joonista_maja(tahvel, 40, 150, 130)
joonista_maja(tahvel, 250, 125, 155, "lightyellow", "darkgreen")
joonista_maja(tahvel, 500, 175, 100, "pink", "slateblue")
aken.mainloop()
