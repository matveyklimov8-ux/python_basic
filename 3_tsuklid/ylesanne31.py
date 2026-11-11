from random import randint

# Prognoos: 1000 katse korral tuleb "Kiri" keskmiselt umbes 700 korda
# ja "Kull" umbes 300 korda, sest tõenäosused on vastavalt 70% ja 30%.
# Tegelikud arvud kõiguvad igal käivitamisel ega pea olema täpselt 700 ja 300.
letters = 0
heads = 0
i = 0
while i < 1000:
    if randint(1, 10) <= 7:
        letters += 1  # 7 võimalikku tulemust 10-st ehk 70%.
    else:
        heads += 1    # 3 võimalikku tulemust 10-st ehk 30%.
    i += 1

print("Kiri:", letters)
print("Kull:", heads)
