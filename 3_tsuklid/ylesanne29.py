from random import randint
count_six = 0
i = 0
while i < 100:
    if randint(1, 6) == 6:
        count_six += 1
    i += 1
print("Täringut visati 100 korda.")
print("Kuus saadi", count_six, "korda.")
