a = float(input("Esimene arv: "))
operation = input("Tehe (+, -, *, /): ").strip()
b = float(input("Teine arv: "))
if operation == "+":
    print("Tulemus:", a + b)
elif operation == "-":
    print("Tulemus:", a - b)
elif operation == "*":
    print("Tulemus:", a * b)
elif operation == "/":
    if b != 0:
        print("Tulemus:", a / b)
    else:
        print("Nulliga ei saa jagada.")
else:
    print("Tundmatu tehe.")
