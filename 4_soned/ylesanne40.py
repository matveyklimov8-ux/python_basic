import tkinter as tk
word = input("Sisesta sõna: ")
vowels = "aeiouõäöüAEIOUÕÄÖÜ"
cell_width = max(35, min(70, 760 // max(1, len(word))))
canvas_width = max(600, len(word) * cell_width + 20)
aken = tk.Tk()
aken.title("Tekstist loodud graafiline muster")
frame = tk.Frame(aken)
frame.pack(fill="both", expand=True)
scrollbar = tk.Scrollbar(frame, orient="horizontal")
scrollbar.pack(side="bottom", fill="x")
tahvel = tk.Canvas(frame, width=800, height=220, bg="white", xscrollcommand=scrollbar.set,
                   scrollregion=(0, 0, canvas_width, 220))
tahvel.pack(side="top", fill="both", expand=True)
scrollbar.config(command=tahvel.xview)
for i, character in enumerate(word):
    center_x = 20 + i * cell_width + cell_width // 2
    if character in vowels:
        radius = min(20, cell_width // 3)
        tahvel.create_oval(center_x - radius, 45, center_x + radius, 45 + radius * 2,
                           fill="#77b5d9", outline="#245b78")
    elif character.isalpha():
        box = min(42, cell_width - 6)
        tahvel.create_rectangle(center_x - box // 2, 45, center_x + box // 2, 45 + box,
                                fill="#f2b880", outline="#8b572a")
    else:
        tahvel.create_line(center_x - 14, 65, center_x + 14, 95, fill="#7b2cbf", width=4)
        tahvel.create_line(center_x - 14, 95, center_x + 14, 65, fill="#7b2cbf", width=4)
    tahvel.create_text(center_x, 130, text=character, font=("Arial", 16, "bold"))
aken.mainloop()
