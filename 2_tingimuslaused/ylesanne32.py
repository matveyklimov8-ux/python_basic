balance = 1000
pin = "1234"
entered_pin = input("Sisesta PIN: ")
if entered_pin != pin:
    print("Vale PIN.")
else:
    amount = int(input("Väljavõetav summa: "))
    if amount <= 0:
        print("Summa peab olema positiivne.")
    elif amount > balance:
        print("Kontol pole piisavalt raha.")
    elif amount % 10 != 0:
        print("Summa peab jaguma 10-ga.")
    else:
        balance -= amount
        print(f"Raha väljastatud: {amount} €")
        print(f"Kontole jäi: {balance} €")
