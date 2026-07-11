import random, time

class Gun:

    def __init__(self, ammo, dmg):
        self.ammo = ammo
        self.dmg = dmg

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"{self.ammo + 1} bullets left... ", end='', flush=True)
            time.sleep(1)
            bullet = random.randint(0, 1)
            if bullet == 0:
                print("click")
                p1.show_health()
            if bullet == 1:
                print("BANG!")
                p1.damage(self.dmg)
                p1.show_health()

class Person:

    def __init__(self, name, health):
        self.name = name
        self.__health = health

    @property
    def Health(self):
        return self.__health

    @Health.setter
    def Health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    def show_health(self):
        print(f"{p1.name} has {self.Health} health")

    def damage(self, dmg):
        global alive
        self.Health -= dmg
        if not self.Health > 0:
            alive = False

name = input("Choose a name (default=Player): ") or "Player"

p1 = Person(name, 100)

g1 = Gun(8, 30)

alive = True

while alive and g1.ammo > 0:
    input()
    Gun.shoot(g1)

print("")

if alive:
    the_end = "You win...!"
if not alive:
    the_end = "Rest in peace.. "

if not alive:
    for i in range(0, len(the_end), 1):
        print(f"{the_end[i]}", end='', flush=True)
        time.sleep(0.5)
    for j in range(0, len(p1.name), 1):
        print(f"{p1.name[j]}", end='', flush=True)
        time.sleep(0.25)
    print(".")
    time.sleep(1)
elif alive: 
    for i in range(0, len(the_end), 1):
        print(f"{the_end[i]}", end='', flush=True)
        time.sleep(0.5)
    print("")
