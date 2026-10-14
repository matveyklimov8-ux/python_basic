sentence = input("Sisesta lause: ")
letter = input("Sisesta täht: ")
if len(letter) != 1:
    print("Palun sisesta täpselt üks täht.")
else:
    count = sentence.lower().count(letter.lower())
    print(f"Täht {letter} esineb {count} korda.")
