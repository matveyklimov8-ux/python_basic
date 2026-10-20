# Ülesanne 33. Sõnade pikkused

def sonade_pikkused(sonad):
    pikkused = []
    for sona in sonad:
        pikkused.append(len(sona))
    return pikkused

print(sonade_pikkused(["Python", "Java", "C"]))
