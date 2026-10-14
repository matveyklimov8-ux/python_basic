first = input("Esimene eesnimi: ").strip()
second = input("Teine eesnimi: ").strip()
last = input("Perekonnanimi: ").strip()
if first and second and last:
    initials = f"{first[0].upper()}.{second[0].upper()}.{last[0].upper()}."
    print("Initsiaalid:", initials)
else:
    print("Palun sisesta kõik kolm nime.")
