import tkinter as tk
aken = tk.Tk()
aken.title("Liiklusfoor")
tahvel = tk.Canvas(aken, width=260, height=440, bg="white")
tahvel.pack()
tahvel.create_rectangle(70, 20, 190, 390, fill="#333333", outline="#111111", width=3)
colors = ["red", "yellow", "green"]
center_x = 130
radius = 38
first_center_y = 85
spacing = 115
for i, color in enumerate(colors):
    center_y = first_center_y + i * spacing
    tahvel.create_oval(center_x - radius, center_y - radius,
                       center_x + radius, center_y + radius,
                       fill=color, outline="black")
aken.mainloop()
