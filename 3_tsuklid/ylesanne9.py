# Ülesanne 9. Arvude 1–5 summa
# Prognoos: summa lõpptulemus on 15 (1 + 2 + 3 + 4 + 5).
i = 1
summa = 0
while i <= 5:
    summa = summa + i  # summa muutub: 1, 3, 6, 10, 15.
    i = i + 1           # i muutub: 2, 3, 4, 5, 6.
# Kui i on 6, on tingimus i <= 5 väär; lõplik summa kuvatakse.
print(summa)
