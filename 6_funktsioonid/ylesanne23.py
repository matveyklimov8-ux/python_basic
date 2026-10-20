# Ülesanne 23. Hinde määramine

def hinne(punktid):
    if punktid < 0 or punktid > 100:
        return None
    elif punktid >= 90:
        return 5
    elif punktid >= 75:
        return 4
    elif punktid >= 50:
        return 3
    elif punktid >= 20:
        return 2
    else:
        return 1

for punktid in (105, 94, 82, 60, 30, 12, -1):
    print(punktid, "->", hinne(punktid))
