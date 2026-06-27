class Person:

    def __init__(self, name, balance):

        self.__name = name
        self.Balance = balance

    @property
    def Balance(self):
        return self.__balance
    
    @Balance.setter
    def Balance(self, value):
        if not value == 1000:
            self.__balance = 1000
        else:
            self.__balance = value

p1 = Person("Charlie", 1)
print(f"{p1.Balance}")

p1 = Person("Charlie", 1000)
print(f"{p1.Balance}")

for i in range(1, 500000, 1):
    p1 = Person("Charlie", i)
print(f"{p1.Balance}")

p1 = Person("Charlie", -40000)
print(f"{p1.Balance}")

for i in range(1, 9999999, 1):
    p1 = Person("Charlie", i)
print(f"{p1.Balance}")
