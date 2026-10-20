balance = 500
amount = float(input("Kui palju soovid välja võtta? "))
if amount <= 0:
    print("Vigane summa.")
else:
    if amount > balance:
        print("Kontol pole piisavalt raha.")
    else:
        balance -= amount
        print("Raha väljastatud.")
        print("Kontole jäi", balance, "eurot.")
