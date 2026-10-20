# Ülesanne 31. Järjendi suurim element – max() ei kasutata

def suurim_element(arvud):
    if len(arvud) == 0:
        return None
    suurim = arvud[0]
    for arv in arvud[1:]:
        if arv > suurim:
            suurim = arv
    return suurim

print(suurim_element([3, 8, 2, 5]))
print(suurim_element([-9, -2, -7]))
print(suurim_element([]))
