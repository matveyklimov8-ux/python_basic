# Ülesanne 18. Mõlemad funktsioonid tagastavad väärtuse.

def arvuta1(a, b):
    return a + b


def arvuta2(a, b):
    return a * b

# Mõlema funktsiooni tagastatud väärtust saab kasutada uues arvutuses.
x = arvuta1(5, 3)
y = arvuta2(5, 3)
print("Liitmise tulemus:", x)
print("Korrutamise tulemus:", y)
print("Uus arvutus (liitmise tulemus × 2):", x * 2)
print("Uus arvutus (korrutamise tulemus + 10):", y + 10)
