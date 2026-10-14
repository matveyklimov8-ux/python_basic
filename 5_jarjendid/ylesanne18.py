# Ülesanne 18. Paaris- ja paaritute arvude loendamine
arvud = [7, 12, 19, 24, 31, 46, 53, 60, 72]
paaris_arv = paaritu_arv = 0
paaris_summa = paaritu_summa = 0
for arv in arvud:
    if arv % 2 == 0:
        paaris_arv += 1
        paaris_summa += arv
    else:
        paaritu_arv += 1
        paaritu_summa += arv
print("Paarisarve:", paaris_arv)
print("Paarituid:", paaritu_arv)
print("Paarisarvude summa:", paaris_summa)
print("Paaritute summa:", paaritu_summa)
