# Ülesanne 49. Parooli tugevuse kontrollija
# check_password() tagastab ainult täidetud tingimuste arvu (0–5).

TINGIMUSED = [
    ("Vähemalt 8 tähemärki", lambda parool: len(parool) >= 8),
    ("Vähemalt üks suurtäht", lambda parool: any(taht.isupper() for taht in parool)),
    ("Vähemalt üks väiketäht", lambda parool: any(taht.islower() for taht in parool)),
    ("Vähemalt üks number", lambda parool: any(taht.isdigit() for taht in parool)),
    ("Vähemalt üks erimärk", lambda parool: any(not taht.isalnum() for taht in parool)),
]


def check_password(password):
    """Tagastab täidetud paroolitingimuste arvu vahemikus 0–5."""
    return sum(1 for _, kontroll in TINGIMUSED if kontroll(password))


def count_failed_conditions(password):
    """Tagastab täitmata paroolitingimuste arvu."""
    return len(TINGIMUSED) - check_password(password)


def list_failed_conditions(password):
    """Tagastab täitmata tingimuste kirjeldused kasutajale kuvamiseks."""
    return [kirjeldus for kirjeldus, kontroll in TINGIMUSED if not kontroll(password)]


if __name__ == "__main__":
    parool = input("Sisesta parool: ")
    punktid = check_password(parool)
    puuduvad_kokku = count_failed_conditions(parool)
    print(f"Tulemus: {punktid}/5")
    print(f"Täitmata tingimusi: {puuduvad_kokku}")
    puuduvad = list_failed_conditions(parool)
    if puuduvad:
        print("Täitmata nõuded:")
        for tingimus in puuduvad:
            print("-", tingimus)
    else:
        print("Kõik nõuded täidetud.")
