from pathlib import Path
kaust = Path(__file__).resolve().parent
faili_tee = kaust / "kulud.txt"
def loe_kulud():
    kulud = []
    if faili_tee.exists():
        with open(faili_tee, encoding="utf-8") as fail:
            for rida in fail:
                osad = rida.rstrip("\n").split(";")
                if len(osad) == 4:
                    try: kulud.append((osad[0], osad[1], osad[2], float(osad[3])))
                    except ValueError: continue
    return kulud
while True:
    print("\n1. Lisa uus kulu\n2. Kuva kõik kulud\n3. Arvuta kogukulu\n4. Kuva kategooria kulud\n5. Salvesta kokkuvõte\n0. Lõpeta")
    valik = input("Valik: ").strip()
    kulud = loe_kulud()
    if valik == "1":
        kuupaev = input("Kuupäev: ").strip(); kategooria = input("Kategooria: ").strip(); kirjeldus = input("Kirjeldus: ").strip()
        try: summa = float(input("Summa (€): ").replace(",", "."))
        except ValueError: print("Summa peab olema arv."); continue
        if summa < 0 or any(";" in x for x in (kuupaev, kategooria, kirjeldus)):
            print("Summa ei tohi olla negatiivne ja tekst ei tohi sisaldada semikoolonit."); continue
        with open(faili_tee, "a", encoding="utf-8") as fail: fail.write(f"{kuupaev};{kategooria};{kirjeldus};{summa:.2f}\n")
        print("Kulu salvestatud.")
    elif valik == "2":
        for k in kulud: print(f"{k[0]} | {k[1]} | {k[2]} | {k[3]:.2f} €")
        if not kulud: print("Kulusid pole.")
    elif valik == "3": print(f"Kogukulu: {sum(k[3] for k in kulud):.2f} €")
    elif valik == "4":
        kat = input("Kategooria: ").strip().casefold()
        vasted = [k for k in kulud if k[1].casefold() == kat]
        for k in vasted: print(f"{k[0]} | {k[2]} | {k[3]:.2f} €")
        print(f"Kategooria kogukulu: {sum(k[3] for k in vasted):.2f} €")
    elif valik == "5":
        rida = f"Kulusid: {len(kulud)}\nKogukulu: {sum(k[3] for k in kulud):.2f} €\n"
        (kaust / "kulude_kokkuvote.txt").write_text(rida, encoding="utf-8"); print(rida, end="")
    elif valik == "0": break
    else: print("Tundmatu valik.")
