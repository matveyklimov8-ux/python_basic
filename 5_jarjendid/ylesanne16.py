# Ülesanne 16. Korrutustabel
arv = int(input("Sisesta arv vahemikus 1–10: "))
if 1 <= arv <= 10:
    for kordaja in range(1, 11):
        print(f"{arv} × {kordaja} = {arv * kordaja}")
else:
    print("Palun sisesta arv vahemikus 1–10.")
