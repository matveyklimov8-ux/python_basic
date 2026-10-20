score = int(input("Sisesta punktid (0–100): "))
if score >= 90:
    grade = 5
elif score >= 75:
    grade = 4
elif score >= 50:
    grade = 3
elif score >= 20:
    grade = 2
else:
    grade = 1
print("Hinne:", grade)
