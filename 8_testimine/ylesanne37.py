"""Ülesanne 37. Pangakonto saldo"""


class Konto:
    def __init__(self, saldo=0):
        if saldo < 0: raise ValueError("Algne saldo ei tohi olla negatiivne")
        self.saldo = saldo
    def lisa(self, summa):
        if summa <= 0: raise ValueError("Summa peab olema positiivne")
        self.saldo += summa
    def võta(self, summa):
        if summa <= 0 or summa > self.saldo: raise ValueError("Väljamakse ei sobi")
        self.saldo -= summa
k = Konto(100); k.lisa(25); k.võta(10)
assert k.saldo == 115
