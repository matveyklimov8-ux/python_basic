# Ülesanne 20. Positiivsed ja negatiivsed arvud
arvud = [-12, 5, 0, 18, -7, 23, -3, 9]
positiivseid = negatiivseid = nulle = 0
positiivne_summa = 0
negatiivsed = []
for arv in arvud:
    if arv > 0:
        positiivseid += 1
        positiivne_summa += arv
    elif arv < 0:
        negatiivseid += 1
        negatiivsed.append(arv)
    else:
        nulle += 1
print("Positiivseid:", positiivseid)
print("Negatiivseid:", negatiivseid)
print("Nulle:", nulle)
print("Positiivsete summa:", positiivne_summa)
print("Negatiivsed arvud:", negatiivsed)
