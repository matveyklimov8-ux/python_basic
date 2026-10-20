a = float(input("Esimene külg: "))
b = float(input("Teine külg: "))
c = float(input("Kolmas külg: "))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Kolmnurk on võimalik.")
else:
    print("Kolmnurk ei ole võimalik.")
