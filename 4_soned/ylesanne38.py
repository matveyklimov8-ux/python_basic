password = input("Sisesta parool: ")
checks = {
    "vähemalt 8 tähemärki": len(password) >= 8,
    "vähemalt üks suurtäht": any(ch.isupper() for ch in password),
    "vähemalt üks väiketäht": any(ch.islower() for ch in password),
    "vähemalt üks number": any(ch.isdigit() for ch in password),
    "vähemalt üks erimärk": any(not ch.isalnum() and not ch.isspace() for ch in password),
}
score = sum(checks.values())
print(f"Tulemus: {score}/5")
if score <= 2:
    print("Hinnang: Nõrk parool")
elif score <= 4:
    print("Hinnang: Keskmine parool")
else:
    print("Hinnang: Kõik nõuded täidetud")
missing = [name for name, passed in checks.items() if not passed]
if missing:
    print("Täitmata tingimused:")
    for item in missing:
        print("-", item)
else:
    print("Kõik tingimused on täidetud.")
