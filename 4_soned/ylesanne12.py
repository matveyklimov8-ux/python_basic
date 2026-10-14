sentence = input("Lause: ")
needle = input("Otsitav: ")
index = sentence.find(needle)
if index >= 0:
    print("Leitud indeksilt", index)
else:
    print("Tekstiosa ei leitud.")
