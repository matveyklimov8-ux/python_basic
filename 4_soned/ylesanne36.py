import tkinter as tk
CIRCLE_COUNT = 25
aken = tk.Tk()
aken.title("Geomeetriline muster")
tahvel = tk.Canvas(aken, width=600, height=400, bg="white")
tahvel.pack()
colors = ["#4b8bbe", "#e07a5f", "#81b29a"]
for i in range(CIRCLE_COUNT):
    column = i % 5
    row = i // 5
    radius = 12 + (i % 4) * 3
    center_x = 65 + column * 115
    center_y = 45 + row * 75
    tahvel.create_oval(center_x - radius, center_y - radius,
                       center_x + radius, center_y + radius,
                       fill=colors[i % len(colors)], outline="black")
aken.mainloop()
