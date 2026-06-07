class User:

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def __str__(self):
        return "Name is {}, age is {} and role is {}".format(self.name,self.age,self.role)

    def __del__(self):
        print(f"{self.name} was deleted")

def prompt():

    while True:
        moduser = input("\"create\" or \"delete\" a user? (\"list\" a user) ")

        if moduser == "create":
            name = input("name of user? ")
            age = input("age of user? ")
            role = input("role of user? ")
            user = User(name, age, role)
            print(f"New user created whos called {user.name}, is {user.age} years old and is a {user.role}")

        elif moduser == "list":
            print(user)

        elif moduser == "delete":
            del user

prompt()
