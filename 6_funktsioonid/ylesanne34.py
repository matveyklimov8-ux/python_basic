# Ülesanne 34. Lokaalne muutuja ja NameError
# Algse variandi viga: kui muutuja tulemus luuakse ainult funktsiooni sees,
# ei ole see väljaspool funktsiooni kättesaadav. Väljaspool kasutamine tekitab
# NameError-i, sest selles nimeruumis pole muutujat nimega tulemus.
# Parandus: tagastame väärtuse return abil ning salvestame selle välisesse muutujasse.

def arvuta():
    tulemus = 25
    return tulemus


arvutuse_tulemus = arvuta()
print(arvutuse_tulemus)
