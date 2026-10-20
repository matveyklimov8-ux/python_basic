# Ülesanne 43. Lumememm
import tkinter as tk

def joonista_silmad(canvas, x, y, suurus):
    for dx in (-suurus * 0.12, suurus * 0.12):
        canvas.create_oval(x + dx - 3, y - 3, x + dx + 3, y + 3, fill="black")

def joonista_nina(canvas, x, y, suurus):
    canvas.create_polygon(x, y, x + suurus * 0.22, y + suurus * 0.04,
                          x, y + suurus * 0.09, fill="orange", outline="orange")

def joonista_noobid(canvas, x, y, suurus):
    for i in range(3):
        cy = y + suurus * (0.25 + i * 0.13)
        canvas.create_oval(x - 3, cy - 3, x + 3, cy + 3, fill="black")

def joonista_lumememm(canvas, x, y, suurus):
    # x,y on alumise ringi keskpunkt; suurus on alumise ringi läbimõõt.
    d1, d2, d3 = suurus, suurus * 0.72, suurus * 0.52
    canvas.create_oval(x-d1/2, y-d1/2, x+d1/2, y+d1/2, fill="white", outline="gray")
    y2 = y - d1/2 - d2/2 + 2
    canvas.create_oval(x-d2/2, y2-d2/2, x+d2/2, y2+d2/2, fill="white", outline="gray")
    y3 = y2 - d2/2 - d3/2 + 2
    canvas.create_oval(x-d3/2, y3-d3/2, x+d3/2, y3+d3/2, fill="white", outline="gray")
    joonista_silmad(canvas, x, y3, d3)
    joonista_nina(canvas, x, y3 + d3 * 0.06, d3)
    joonista_noobid(canvas, x, y2, d2)

aken = tk.Tk()
aken.title("Lumememmed")
tahvel = tk.Canvas(aken, width=600, height=350, bg="lightblue")
tahvel.pack()
joonista_lumememm(tahvel, 180, 275, 130)
joonista_lumememm(tahvel, 420, 290, 90)
aken.mainloop()
