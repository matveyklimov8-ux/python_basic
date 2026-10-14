text = input("Sisesta tekst: ")
result = ""
for character in text:
    if "a" <= character <= "z":
        result += chr((ord(character) - ord("a") + 3) % 26 + ord("a"))
    elif "A" <= character <= "Z":
        result += chr((ord(character) - ord("A") + 3) % 26 + ord("A"))
    else:
        result += character
print("Krüpteeritud:", result)
