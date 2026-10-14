# Ülesanne 5. Elemendi olemasolu kontroll
kasutajad = ["mari", "juhan", "kati", "peeter", "anna"]
nimi = input("Sisesta kasutajanimi: ").strip().lower()

if nimi in kasutajad:
    print("Kasutaja on registreeritud.")
else:
    print("Kasutajat ei leitud.")
