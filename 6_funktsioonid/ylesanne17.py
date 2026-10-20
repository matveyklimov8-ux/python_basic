# Ülesanne 17. Ringi pindala
import math

def ringi_pindala(raadius):
    return math.pi * raadius ** 2

for raadius in (1, 2.5, 5):
    print(f"Raadius {raadius}: pindala {ringi_pindala(raadius):.2f}")
