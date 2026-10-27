from pathlib import Path
faili_tee = Path(__file__).with_name("ostunimekiri.txt")
with open(faili_tee, "a", encoding="utf-8") as fail:
    while True:
        toode = input("Lisa toode (lõpetamiseks STOP): ").strip()
        if toode.upper() == "STOP":
            break
        if toode:
            fail.write(toode + "\n")
print("Uued tooted lisati faili lõppu.")
