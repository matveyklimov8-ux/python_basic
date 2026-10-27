from pathlib import Path

faili_tee = Path(__file__).with_name("tervitus.txt")
with open(faili_tee, encoding="utf-8") as fail:
    for number, rida in enumerate(fail, start=1):
        print(f"{number}: {rida.strip()}")
