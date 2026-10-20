# Ülesanne 32. Paaritute arvude loendamine

def paaritute_arv(arvud):
    kogus = 0
    for arv in arvud:
        if arv % 2 != 0:
            kogus += 1
    return kogus

print(paaritute_arv([2, 3, 5, 8, 11, 14]))
