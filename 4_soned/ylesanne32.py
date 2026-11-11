# Ülesanne 32. Koordinaatvõrgustik
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

    # Äärmiste väärtuste korral nihutame teksti sissepoole, et see ei jääks
    # Canvas'e nähtavast alast välja. Teised sildid jäävad joone kõrvale.
    x_anchor = "ne" if coordinate == SIZE else "nw"
    x_position = SIZE - 4 if coordinate == SIZE else coordinate + 4
    tahvel.create_text(x_position, 4, text=str(coordinate), anchor=x_anchor, fill="black")

    y_anchor = "se" if coordinate == SIZE else "nw"
    y_position = SIZE - 4 if coordinate == SIZE else coordinate + 4
    tahvel.create_text(4, y_position, text=str(coordinate), anchor=y_anchor, fill="black")

aken.mainloop()
