try:
    faili_nimi = input("Sisesta failinimi: ").strip()
    with open(faili_nimi, encoding="utf-8") as fail:
        print(fail.read(), end="")
except FileNotFoundError:
    print("Viga: sellist faili ei leitud.")
except OSError as viga:
    print("Faili avamine ebaõnnestus:", viga)
