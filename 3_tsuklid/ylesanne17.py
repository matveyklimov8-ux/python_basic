correct_password = "python123"
attempts = 0
success = False
while attempts < 3 and not success:
    password = input("Sisesta parool: ")
    attempts += 1
    if password == correct_password:
        success = True
if success:
    print("Ligipääs lubatud!")
else:
    print("Ligipääs blokeeritud!")
