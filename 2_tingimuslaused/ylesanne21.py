a = float(input("Esimene külg: "))
b = float(input("Teine külg: "))
c = float(input("Kolmas külg: "))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Võrdkülgne kolmnurk")
    elif a == b or a == c or b == c:
        print("Võrdhaarne kolmnurk")
    else:
        print("Erikülgne kolmnurk")
else:
    print("Kolmnurk ei ole võimalik.")
