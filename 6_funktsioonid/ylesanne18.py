# Ülesanne 18. print() ja return

def arvuta1(a, b):
    print(a + b)  # Kuvab tulemuse, kuid ei tagasta seda.

def arvuta2(a, b):
    return a + b   # Tagastab tulemuse kasutamiseks programmis.

x = arvuta1(5, 3)
y = arvuta2(5, 3)
print("x =", x)  # None
print("y =", y)  # 8
# return-väärtust saab kasutada uues arvutuses, näiteks print(y * 2).
