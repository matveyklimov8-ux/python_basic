from pathlib import Path
kaust = Path(__file__).resolve().parent
faili_tee = kaust / "hinded.txt"
def loe_andmed():
    nimed, hinded = [], []
    if faili_tee.exists():
        with open(faili_tee, encoding="utf-8") as fail:
            for rida in fail:
                osad = rida.strip().rsplit(maxsplit=1)
                if len(osad) == 2:
                    nimi, hinde_tekst = osad
                    try:
                        hinne = int(hinde_tekst)
                        if 1 <= hinne <= 5:
                            nimed.append(nimi)
                            hinded.append(hinne)
                    except ValueError:
                        pass
    return nimed, hinded
def salvesta_aruanne(nimed, hinded):
    read = [f"{i}. {nimi} – hinne {hinded[i-1]}" for i, nimi in enumerate(nimed, start=1)]
    if hinded:
        read += [f"Keskmine hinne: {sum(hinded)/len(hinded):.2f}"]
        read += [f"Hinne {h}: {hinded.count(h)}" for h in range(1, 6)]
    aruanne = "\n".join(read) + "\n"
    (kaust / "opilaste_hinnete_aruanne.txt").write_text(aruanne, encoding="utf-8")
    print("Aruanne salvestati faili opilaste_hinnete_aruanne.txt.")
while True:
    print("\n1. Kuva kõik õpilased\n2. Lisa uus õpilane ja hinne\n3. Otsi õpilast\n4. Kuva hinnete statistika\n5. Salvesta aruanne faili\n6. Lõpeta")
    valik = input("Vali tegevus: ").strip()
    nimed, hinded = loe_andmed()
    if valik == "1":
        if not nimed: print("Õpilasi pole.")
        for nimi, hinne in zip(nimed, hinded): print(f"{nimi}: {hinne}")
    elif valik == "2":
        nimi = input("Õpilase nimi: ").strip()
        try: hinne = int(input("Hinne (1–5): "))
        except ValueError:
            print("Hinne peab olema täisarv."); continue
        if not nimi or nimi.casefold() in [n.casefold() for n in nimed]:
            print("Nimi on tühi või selline õpilane on juba olemas.")
        elif not 1 <= hinne <= 5:
            print("Hinne peab olema 1–5.")
        else:
            with open(faili_tee, "a", encoding="utf-8") as fail: fail.write(f"{nimi} {hinne}\n")
            print("Õpilane lisatud.")
    elif valik == "3":
        otsitav = input("Otsitav nimi: ").strip().casefold()
        vaste = next(((n, h) for n, h in zip(nimed, hinded) if n.casefold() == otsitav), None)
        print(f"{vaste[0]}: hinne {vaste[1]}" if vaste else "Õpilast ei leitud.")
    elif valik == "4":
        if not hinded: print("Õpilasi pole, statistikat ei saa arvutada.")
        else:
            print(f"Keskmine hinne: {sum(hinded)/len(hinded):.2f}")
            for h in range(1, 6): print(f"Hinne {h}: {hinded.count(h)}")
    elif valik == "5": salvesta_aruanne(nimed, hinded)
    elif valik == "6": break
    else: print("Vigane menüüvalik.")
