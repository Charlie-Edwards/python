import sqlite3
import random

class User:

    def __init__(self, id=1, displayname='', username='', plan=''):
        self.id = id
        self.displayname = displayname
        self.username = username
        self.plan = plan
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()

    def load(self, id):
        self.cursor.execute("""
        SELECT * FROM users
        WHERE id = {}
        """.format(id))

        results = self.cursor.fetchone()

        self.id = id
        self.displayname = results[1]
        self.username = results[2]
        self.plan = results[3]

    def append(self):
        self.cursor.execute("""
        INSERT INTO users VALUES
        ({}, '{}', '{}', '{}')
        """.format(self.id, self.displayname, self.username, self.plan))

        self.connection.commit()
        self.connection.close()

    def remove(self):
        self.cursor.execute("""
        DELETE FROM users WHERE ID  = '{}'
        """.format(self.id))

        self.connection.commit()
        self.connection.close()


connection = sqlite3.connect('users.db')
cursor = connection.cursor()

def main():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER,
            displayname TEXT,
            username TEXT,
            plan TEXT
        )
        """)
    print("")
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for user in results:
        print(user)
    action = input("\nappend, list or remove?\n> ").lower()

    if action[0] == "a":
        form_displayname = input("set display name\n> ")
        form_username = input("set username\n> ").lower()
        form_plan = input("free or paid plan?\n> ").lower()
        if form_plan != "paid":
            form_plan = "free"

        u1 = User(
            random.randint(1000000000000000000, 9223372036854775807),
            form_displayname,
            form_username,
            form_plan
        )

        u1.append()
        main()

    elif action[0] == "l":
        main()

    elif action[0] == "r":
        form_id = input("id to remove (id, 'all' or 'back')\n> ")

        if form_id == "all":
            for user in results:
                user_id = user[0]
                cursor.execute("DELETE FROM users WHERE id = {}".format(user_id))
            connection.commit()

        elif form_id == "back":
            main()

        else:
            form_id = int(form_id)
            u1 = User()
            u1.id = form_id
            u1.remove()
        main()

    else:
        main()
main()
