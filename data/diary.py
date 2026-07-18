import sqlite3, getpass, os, sys, time
from dotenv import load_dotenv

load_dotenv()

connection = sqlite3.connect('diary.db')
cursor = connection.cursor()
user = getpass.getuser()

hometitle = f"""{" "*20}{user}'s Diary:
- Home                                  [0]*
- Add entry                             [1]
- View entry                            [2]
- Edit entry                            [3]
- Delete entry                          [4]
- Edit password                         [5]
- Exit                                  [6]
"""

addentrytitle = f"""{" "*20}{user}'s Diary:
- Home                                  [0]
- Add entry                             [1]*
- View entry                            [2]
- Edit entry                            [3]
- Delete entry                          [4]
- Edit password                         [5]
- Exit                                  [6]
"""

viewentrytitle = f"""{" "*20}{user}'s Diary:
- Home                                  [0]
- Add entry                             [1]
- View entry                            [2]*
- Edit entry                            [3]
- Delete entry                          [4]
- Edit password                         [5]
- Exit                                  [6]
"""

editentrytitle = f"""{" "*20}{user}'s Diary:
- Home                                  [0]
- Add entry                             [1]
- View entry                            [2]
- Edit entry                            [3]*
- Delete entry                          [4]
- Edit password                         [5]
- Exit                                  [6]
"""

deleteentrytitle = f"""{" "*20}{user}'s Diary:
- Home                                  [0]
- Add entry                             [1]
- View entry                            [2]
- Edit entry                            [3]
- Delete entry                          [4]*
- Edit password                         [5]
- Exit                                  [6]
"""

editpasswordtitle = f"""{" "*20}{user}'s Diary:
- Home                                  [0]
- Add entry                             [1]
- View entry                            [2]
- Edit entry                            [3]
- Delete entry                          [4]
- Edit password                         [5]*
- Exit                                  [6]
"""

exittitle = f"""{" "*20}{user}'s Diary:
- Home                                  [0]
- Add entry                             [1]
- View entry                            [2]
- Edit entry                            [3]
- Delete entry                          [4]
- Edit password                         [5]
- Exit                                  [6]*
"""

def options(option):
    if option == "0":
        home()
    elif option == "1":
        addEntry()
    elif option == "2":
        viewEntry()
    elif option == "3":
        editEntry()
    elif option == "4":
        deleteEntry()
    elif option == "5":
        editPassword()
    elif option == "6":
        exitDiary()
    else:
        home()

