# Ülesanne 35. Sama nimega muutujad
arv = 100

def muuda():
    arv = 20  # See on funktsiooni lokaalne muutuja.
    print("Funktsioonis:", arv)

muuda()
print("Põhiprogrammis:", arv)  # Väärtus on endiselt 100.
