# Ülesanne 50. Juhuslike arvude statistika
import random

def arvude_summa(arvud):
    summa = 0
    for arv in arvud:
        summa += arv
    return summa

def aritmeetiline_keskmine(arvud):
    if not arvud:
        return None
    return arvude_summa(arvud) / len(arvud)

def suurim_ja_vaikseim(arvud):
    if not arvud:
        return None, None
    suurim = vaikseim = arvud[0]
    for arv in arvud[1:]:
        if arv > suurim:
            suurim = arv
        if arv < vaikseim:
            vaikseim = arv
    return suurim, vaikseim

def paarisarvude_kogus(arvud):
    kogus = 0
    for arv in arvud:
        if arv % 2 == 0:
            kogus += 1
    return kogus

def piirist_suuremate_kogus(arvud, piir):
    kogus = 0
    for arv in arvud:
        if arv > piir:
            kogus += 1
    return kogus

arvud = [random.randint(1, 100) for _ in range(100)]
suurim, vaikseim = suurim_ja_vaikseim(arvud)
print("Arve kokku:", len(arvud))
print("Summa:", arvude_summa(arvud))
print(f"Keskmine: {aritmeetiline_keskmine(arvud):.2f}")
print("Suurim:", suurim, "| Väikseim:", vaikseim)
print("Paarisarve:", paarisarvude_kogus(arvud))
print("Üle 50:", piirist_suuremate_kogus(arvud, 50))
