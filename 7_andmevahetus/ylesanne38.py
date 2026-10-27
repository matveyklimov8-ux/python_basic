from pathlib import Path
import tkinter as tk
kaust = Path(__file__).resolve().parent
joonistusfail = kaust / "joonistus.txt"
aken = tk.Tk()
aken.title("Failipõhine joonistusprogramm")
tahvel = tk.Canvas(aken, width=500, height=400, bg="white")
tahvel.pack()
vead = []
with open(joonistusfail, encoding="utf-8") as fail:
    for nr, rida in enumerate(fail, start=1):
        osad = rida.split()
        if not osad:
            continue
        try:
            kask = osad[0].upper()
            if kask == "RECT" and len(osad) == 6:
                x1, y1, x2, y2 = map(float, osad[1:5]); tahvel.create_rectangle(x1, y1, x2, y2, fill=osad[5])
            elif kask == "OVAL" and len(osad) == 6:
                x1, y1, x2, y2 = map(float, osad[1:5]); tahvel.create_oval(x1, y1, x2, y2, fill=osad[5])
            elif kask == "LINE" and len(osad) == 6:
                x1, y1, x2, y2 = map(float, osad[1:5]); tahvel.create_line(x1, y1, x2, y2, fill=osad[5], width=3)
            else:
                raise ValueError("Tundmatu käsk või vale argumentide arv")
        except (ValueError, tk.TclError) as viga:
            vead.append(f"Rida {nr}: {viga}")
if vead:
    print("Joonistusfailis leiti probleemid:")
    for viga in vead: print(viga)
aken.mainloop()
