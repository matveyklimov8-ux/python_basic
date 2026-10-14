username = input("Kasutajanimi: ")
if not 5 <= len(username) <= 15:
    print("Viga: kasutajanimi peab olema 5–15 tähemärki pikk.")
elif not username.isascii() or not username.isalnum():
    print("Viga: kasutada võib ainult ladina tähti ja numbreid.")
elif not username[0].isalpha():
    print("Viga: kasutajanimi peab algama tähega.")
else:
    print("Kasutajanimi sobib.")
