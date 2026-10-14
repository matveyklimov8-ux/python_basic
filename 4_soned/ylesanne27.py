import tkinter as tk
WIDTH = 600
HEIGHT = 400
BACKGROUND = "white"
aken = tk.Tk()
aken.title("Minu esimene graafika")
tahvel = tk.Canvas(aken, width=WIDTH, height=HEIGHT, bg=BACKGROUND)
tahvel.pack()
aken.mainloop()
