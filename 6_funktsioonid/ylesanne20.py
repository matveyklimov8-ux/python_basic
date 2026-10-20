# Ülesanne 20. Positiivne, negatiivne või null

def arvu_tyyp(arv):
    if arv > 0:
        return "Positiivne"
    elif arv < 0:
        return "Negatiivne"
    else:
        return "Null"

for arv in (5, -2, 0):
    print(arvu_tyyp(arv))
