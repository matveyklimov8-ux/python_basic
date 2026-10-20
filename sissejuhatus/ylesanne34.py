price_without_vat = float(input("Kauba hind ilma käibemaksuta: "))
vat_rate = 0.24  # Näidismäär; kasuta õpetaja antud määra, kui see erineb.
vat = price_without_vat * vat_rate
price_with_vat = price_without_vat + vat
print("Käibemaks:", round(vat, 2), "eurot")
print("Hind koos käibemaksuga:", round(price_with_vat, 2), "eurot")
