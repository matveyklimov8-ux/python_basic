# Ülesanne 38. Nime töötlemine

def puhasta_nimi(nimi):
    return nimi.strip()

def vorminda_nimi(nimi):
    return puhasta_nimi(nimi).title()

def loo_tervitus(nimi):
    return f"Tere, {vorminda_nimi(nimi)}!"

print(loo_tervitus("  mARI kASK  "))
