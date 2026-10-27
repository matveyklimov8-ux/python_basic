from pathlib import Path
kaust = Path(__file__).resolve().parent
faili_tee = kaust / "kontaktid.txt"
while True:
    otsitav = input("Otsi kontakti nime järgi (lõpetamiseks STOP): ").strip()
    if otsitav.casefold() == "stop":
        break
    leitud = False
    with open(faili_tee, encoding="utf-8") as fail:
        for rida in fail:
            osad = rida.strip().split(";")
            if len(osad) == 3 and osad[0].casefold() == otsitav.casefold():
                print("Nimi:", osad[0])
                print("E-post:", osad[1])
                print("Telefon:", osad[2])
                leitud = True
                break
    if not leitud:
        print("Kontakti ei leitud.")
