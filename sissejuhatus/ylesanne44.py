cents = int(input("Sisesta summa sentides: "))

euros = cents // 100
cents_left = cents % 100

print(euros, "eurot ja", cents_left, "senti")