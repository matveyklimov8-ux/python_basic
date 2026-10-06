year = int(input("Sisesta aasta: "))

if year % 400 == 0:
    print("Liigaasta")
elif year % 100 == 0:
    print("Ei ole liigaasta")
elif year % 4 == 0:
    print("Liigaasta")
else:
    print("Ei ole liigaasta")