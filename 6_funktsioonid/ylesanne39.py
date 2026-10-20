# Ülesanne 39. Arvutuste moodul

def liitmine(a, b):
    return a + b

def lahutamine(a, b):
    return a - b

def korrutamine(a, b):
    return a * b

def jagamine(a, b):
    if b == 0:
        return None
    return a / b

def astendamine(a, b):
    return a ** b

def arvuta(a, b, tehe):
    if tehe == "+":
        return liitmine(a, b)
    elif tehe == "-":
        return lahutamine(a, b)
    elif tehe == "*":
        return korrutamine(a, b)
    elif tehe == "/":
        return jagamine(a, b)
    elif tehe == "**":
        return astendamine(a, b)
    return None

for tehe in ("+", "-", "*", "/", "**", "%"):
    print(f"10 {tehe} 2 = {arvuta(10, 2, tehe)}")
print("Nulliga jagamine:", arvuta(5, 0, "/"))
