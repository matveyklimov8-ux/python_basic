import tkinter as tk
first = input("Eesnimi: ").strip()
last = input("Perekonnanimi: ").strip()
group = input("Õpperühm: ").strip()
favorite = input("Lemmikvärv (nt blue, green, pink, purple): ").strip().lower()
allowed_colors = {"blue", "green", "pink", "purple", "red", "yellow", "orange", "white", "black", "cyan"}
if favorite not in allowed_colors:
    favorite = "lightblue"
full_name = f"{first} {last}".strip()
font_size = 30 if len(full_name) <= 18 else 22
aken = tk.Tk()
aken.title("Graafiline nimekaart")
tahvel = tk.Canvas(aken, width=500, height=300, bg=favorite, highlightthickness=0)
tahvel.pack()
tahvel.create_oval(25, 25, 90, 90, fill="white", outline="white")
tahvel.create_rectangle(410, 210, 475, 275, fill="#333333", outline="#333333")
tahvel.create_text(250, 110, text=full_name, font=("Arial", font_size, "bold"), fill="white")
tahvel.create_text(250, 165, text=group, font=("Arial", 18), fill="white")
tahvel.create_text(250, 235, text="MINU NIMEKAART", font=("Arial", 12, "bold"), fill="white")
aken.mainloop()
