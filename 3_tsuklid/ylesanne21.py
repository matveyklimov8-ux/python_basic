balance = 1000.0
years = 0
while balance < 2000:
    balance *= 1.05
    years += 1
print("Aastaid kulus:", years)
print(f"Kontol on: {balance:.2f} eurot")
