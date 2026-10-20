# Ülesanne 25. Soodustuse arvutamine

def soodushind(hind, soodustus=10):
    if hind < 0 or not 0 <= soodustus <= 100:
        return None
    return hind * (1 - soodustus / 100)

print(soodushind(100))
print(soodushind(80, 25))
print(soodushind(50, 120))  # None – vigane soodustus
