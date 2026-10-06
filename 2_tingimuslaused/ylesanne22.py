username = input("Kasutajanimi: ")

if username == "admin":
    password = input("Parool: ")

    if password == "python123":
        print("Tere tulemast!")
    else:
        print("Vale parool.")
else:
    print("Tundmatu kasutaja.")