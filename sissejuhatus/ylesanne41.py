minutes = int(input("Mitu minutit on keskööst möödunud? ")) % (24 * 60)
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{hours:02d}:{remaining_minutes:02d}")
