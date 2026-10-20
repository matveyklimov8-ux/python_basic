email = input("Sisesta e-post: ")
valid = (
    email.count("@") == 1
    and not any(character.isspace() for character in email)
    and email.split("@")[0] != ""
    and "." in email.split("@")[-1]
    and not email.split("@")[-1].startswith(".")
    and not email.split("@")[-1].endswith(".")
)
print("Aadressi kuju on sobiv." if valid else "Aadressi kuju ei sobi.")
