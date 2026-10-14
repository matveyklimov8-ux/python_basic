import tkinter as tk
aken = tk.Tk()
aken.title("Malelaud")
cell = 50
size = 8 * cell
tahvel = tk.Canvas(aken, width=size, height=size)
tahvel.pack()
for row in range(8):
    for column in range(8):
        color = "white" if (row + column) % 2 == 0 else "black"
        x1, y1 = column * cell, row * cell
        tahvel.create_rectangle(x1, y1, x1 + cell, y1 + cell, fill=color, outline="gray")
aken.mainloop()
