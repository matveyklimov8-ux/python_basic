# Sulgudega avaldised näitavad, milline tehe tehakse esimesena.
expressions = [
    ("2 + 4 * 3", 2 + 4 * 3),
    ("(2 + 4) * 3", (2 + 4) * 3),
    ("10 - 6 / 2", 10 - 6 / 2),
    ("10 - 6 // 2", 10 - 6 // 2),
    ("2 ** 3 + 1", 2 ** 3 + 1),
    ("2 * 3 ** 2", 2 * 3 ** 2),
]
for expression, result in expressions:
    print(f"{expression} = {result}")
