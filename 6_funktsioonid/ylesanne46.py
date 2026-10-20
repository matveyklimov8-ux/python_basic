# Ülesanne 46. Taskukalkulaator

def liida(a, b): return a + b
def lahuta(a, b): return a - b
def korruta(a, b): return a * b
def jaga(a, b):
    if b == 0:
        return None
    return a / b

def kuva_menuu():
    print("\nKALKULAATOR")
    print("1. Liida  2. Lahuta  3. Korruta  4. Jaga  0. Välju")

while True:
    kuva_menuu()
    valik = input("Vali tehe: ").strip()
    if valik == "0":
        print("Head aega!")
        break
    if valik not in ("1", "2", "3", "4"):
        print("Tundmatu valik.")
        continue
    try:
        a = float(input("Esimene arv: "))
        b = float(input("Teine arv: "))
    except ValueError:
        print("Palun sisesta arvud.")
        continue
    tehted = {"1": liida, "2": lahuta, "3": korruta, "4": jaga}
    tulemus = tehted[valik](a, b)
    if tulemus is None:
        print("Nulliga jagada ei saa.")
    else:
        print("Tulemus:", tulemus)
