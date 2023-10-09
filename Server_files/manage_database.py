#!/usr/bin/python3

import sqlite3

'''Module creates a database and provides provides on how
   to add, update, delete and exit from the script'''


conn = sqlite3.connect("face_data.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS face_data
                  (name TEXT PRIMARY KEY, access_rights TEXT)''')
conn.commit()

while True:
    print("Choose an option:")
    print("1. UPDATE")
    print("2. NEW")
    print("3. DEL")
    print("4. DISPLAY")
    print("5. EXIT")
                                
    choice = input("Enter your choice: ").strip().lower()
                                        
    if choice == "update":
        name = input("Enter the name you want to update: ")
        new_access_rights = input("Enter the new access_rights: ")
        
        cursor.execute("UPDATE face_data SET access_rights = ? WHERE name = ?", (new_access_rights, name))
        conn.commit()
        print("Update successful!")

    elif choice == "new":
        name = input("Enter the new name: ")
        access_rights = input("Enter the access_rights: ")

        cursor.execute("INSERT INTO face_data (name, access_rights) VALUES (?, ?)", (name, access_rights))
        conn.commit()
        print("New entry added!")

    elif choice == "del":
        name = input("Enter the name you want to delete: ")

        cursor.execute("DELETE FROM face_data WHERE name = ?", (name,))
        conn.commit()
        print("Entry deleted!")

    elif choice == "display":

        cursor.execute("SELECT * FROM face_data")
        rows = cursor.fetchall()

        print("Name\tAccess Rights")
        print("-------------------")
        for row in rows:
            print(f"{row[0]}\t{row[1]}")

    elif choice == "exit":
        break

conn.close()
