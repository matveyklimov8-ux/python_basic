# Ülesanne 26. Arvude summa vahemikus 1 kuni n

def arvude_summa(n):
    summa = 0
    for arv in range(1, n + 1):
        summa += arv
    return summa

print(arvude_summa(5))  # 15
