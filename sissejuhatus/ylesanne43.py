today = int(input("Tänase päeva number (0–6): "))
days_forward = int(input("Mitu päeva edasi? "))
print("Uue päeva number:", (today + days_forward) % 7)
