# Ülesanne 30. Positiivsete arvude filtreerimine

def positiivsed(arvud):
    tulemus = []
    for arv in arvud:
        if arv > 0:
            tulemus.append(arv)
    return tulemus

print(positiivsed([-4, 5, 0, 12, -2, 7]))
