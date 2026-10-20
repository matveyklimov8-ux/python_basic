# Ülesanne 16. Sekundite teisendamine

def teisenda_sekundid(sekundid):
    tunnid = sekundid // 3600
    minutid = (sekundid % 3600) // 60
    jaak = sekundid % 60
    return tunnid, minutid, jaak

print(teisenda_sekundid(3675))  # (1, 1, 15)
