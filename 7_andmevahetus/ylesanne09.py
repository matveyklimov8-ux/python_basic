from pathlib import Path
faili_tee = Path(__file__).with_name("arvud.txt")
with open(faili_tee, encoding="utf-8") as fail:
    arvud = [int(r.strip()) for r in fail if r.strip()]
if arvud:
    suurim, vaikseim = max(arvud), min(arvud)
    print("Suurim arv:", suurim)
    print("Väikseim arv:", vaikseim)
    print("Vahe:", suurim - vaikseim)
else:
    print("Failis pole arve.")
