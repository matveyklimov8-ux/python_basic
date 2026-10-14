word = input("Sisesta sõna: ")
print("Tagurpidi:", word[::-1])

# Sama tulemus tsükliga:
reversed_word = ""
for character in word:
    reversed_word = character + reversed_word
print("Tagurpidi (tsükliga):", reversed_word)
