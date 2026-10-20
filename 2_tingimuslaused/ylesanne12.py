temperature = float(input("Sisesta temperatuur: "))
if temperature < 0:
    print("Külmub")
elif temperature <= 15:
    print("Jahe")
elif temperature <= 25:
    print("Soe")
else:
    print("Palav")
