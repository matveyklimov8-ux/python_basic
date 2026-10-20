# Ülesanne 22. Suurim kolmest – max() ei kasutata

def suurim(a, b, c):
    tulemus = a
    if b > tulemus:
        tulemus = b
    if c > tulemus:
        tulemus = c
    return tulemus

print(suurim(3, 9, 5))
print(suurim(4, 4, 2))
print(suurim(7, 7, 7))
