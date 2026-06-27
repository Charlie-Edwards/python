from datetime import datetime
import os
import random
import getpass

class Person:

    def __init__(self, name, age, level):

        self.Name = name
        self.Age = age
        self.Level = level

    def __str__(self):
        return "User = {}\n" \
        "Age = {}\n" \
        "Level = {}".format(self.Name,self.Age,self.Level)

    @property
    def Name(self):
        return self.__name
    
    @property
    def Age(self):
        return self.__age

    @property
    def Level(self):
        return self.__level

    @Name.setter
    def Name(self, value):
        if not value == getpass.getuser():
            self.__name = getpass.getuser()
        else:
            self.__name = value

    @Age.setter
    def Age(self, value):
        current_year = datetime.now().year
        self.__age = current_year - 2012

    @Level.setter
    def Level(self, value):
        if not value < 10:
            self.__level = 10
        else:
            self.__level = value

user = Person("Unknown", 0, 0)

xp = 0

while True:
    user.Level = xp // 100
    os.system("cls")
    print(f"{user} ({xp}xp)\n\nSend messages to gain xp\n")
    bleh = input("> ")
    if len(bleh) > 0:
        xp = xp + random.randint(11, 25)
    else:
        pass
