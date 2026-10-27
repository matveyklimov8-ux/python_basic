from pathlib import Path

faili_tee = Path(__file__).with_name("tervitus.txt")
with open(faili_tee, "r", encoding="utf-8") as fail:
    sisu = fail.read()
print(sisu, end="")
