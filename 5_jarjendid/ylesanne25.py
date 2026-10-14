# Ülesanne 25. Korduvate väärtuste eemaldamine
arvud = [4, 7, 4, 9, 2, 7, 5, 9, 1, 2]
unikaalsed = []
for arv in arvud:
    if arv not in unikaalsed:
        unikaalsed.append(arv)
print("Ilma kordusteta:", unikaalsed)
