import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    phone TEXT
)
""")

conn.commit()


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        phone = input("Enter student phone: ")

        cursor.execute(
            "INSERT INTO students (name, age, phone) VALUES (?, ?, ?)",
            (name, age, phone)
        )
        conn.commit()

        print("✅ Student added successfully!")


    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        print("\nID | NAME | AGE | PHONE")
        print("-" * 30)
        for row in rows:
            print(row[0], row[1], row[2], row[3])


    elif choice == "3":
        sid = input("Enter Student ID to delete: ")

        cursor.execute("DELETE FROM students WHERE id = ?", (sid,))
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Student deleted successfully!")
        else:
            print("❌ Student ID not found.")


    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("❌ Invalid choice. Please try again.")


conn.close()
print("Database connection closed.")









