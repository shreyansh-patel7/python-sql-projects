import sqlite3


connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT NOT NULL,
    marks INTEGER
)
""")
connection.commit()


while True:
    print("\n" + "=" * 60)
    print("      ACADEMIC RECORDS MANAGEMENT SYSTEM")
    print("               XYZ COLLEGE")
    print("=" * 60)

    print("""
1. Add a new student
2. View all students
3. Search for a student
4. Update existing student details
5. Delete a student
6. Exit the system
""")

    choice = input("Enter your option (1-6): ")

  
    if choice == "1":
        print("\n" + "-" * 50)
        print("ADD NEW STUDENT")
        print("-" * 50)

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter course name: ")
        marks = int(input("Enter academic marks: "))

        cursor.execute(
            "INSERT INTO records (name, age, course, marks) VALUES (?, ?, ?, ?)",
            (name, age, course, marks)
        )
        connection.commit()

        print("\nStudent added successfully!")

    
    elif choice == "2":
        print("\n" + "-" * 60)
        print("ALL STUDENT RECORDS")
        print("-" * 60)

        cursor.execute("SELECT * FROM records")
        rows = cursor.fetchall()

        if rows:
            print("ID | Name | Age | Course | Marks")
            print("-" * 60)
            for row in rows:
                print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4])
        else:
            print("No student records found.")

   
    elif choice == "3":
        print("\n" + "-" * 50)
        print("SEARCH STUDENT")
        print("-" * 50)

        print("""
1. Search by Student ID
2. Search by Student Name
""")

        search_choice = input("Enter your choice: ")

        if search_choice == "1":
            stu_id = int(input("Enter student ID: "))
            cursor.execute("SELECT * FROM records WHERE student_id = ?", (stu_id,))
            row = cursor.fetchone()

            if row:
                print("\nStudent Found:", row)
            else:
                print("\nStudent not found.")

        elif search_choice == "2":
            name = input("Enter student name: ")
            cursor.execute("SELECT * FROM records WHERE name = ?", (name,))
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print("\nStudent Found:", row)
            else:
                print("\nStudent not found.")


    elif choice == "4":
        print("\n" + "-" * 50)
        print("UPDATE STUDENT RECORD")
        print("-" * 50)

        stu_id = int(input("Enter student ID to update: "))
        cursor.execute("SELECT * FROM records WHERE student_id = ?", (stu_id,))
        row = cursor.fetchone()

        if not row:
            print("Student not found.")
        else:
            print("\nCurrent Record:", row)
            print("""
1. Update Name
2. Update Age
3. Update Course
4. Update Marks
""")

            update_choice = input("Enter option: ")

            if update_choice == "1":
                new_name = input("Enter new name: ")
                cursor.execute(
                    "UPDATE records SET name = ? WHERE student_id = ?",
                    (new_name, stu_id)
                )

            elif update_choice == "2":
                new_age = int(input("Enter new age: "))
                cursor.execute(
                    "UPDATE records SET age = ? WHERE student_id = ?",
                    (new_age, stu_id)
                )

            elif update_choice == "3":
                new_course = input("Enter new course: ")
                cursor.execute(
                    "UPDATE records SET course = ? WHERE student_id = ?",
                    (new_course, stu_id)
                )

            elif update_choice == "4":
                new_marks = int(input("Enter new marks: "))
                cursor.execute(
                    "UPDATE records SET marks = ? WHERE student_id = ?",
                    (new_marks, stu_id)
                )

            connection.commit()
            print("\nStudent record updated successfully.")

    
    elif choice == "5":
        print("\n" + "-" * 50)
        print("DELETE STUDENT RECORD")
        print("-" * 50)

        stu_id = int(input("Enter student ID to delete: "))
        cursor.execute("SELECT * FROM records WHERE student_id = ?", (stu_id,))
        row = cursor.fetchone()

        if row:
            print("\nStudent Found:", row)
            confirm = input("Are you sure you want to delete? (yes/no): ")

            if confirm.lower() == "yes":
                cursor.execute(
                    "DELETE FROM records WHERE student_id = ?",
                    (stu_id,)
                )
                connection.commit()
                print("\nStudent deleted successfully.")
            else:
                print("\nDeletion cancelled.")
        else:
            print("\nStudent not found.")


    elif choice == "6":
        print("\nThank you for using the system. Goodbye!")
        connection.close()
        break

    else:
        print("\nInvalid choice. Please try again.")
