distance = float(input("Teekond kilomeetrites: "))
consumption = float(input("Auto kütusekulu (l/100 km): "))
fuel_price = float(input("Kütuse hind (€/l): "))
fuel_used = distance * consumption / 100
trip_cost = fuel_used * fuel_price
print("Kütust kulub:", round(fuel_used, 2), "l")
print("Reisi kütusekulu maksumus:", round(trip_cost, 2), "€")
