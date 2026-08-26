import sqlite3

file = input("File: ")

conn = sqlite3.connect(file)
cursor = conn.cursor()

try:
    while True:
        for line in conn.iterdump():
            print(line)
        sql = input()
        cursor.execute(sql)
        conn.commit()

except:
    conn.close()
