from pathlib import Path
faili_tee = Path(__file__).with_name("nimed.txt")
with open(faili_tee, encoding="utf-8") as fail:
    nimede_arv = sum(1 for rida in fail if rida.strip())
print(f"Failis on {nimede_arv} nime.")
