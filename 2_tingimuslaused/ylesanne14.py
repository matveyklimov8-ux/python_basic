color = input("Sisesta valgusfoori värv: ").strip().lower()
if color == "punane":
    print("Seisa!")
elif color == "kollane":
    print("Valmistu!")
elif color == "roheline":
    print("Liigu!")
else:
    print("Tundmatu värv.")
