# Ülesanne 45. Linnasiluett
import tkinter as tk

def joonista_hoone(canvas, x, y, laius, korgus, varv):
    canvas.create_rectangle(x, y-korgus, x+laius, y, fill=varv, outline=varv)

def joonista_aken(canvas, x, y, suurus, varv):
    canvas.create_rectangle(x, y, x+suurus, y+suurus, fill=varv, outline=varv)

def joonista_kuu(canvas, x, y, raadius):
    canvas.create_oval(x-raadius, y-raadius, x+raadius, y+raadius,
                       fill="lightyellow", outline="lightyellow")

def joonista_linn(canvas):
    canvas.create_rectangle(0, 0, 700, 400, fill="midnightblue", outline="midnightblue")
    joonista_kuu(canvas, 590, 65, 30)
    alused = [100, 145, 85, 175, 125]
    laius = 95
    for i, korgus in enumerate(alused):
        x = 10 + i * 138
        y = 365
        joonista_hoone(canvas, x, y, laius, korgus, ["#29334f", "#35405e", "#222b45"][i % 3])
        for aken_rida in range(max(1, korgus // 32)):
            for aken_veerg in range(3):
                ax = x + 12 + aken_veerg * 27
                ay = y - korgus + 12 + aken_rida * 25
                joonista_aken(canvas, ax, ay, 10, "gold" if (i+aken_rida+aken_veerg) % 3 else "lightblue")

aken = tk.Tk()
aken.title("Öine linn")
tahvel = tk.Canvas(aken, width=700, height=400, highlightthickness=0)
tahvel.pack()
joonista_linn(tahvel)
aken.mainloop()
