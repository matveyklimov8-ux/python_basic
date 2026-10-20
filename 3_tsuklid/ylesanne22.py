population = 50000.0
years = 0
while population <= 60000:
    population *= 1.02
    years += 1
print("Aastaid kulus:", years)
print("Elanike arv:", round(population))
