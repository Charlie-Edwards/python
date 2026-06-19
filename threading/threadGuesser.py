import threading
import random

def bogo():
    while True:
        guess = random.randint(1, maxtarget)
        if guess == target:
            print(f"Thread {_}: guesed {target} successfully!")
            break

power = int(input("power: "))
threadcount = int(input("threads: "))

maxtarget = 10 ** power
target = random.randint(1, maxtarget)

threads = []

for _ in range(1, threadcount+1, 1):
    t = threading.Thread(target=bogo)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
