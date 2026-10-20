balance = 1000.0
year = 1
while year <= 10:
    balance *= 1.05
    print(f"{year}. aasta: {balance:.2f} eurot")
    year += 1
