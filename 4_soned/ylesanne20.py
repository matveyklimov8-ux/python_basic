secret = "python"
attempts_left = 5
while attempts_left > 0:
    guess = input("Arva salasõna: ")
    if guess == secret:
        print("Õige vastus!")
        break
    attempts_left -= 1
    if attempts_left > 0:
        print("Vale vastus. Katseid jäänud:", attempts_left)
else:
    print("Katsed said otsa. Salasõna oli:", secret)
