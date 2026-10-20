# Ülesanne 29. Sõne tagurpidi tsükli abil

def poora_sone(tekst):
    tulemus = ""
    for taht in tekst:
        tulemus = taht + tulemus
    return tulemus

print(poora_sone("programmeerimine"))
