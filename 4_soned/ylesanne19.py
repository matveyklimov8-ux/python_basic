character = input("Sisesta tähemärk: ")
vowels = "aeiouõäöüAEIOUÕÄÖÜ"
if len(character) != 1:
    print("Viga: sisesta täpselt üks tähemärk.")
elif character in vowels:
    print("Tegemist on täishäälikuga.")
elif character.isalpha():
    print("Tegemist on kaashäälikuga.")
elif character.isdigit():
    print("Tegemist on numbriga.")
else:
    print("Tegemist on muu sümboliga.")
