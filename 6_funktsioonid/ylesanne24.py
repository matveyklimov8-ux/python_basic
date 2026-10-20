# Ülesanne 24. Kolmnurga kontroll

def on_kolmnurk(a, b, c):
    return (a > 0 and b > 0 and c > 0
            and a + b > c and a + c > b and b + c > a)

print(on_kolmnurk(3, 4, 5))
print(on_kolmnurk(1, 2, 10))
print(on_kolmnurk(-1, 2, 2))
