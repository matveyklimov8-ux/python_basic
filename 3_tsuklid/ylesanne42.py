positiivseid = 0
negatiivseid = 0

while True:
    arv = int(input("Sisesta arv (0 lõpetab): "))
    if arv == 0:
        break
    elif arv > 0:
        positiivseid = positiivseid + 1
    else:
        negatiivseid = negatiivseid + 1

print("Positiivseid:", positiivseid)
print("Negatiivseid:", negatiivseid)
