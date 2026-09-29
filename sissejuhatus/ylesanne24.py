seconds = int(input("Sisesta sekundid: "))

minutes = seconds // 60
seconds_left = seconds % 60

print(minutes, "minutit ja", seconds_left, "sekundit")