import tkinter as tk
WIDTH = 600
HEIGHT = 300
STRIPE_HEIGHT = HEIGHT / 3
aken = tk.Tk()
aken.title("Eesti lipp")
tahvel = tk.Canvas(aken, width=WIDTH, height=HEIGHT, bg="white", highlightthickness=0)
tahvel.pack()
colors = ["#4891D9", "black", "white"]
for row, color in enumerate(colors):
    y1 = row * STRIPE_HEIGHT
    y2 = (row + 1) * STRIPE_HEIGHT
    tahvel.create_rectangle(0, y1, WIDTH, y2, fill=color, outline=color)
aken.mainloop()
