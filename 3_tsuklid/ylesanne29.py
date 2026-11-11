from random import randint

# Prognoos: 100 täringuviske korral tuleb kuus keskmiselt umbes 100/6 ehk 16–17 korda.
# Täpne arv muutub igal käivitamisel, sest iga vise on juhuslik.
# Mitme käivituse tulemusi võrreldes peaks sagedus üldiselt lähenema 1/6-le.
count_six = 0
i = 0
while i < 100:
    if randint(1, 6) == 6:
        count_six += 1
    i += 1

print("Täringut visati 100 korda.")
print("Kuus saadi", count_six, "korda.")
