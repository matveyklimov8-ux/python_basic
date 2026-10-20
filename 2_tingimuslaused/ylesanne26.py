month = int(input("Sisesta kuu (1–12): "))
day = int(input("Sisesta päev: "))
if month == 2:
    max_day = 28
elif month in (4, 6, 9, 11):
    max_day = 30
elif month in (1, 3, 5, 7, 8, 10, 12):
    max_day = 31
else:
    max_day = 0
if 1 <= day <= max_day:
    print("Kuupäev on korrektne.")
else:
    print("Sellist kuupäeva ei ole.")
