from pathlib import Path
from datetime import date
faili_tee = Path(__file__).with_name("paevik.txt")
while True:
    print("\n1. Lisa päevikusse sissekanne")
    print("2. Vaata kõiki sissekandeid")
    print("3. Lõpeta")
    valik = input("Vali tegevus: ").strip()
    if valik == "1":
        kuupaev = input("Kuupäev (nt 20.10.2026): ").strip() or date.today().strftime("%d.%m.%Y")
        sissekanne = input("Sissekanne: ").strip()
        with open(faili_tee, "a", encoding="utf-8") as fail:
            fail.write(f"{kuupaev}; {sissekanne}\n")
        print("Sissekanne salvestatud.")
    elif valik == "2":
        try:
            with open(faili_tee, encoding="utf-8") as fail:
                print(fail.read(), end="")
        except FileNotFoundError:
            print("Päevik on veel tühi.")
    elif valik == "3":
        print("Head aega!")
        break
    else:
        print("Tundmatu valik.")
