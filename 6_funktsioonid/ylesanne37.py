# Ülesanne 37. Ostukorvi arvutused

def rea_summa(hind, kogus):
    return hind * kogus

def lisa_kaibemaks(summa, maar):
    return summa * (1 + maar / 100)

def kuva_kokkuvote(summa, maar):
    koos_maksuga = lisa_kaibemaks(summa, maar)
    print(f"Summa ilma käibemaksuta: {summa:.2f} €")
    print(f"Käibemaksuga ({maar}%): {koos_maksuga:.2f} €")

ostusumma = rea_summa(12.50, 2) + rea_summa(4.20, 3) + rea_summa(25, 1)
kuva_kokkuvote(ostusumma, 22)
