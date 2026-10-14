sentence = input("Sisesta lause: ").lower()
vowels = "aeiouõäöü"
counts = {vowel: 0 for vowel in vowels}
for character in sentence:
    if character in vowels:
        counts[character] += 1
print("Täishäälikuid kokku:", sum(counts.values()))
for vowel, count in counts.items():
    print(f"{vowel}: {count}")
