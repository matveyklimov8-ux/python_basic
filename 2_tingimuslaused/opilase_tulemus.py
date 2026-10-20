name = input("Nimi: ")
points = int(input("Punktisumma: "))
absences = int(input("Puudumiste arv: "))
works = input("Kas kõik tööd on esitatud (jah/ei): ").strip().lower()

if points >= 90:
    grade = 5
elif points >= 75:
    grade = 4
elif points >= 50:
    grade = 3
elif points >= 20:
    grade = 2
else:
    grade = 1

print("Õpilane:", name)
print("Hinne:", grade)
if absences > 10:
    print("Hoiatus: liiga palju puudumisi.")
else:
    print("Puudumiste arv on lubatud.")
if works == "jah":
    print("Kõik tööd on esitatud.")
else:
    print("Kõik tööd ei ole esitatud.")
if grade >= 3 and absences <= 10 and works == "jah":
    print("Aine on läbitud.")
else:
    if grade < 3 or absences > 10 or works != "jah":
        print("Aine ei ole läbitud.")
