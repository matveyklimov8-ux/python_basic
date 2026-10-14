import tkinter as tk
aken = tk.Tk()
aken.title("Värvilised ruudud")
side = 40
spacing = 10
count = 10
width = count * side + (count - 1) * spacing + 20
tahvel = tk.Canvas(aken, width=width, height=80, bg="white")
tahvel.pack()
for i in range(count):
    x1 = 10 + i * (side + spacing)
    color = "red" if i % 2 == 0 else "blue"
    tahvel.create_rectangle(x1, 20, x1 + side, 20 + side, fill=color, outline="black")
aken.mainloop()
