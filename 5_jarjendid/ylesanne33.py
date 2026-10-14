# Ülesanne 33. Õpilaste hinnete analüüs
hinded = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]
print("Hinnete koguarv:", len(hinded))
print(f"Keskmine hinne: {sum(hinded) / len(hinded):.2f}")
sagedused = {hinne: hinded.count(hinne) for hinne in range(1, 6)}
suurim_sagedus = max(sagedused.values())
sagedasemad = [hinne for hinne, kogus in sagedused.items() if kogus == suurim_sagedus]
print("Kõige sagedasem hinne:", ", ".join(map(str, sagedasemad)))
print("Positiivseid hindeid (3–5):", sum(1 for hinne in hinded if hinne >= 3))
print("Mitterahuldavaid hindeid (1–2):", sum(1 for hinne in hinded if hinne <= 2))
for hinne in range(1, 6):
    print(f"Hinne {hinne}: {'*' * sagedused[hinne]}")
