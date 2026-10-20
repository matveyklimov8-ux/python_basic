# Ülesanne 49. Paroolide kontrollija

def piisav_pikkus(parool):
    return len(parool) >= 8

def sisaldab_suurtahte(parool):
    return any(taht.isupper() for taht in parool)

def sisaldab_vaiketahte(parool):
    return any(taht.islower() for taht in parool)

def sisaldab_numbrit(parool):
    return any(taht.isdigit() for taht in parool)

def sisaldab_erimarki(parool):
    return any(not taht.isalnum() for taht in parool)

def kontrolli_parool(parool):
    kontrollid = [
        (piisav_pikkus(parool), "Vähemalt 8 tähemärki"),
        (sisaldab_suurtahte(parool), "Vähemalt üks suurtäht"),
        (sisaldab_vaiketahte(parool), "Vähemalt üks väiketäht"),
        (sisaldab_numbrit(parool), "Vähemalt üks number"),
        (sisaldab_erimarki(parool), "Vähemalt üks erimärk"),
    ]
    punktid = sum(1 for sobib, _ in kontrollid if sobib)
    puuduvad = [kirjeldus for sobib, kirjeldus in kontrollid if not sobib]
    return punktid, puuduvad

parool = input("Sisesta parool: ")
punktid, puuduvad = kontrolli_parool(parool)
print(f"Tulemus: {punktid}/5")
if puuduvad:
    print("Täitmata nõuded:")
    for tingimus in puuduvad:
        print("-", tingimus)
else:
    print("Kõik nõuded täidetud.")
