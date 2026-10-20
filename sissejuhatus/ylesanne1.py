# Iga väärtuse andmetüüp: int, float või str.
values = [25, "25", 25.0, "25.0", -10, "Python", 0, 0.0]
for value in values:
    print(repr(value), "->", type(value).__name__)