def home():

    os.system("cls")

    cursor.execute("""CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        note TEXT,
        ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

    print(hometitle)

    option = input(f"{user}/> ") or "0"

    options(option)

def addEntry():
    os.system("cls")
    print(addentrytitle)
    name = input(f"{user}/> ") or "Empty"
    if name == "0" or name == "1" or name == "2" or name == "3" or name == "4" or name == "5" or name == "6":
        options(name)
    else:
        os.system("cls")
        print(addentrytitle)
        note = input(f"{user}/{name}/> ") or "Empty"
        cursor.execute(f"INSERT INTO entries (name, note) VALUES (?, ?)", (name, note))
        connection.commit()
        os.system("cls")
        print(addentrytitle)
        option = input(f"{user}/> ") or "0"
        options(option)

def viewEntry():
    os.system("cls")
    print(viewentrytitle)
    print("(ID, Name, Note, Timestamp)")
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()
    for entry in entries:
        print(entry)
    option = input(f"\n{user}/> ") or "0"
    options(option)

def editEntry():
    os.system("cls")
    print(editentrytitle)
    print("Edit an entry (ENTER) ?\n")
    showEntry = input(f"{user}/> ")
    showEntries(showEntry)

    print("\nID of entry to change (ENTER to go back): \n")
    entryid = input(f"{user}/> ") or "Back"

    if entryid == "Back":
        editEntry()
    else:
        pass

    os.system("cls")
    print(addentrytitle)
    cursor.execute("SELECT * FROM entries WHERE id = ?", entryid)
    selectedEntry = cursor.fetchall()
    selectedEntry = selectedEntry[0]
    entryDetails(selectedEntry)

    print(f"\nSet Name of {selectedEntry[1]}\n")
    name = input(f"{user}/{selectedEntry[1]}/> ") or "Empty"
    cursor.execute("UPDATE entries SET name = ?WHERE id = ?", (name, entryid))
    cursor.execute("SELECT * FROM entries WHERE id = ?", entryid)
    selectedEntry = cursor.fetchall()
    selectedEntry = selectedEntry[0]
    entryDetails(selectedEntry)

    print(f"\nSet Note in {selectedEntry[1]}\n")
    note = input(f"{user}/{selectedEntry[1]}/> ") or "Empty"

    cursor.execute("UPDATE entries SET note = ? WHERE id = ?", (note, entryid))

    cursor.execute("UPDATE entries SET ts = CURRENT_TIMESTAMP WHERE id = ?", entryid)

    print("New Entry:")

    cursor.execute("SELECT * FROM entries WHERE id = ?", entryid)
    selectedEntry = cursor.fetchall()
    selectedEntry = selectedEntry[0]
    entryDetails(selectedEntry)

    print("\nSave changes or Edit again?\n")

    saveOrEdit = input(f"{user}/> ").lower()
    if saveOrEdit == "s" or saveOrEdit == "save" or saveOrEdit == "1":
        connection.commit()
        home()
    elif saveOrEdit == "e" or saveOrEdit == "edit" or saveOrEdit == "2":
        connection.rollback()
        editEntry()
    else:
        connection.commit()
        home()

def deleteEntry():
    os.system("cls")
    print(deleteentrytitle)
    print("Delete an entry (ENTER) ?\n")
    showEntry = input(f"{user}/> ")
    showEntries(showEntry)

    print("\nID of entry to delete: \n")
    entryid = input(f"{user}/> ")

    cursor.execute("SELECT * FROM entries WHERE id = ?", entryid)
    deletedEntry = cursor.fetchall()

    cursor.execute("DELETE FROM entries WHERE id = ?", entryid)

    os.system("cls")
    print(deleteentrytitle)
    print(f"Removed: {deletedEntry}")
    print("\nSave changes or Undo?\n")

    saveOrUndo = input(f"{user}/> ").lower()
    if saveOrUndo == "s" or saveOrUndo == "save" or saveOrUndo == "1":
        connection.commit()
        home()
    elif saveOrUndo == "e" or saveOrUndo == "undo" or saveOrUndo == "2":
        connection.rollback()
        deleteEntry()
    else:
        connection.commit()
        home()

def editPassword():
    for j in range(2, -1, -1):
            os.system("cls")
            print(editpasswordtitle)
            print("Enter current password: \n")
            oldPassword = input(f"{user}/> ")
            if oldPassword == "0" or oldPassword == "1" or oldPassword == "2" or oldPassword == "3" or oldPassword == "4" or oldPassword == "5" or oldPassword == "6":
                options(oldPassword)
            else:
                if oldPassword == os.getenv("DIARYPASSWORD"):
                    changePassword()
                    os.system("cls")
                    print(editpasswordtitle)
                    option = input(f"{user}/> ") or "0"
                    options(option)
                else:
                    print(f"Password incorrect, {j} tries remaining..."); time.sleep(1)
    os.system("cls")
    print(editpasswordtitle)
    option = input(f"{user}/> ") or "0"
    options(option)

def exitDiary():
    os.system("cls")
    print(exittitle)
    connection.close()
    time.sleep(1)
    sys.exit()

def entryDetails(selectedEntry):
    os.system("cls")
    print(editentrytitle)
    print(f"ID = {selectedEntry[0]}")
    print(f"Name = {selectedEntry[1]}")
    print(f"Note = {selectedEntry[2]}")
    print(f"Timestamp = {selectedEntry[3]}")

def showEntries(showEntry):
    if showEntry == "0" or showEntry == "1" or showEntry == "2" or showEntry == "3" or showEntry == "4" or showEntry == "5" or showEntry == "6":
        options(showEntry)
    else:
        os.system("cls")
        print(editentrytitle)
        print("(ID, Name, Note, Timestamp)")
        cursor.execute("SELECT * FROM entries")
        entries = cursor.fetchall()
        for entry in entries:
            print(entry)

def changePassword():
    os.system("cls")
    print(editpasswordtitle)
    print("Enter new password: \n")
    newPassword = input(f"{user}/> ")
    if len(newPassword) < 4:
        print("Password must be at least 4 characters!"); time.sleep(1)
        changePassword()
    else:
        with open(".env", "w") as f:
            f.write(f"DIARYPASSWORD = {newPassword}")

def main():
    for i in range(2, -1, -1):
        guessedPassword = input(f"Password for {user}'s diary: ")
        if guessedPassword == os.getenv("DIARYPASSWORD"):
            print(f"Welcome, {user}..."); time.sleep(1)
            home()
        else:
            print(f"Incorrect password, {i} more trie(s)")
    print("(Hint: check the .env file)")

try:
    main()
except KeyboardInterrupt:
    exitDiary()
