import random, os, time

colors = "RGBY"
simon = ""

for score in range(0, 10):
    simon += random.choice(colors)
    i = 1
    for color in simon:
        print(i, color)
        time.sleep(0.5)
        i += 1
        os.system("cls")
    guess = input("Repeat: ")
    os.system("cls")
    if guess != simon:
        print(f"Game over, your final score is {score}!")
        break