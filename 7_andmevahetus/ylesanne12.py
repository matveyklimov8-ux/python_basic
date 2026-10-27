from pathlib import Path
faili_tee = Path(__file__).with_name("hinded.txt")
with open(faili_tee, encoding="utf-8") as fail:
    opilased = [(osad[0], int(osad[1])) for r in fail if (osad := r.split()) and len(osad) >= 2]
hinded = [hinne for _, hinne in opilased]
if hinded:
    print(f"Keskmine hinne: {sum(hinded) / len(hinded):.2f}")
    print("Kõrgeim hinne:", max(hinded))
    print("Madalaim hinne:", min(hinded))
    print("\nÕpilased hindega vähemalt 4:")
    for nimi, hinne in opilased:
        if hinne >= 4:
            print(nimi)
