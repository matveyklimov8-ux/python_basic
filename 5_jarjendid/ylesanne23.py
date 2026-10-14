# Ülesanne 23. Kõige pikem ja kõige lühem sõna
sonad = ["arvuti", "programmeerimine", "hiir", "klaviatuur", "monitor"]
pikim = sonad[0]
lyhim = sonad[0]
for sona in sonad[1:]:
    if len(sona) > len(pikim):
        pikim = sona
    if len(sona) < len(lyhim):
        lyhim = sona
print("Pikim sõna:", pikim, "–", len(pikim), "tähemärki")
print("Lühim sõna:", lyhim, "–", len(lyhim), "tähemärki")
