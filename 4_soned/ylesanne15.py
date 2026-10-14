password = input("Sisesta parool: ")
length = len(password)
if length < 8:
    print("Parool on liiga lühike.")
elif length < 12:
    print("Parooli pikkus on sobiv.")
else:
    print("Pikk parool.")
