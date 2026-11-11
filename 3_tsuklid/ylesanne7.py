# Ülesanne 7. Kahe- ja kolmekordistamine
# Prognoos: esimene tsükkel kuvab 1, 2, 4, 8, 16, 32, 64.
# Teine tsükkel kuvab 1, 3, 9, 27, 81.
# Muutuja arv muutub igas ringis: esimeses tsüklis korrutatakse kahega,
# teises tsüklis kolmega. Tsükkel peatub enne esimese 100 või suurema arvu kuvamist.
arv = 1
while arv < 100:
    print(arv)
    arv *= 2

print("Kolmekordistades:")
arv = 1
while arv < 100:
    print(arv)
    arv *= 3
