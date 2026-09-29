minutes = int(input("Sisesta minutid: "))

hours = minutes // 60
minutes_left = minutes % 60

print(hours, "tundi ja", minutes_left, "minutit")