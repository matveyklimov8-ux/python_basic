import tkinter as tk
aken = tk.Tk()
aken.title("Päikeseloojang")
tahvel = tk.Canvas(aken, width=700, height=420, bg="#f4a261")
tahvel.pack()
tahvel.create_rectangle(0, 0, 700, 260, fill="#f4a261", outline="#f4a261")
tahvel.create_oval(285, 125, 415, 255, fill="#ffd166", outline="#ffd166")
tahvel.create_rectangle(0, 250, 700, 420, fill="#3d405b", outline="#3d405b")
tahvel.create_polygon(0, 330, 150, 240, 280, 340, 430, 260, 590, 340, 700, 285,
                     700, 420, 0, 420, fill="#6d597a", outline="#6d597a")
# Korduvad linnud taevas.
for x in range(80, 600, 100):
    y = 70 + (x // 100 % 2) * 25
    tahvel.create_arc(x, y, x + 25, y + 15, start=0, extent=180, style="arc", width=2)
    tahvel.create_arc(x + 25, y, x + 50, y + 15, start=0, extent=180, style="arc", width=2)
aken.mainloop()
