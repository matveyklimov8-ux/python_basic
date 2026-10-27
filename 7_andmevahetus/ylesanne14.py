from pathlib import Path
faili_tee = Path(__file__).with_name("tekst.txt")
with open(faili_tee, encoding="utf-8") as fail:
    read = [rida.rstrip("\n\r") for rida in fail]
sonade_arv = sum(len(rida.split()) for rida in read)
maerkide_arv = sum(len(rida) for rida in read)
mittetyhjad = [rida for rida in read if rida.strip()]
print("Ridu:", len(read))
print("Sõnu:", sonade_arv)
print("Tähemärke koos tühikutega:", maerkide_arv)
print("Mittetühje ridu:", len(mittetyhjad))
print("Keskmine sõnade arv rea kohta:", f"{sonade_arv / len(read):.2f}" if read else "0.00")
