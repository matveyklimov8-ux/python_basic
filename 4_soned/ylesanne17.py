word = input("Sisesta sõna: ").lower()
if word == word[::-1]:
    print("Tegemist on palindroomiga.")
else:
    print("See ei ole palindroom.")