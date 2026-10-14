import tkinter as tk
aken = tk.Tk()
aken.title("Linnasiluett")
W, H = 800, 500
tahvel = tk.Canvas(aken, width=W, height=H, bg="#10172a")
tahvel.pack()
tahvel.create_oval(650, 35, 720, 105, fill="#f6f0c6", outline="#f6f0c6")
buildings = [(20, 270, 110, 480), (125, 210, 230, 480), (245, 300, 340, 480),
             (355, 170, 465, 480), (480, 245, 590, 480), (605, 300, 710, 480), (725, 225, 790, 480)]
for x1, y1, x2, y2 in buildings:
    tahvel.create_rectangle(x1, y1, x2, y2, fill="#29364f", outline="#71809a")
    y = y1 + 18
    while y + 10 < y2 - 12:
        x = x1 + 12
        while x + 8 < x2 - 8:
            tahvel.create_rectangle(x, y, x + 8, y + 10, fill="#f4d06f", outline="#f4d06f")
            x += 22
        y += 25
# Ühele hoonele uks.
tahvel.create_rectangle(390, 420, 430, 480, fill="#70513a", outline="#bd9b70")
aken.mainloop()
