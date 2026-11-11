# Ülesanne 36. Geomeetriline muster: ringide arv arvestab lõuendi piire.
import tkinter as tk

CIRCLE_COUNT = 25
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
SPACING = 75
MARGIN = 30
MAX_RADIUS = 21

# Arvutame, mitu ringi mahub ühte ritta ja mitu rida on võimalik joonistada.
# Seega saab CIRCLE_COUNT väärtust muuta, ilma et ringid läheksid lõuendist välja.
columns = (CANVAS_WIDTH - 2 * (MARGIN + MAX_RADIUS)) // SPACING + 1
rows = (CANVAS_HEIGHT - 2 * (MARGIN + MAX_RADIUS)) // SPACING + 1
capacity = columns * rows
if not 0 <= CIRCLE_COUNT <= capacity:
    raise ValueError(f"Ringide arv peab olema vahemikus 0 kuni {capacity}.")

aken = tk.Tk()
aken.title("Geomeetriline muster")
tahvel = tk.Canvas(aken, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
tahvel.pack()
colors = ["#4b8bbe", "#e07a5f", "#81b29a"]

for i in range(CIRCLE_COUNT):
    column = i % columns
    row = i // columns
    radius = 12 + (i % 4) * 3
    center_x = MARGIN + MAX_RADIUS + column * SPACING
    center_y = MARGIN + MAX_RADIUS + row * SPACING
    tahvel.create_oval(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        fill=colors[i % len(colors)], outline="black"
    )

aken.mainloop()
