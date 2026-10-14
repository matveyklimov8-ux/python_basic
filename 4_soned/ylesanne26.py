while True:
    message = input("Sina: ").strip().lower()
    if message == "head aega":
        print("PyBot: Nägemist!")
        break
    elif "tere" in message:
        print("PyBot: Tere! Kuidas saan aidata?")
    elif "nimi" in message:
        print("PyBot: Minu nimi on PyBot.")
    elif "python" in message:
        print("PyBot: Python on programmeerimiskeel.")
    elif "abi" in message:
        print("PyBot: Kirjuta tere, nimi või python.")
    else:
        print("PyBot: Ma ei saanud aru. Kirjuta abi, kui vajad vihjet.")
