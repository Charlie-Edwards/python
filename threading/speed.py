import random, os, threading, string

def mode1():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    target = input("Target = ").lower()
    guess = ""
    tries = 0
    if ' ' in target:
        alphabet.append(' ')
    while guess != target:
        guess = ""
        os.system("cls")
        for _ in range(len(target)):
            guess += random.choice(alphabet)
            tries += 1
        print(f"Target = {target}")
        print(f"Guess = {guess}")
        print(f"Tries = {tries}")

def mode2():
    alphabet = []
    target = input("Target = ")
    guess = ""
    tries = 0
    for i in target:
        alphabet.append(i)
    while guess != target:
        guess = ""
        os.system("cls")
        for _ in range(len(target)):
            guess += random.choice(alphabet)
            tries += 1
        print(f"Target = {target}")
        print(f"Guess = {guess}")
        print(f"Tries = {tries}")

def mode3():
    alphabet = list(string.ascii_letters)
    alphabet.append(' ')
    target = input("Target = ")
    guess = ""
    tries = 0
    for i in range(len(target)):
        for j in range(len(alphabet)):
            os.system("cls")
            guess = guess[:i] + alphabet[j]
            print(f"Target = {target}")
            print(f"Guess = {guess}")
            print(f"Tries = {tries}")
            tries += 1
            if target[i] == alphabet[j]:
                break

print("Mode 1 - Hard")
print("Mode 2 - Medium")
print("Mode 3 - Easy")

mode = int(input("Mode: ")) or 3

if mode == 1:
    t = threading.Thread(target=mode1)
elif mode == 2:
    t = threading.Thread(target=mode2)
elif mode == 3:
    t = threading.Thread(target=mode3)
else:
    t = threading.Thread(target=mode3)

t.start()
t.join()
