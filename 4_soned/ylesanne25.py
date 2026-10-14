code = input("Sisesta testimiseks väljamõeldud isikukood: ").strip()
valid = len(code) == 11 and code.isdigit() and code[0] in "12345678"
print("Vorming on sobiv." if valid else "Vorming ei sobi.")
