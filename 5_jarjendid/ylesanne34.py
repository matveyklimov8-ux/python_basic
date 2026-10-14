# Ülesanne 34. Nädala müügitulemused
muugid = [125.50, 210.00, 98.75, 340.20, 185.40, 420.00, 275.90]
paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]
for paev, muuk in zip(paevad, muugid):
    print(f"{paev}: {muuk:.2f} €")
korgem = max(muugid)
print(f"Nädala kogumüük: {sum(muugid):.2f} €")
print(f"Keskmine päevamüük: {sum(muugid) / len(muugid):.2f} €")
print(f"Suurim müük: {paevad[muugid.index(korgem)]} ({korgem:.2f} €)")
print("Üle 200-eurose müügiga päevi:", sum(1 for muuk in muugid if muuk > 200))
