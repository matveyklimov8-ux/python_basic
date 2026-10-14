text = input("Sisesta töödeldav tekst: ")
while True:
    print("\nTEKSTITÖÖTLUS")
    print("1 - Muuda tekst suurtähtedeks")
    print("2 - Muuda tekst väiketähtedeks")
    print("3 - Kuva teksti pikkus")
    print("4 - Pööra tekst tagurpidi")
    print("0 - Välju")
    choice = input("Valik: ").strip()
    if choice == "1":
        print(text.upper())
    elif choice == "2":
        print(text.lower())
    elif choice == "3":
        print("Pikkus:", len(text))
    elif choice == "4":
        print(text[::-1])
    elif choice == "0":
        print("Head aega!")
        break
    else:
        print("Tundmatu valik.")
    text = input("Sisesta uus tekst (või kasuta sama teksti): ")
