text = input("Sisesta tekst: ")
vowels = "aeiouõäöüAEIOUÕÄÖÜ"
print("Tähemärke kokku:", len(text))
print("Tähemärke ilma tühikuteta:", len(text.replace(" ", "")))
print("Sõnu:", len(text.split()))
print("Täishäälikuid:", sum(1 for ch in text if ch in vowels))
print("Numbreid:", sum(1 for ch in text if ch.isdigit()))
