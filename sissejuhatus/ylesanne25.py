seconds = int(input("Sisesta sekundid: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{hours} h {minutes} min {remaining_seconds} s")
