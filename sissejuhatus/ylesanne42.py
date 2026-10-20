current_hour = int(input("Praegune tund (0–23): "))
hours_until_alarm = int(input("Äratuseni mitu tundi? "))
alarm_hour = (current_hour + hours_until_alarm) % 24
print("Äratus heliseb kell", alarm_hour)
