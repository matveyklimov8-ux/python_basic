import tkinter as tk
SIZE = 500
STEP = 50
aken = tk.Tk()
aken.title("Koordinaatvõrgustik")
tahvel = tk.Canvas(aken, width=SIZE, height=SIZE, bg="white")
tahvel.pack()
for coordinate in range(0, SIZE + 1, STEP):
    tahvel.create_line(coordinate, 0, coordinate, SIZE, fill="gray")
    tahvel.create_line(0, coordinate, SIZE, coordinate, fill="gray")
    tahvel.create_text(coordinate + 3, 10, text=str(coordinate), anchor="nw", fill="black")
    tahvel.create_text(3, coordinate + 2, text=str(coordinate), anchor="nw", fill="black")
aken.mainloop()
