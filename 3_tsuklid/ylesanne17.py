oige_parool = "python123"
katse = 0
oige = False

while katse < 3 and not oige:
    parool = input("Sisesta parool: ")
    katse = katse + 1

    if parool == oige_parool:
        oige = True
        print("Ligipääs lubatud!")
    else:
        print("Vale parool!")

if not oige:
    print("Ligipääs blokeeritud!")
