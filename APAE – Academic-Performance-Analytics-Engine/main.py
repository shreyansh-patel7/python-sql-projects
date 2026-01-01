import sqlite3

connection = sqlite3.connect("academic_records.db")
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


def line():
    print("-" * 70)


def add_student():
    line()
    print("add new student details below")
    name = input("enter student name: ")
    age = int(input("enter age: "))
    course = input("enter course name: ")
    marks = int(input("enter marks: "))

    cursor.execute(
        "INSERT INTO records (name, age, course, marks) VALUES (?, ?, ?, ?)",
        (name, age, course, marks)
    )
    connection.commit()
    print("student added successfully")
    line()


def view_students():
    line()
    print("list of all students present in the system")
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()

    if not rows:
        print("no student data available right now")
    else:
        print("ID | Name | Age | Course | Marks")
        line()
        for row in rows:
            print(row[0], row[1], row[2], row[3], row[4])
    line()


def search_student():
    line()
    print("search student records")
    print("1. search by student id")
    print("2. search by name")
    choice = input("enter choice: ")

    if choice == "1":
        sid = int(input("enter student id: "))
        cursor.execute("SELECT * FROM records WHERE student_id = ?", (sid,))
        row = cursor.fetchone()
        if row:
            print("student found:", row)
        else:
            print("student not found")

    elif choice == "2":
        name = input("enter student name: ")
        cursor.execute("SELECT * FROM records WHERE name = ?", (name,))
        rows = cursor.fetchall()
        if rows:
            for r in rows:
                print("student found:", r)
        else:
            print("student not found")
    line()


def update_student():
    line()
    sid = int(input("enter student id to update: "))
    cursor.execute("SELECT * FROM records WHERE student_id = ?", (sid,))
    row = cursor.fetchone()

    if not row:
        print("student not found cannot update")
        line()
        return

    print("current record:", row)
    print("what do you want to update")
    print("1 name")
    print("2 age")
    print("3 course")
    print("4 marks")

    ch = input("enter choice: ")

    if ch == "1":
        new_name = input("enter new name: ")
        cursor.execute("UPDATE records SET name = ? WHERE student_id = ?", (new_name, sid))

    elif ch == "2":
        new_age = int(input("enter new age: "))
        cursor.execute("UPDATE records SET age = ? WHERE student_id = ?", (new_age, sid))

    elif ch == "3":
        new_course = input("enter new course: ")
        cursor.execute("UPDATE records SET course = ? WHERE student_id = ?", (new_course, sid))

    elif ch == "4":
        new_marks = int(input("enter new marks: "))
        cursor.execute("UPDATE records SET marks = ? WHERE student_id = ?", (new_marks, sid))

    connection.commit()
    print("student details updated")
    line()


def delete_student():
    line()
    sid = int(input("enter student id to delete: "))
    cursor.execute("SELECT * FROM records WHERE student_id = ?", (sid,))
    row = cursor.fetchone()

    if not row:
        print("student not found")
    else:
        print("student record:", row)
        confirm = input("are you sure you want to delete this student yes/no: ")
        if confirm.lower() == "yes":
            cursor.execute("DELETE FROM records WHERE student_id = ?", (sid,))
            connection.commit()
            print("student deleted")
        else:
            print("deletion cancelled")
    line()


def analytics_menu():
    while True:
        line()
        print("analytics and insights section")
        print("1 top three performers")
        print("2 students at risk (marks below 40)")
        print("3 course wise average marks")
        print("4 total student count")
        print("5 back to main menu")

        ch = input("enter option: ")

        if ch == "1":
            cursor.execute("SELECT * FROM records ORDER BY marks DESC LIMIT 3")
            rows = cursor.fetchall()
            print("top performers are:")
            for r in rows:
                print(r)

        elif ch == "2":
            cursor.execute("SELECT * FROM records WHERE marks < 40")
            rows = cursor.fetchall()
            print("students at risk list")
            if rows:
                for r in rows:
                    print(r)
            else:
                print("no students currently under risk")

        elif ch == "3":
            cursor.execute("""
                SELECT course, AVG(marks) 
                FROM records 
                GROUP BY course
            """)
            rows = cursor.fetchall()
            print("course wise average performance")
            for r in rows:
                print("course:", r[0], "average marks:", round(r[1], 2))

        elif ch == "4":
            cursor.execute("SELECT COUNT(*) FROM records")
            count = cursor.fetchone()[0]
            print("total number of students:", count)

        elif ch == "5":
            break

        else:
            print("invalid choice try again")


while True:
    line()
    print("academic records analytics and management system")
    print("choose an option")
    print("1 add student")
    print("2 view all students")
    print("3 search student")
    print("4 update student details")
    print("5 delete student")
    print("6 analytics and insights")
    print("7 exit system")

    choice = input("enter option number: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        analytics_menu()

    elif choice == "7":
        print("closing system thank you")
        connection.close()
        break

    else:
        print("wrong option entered please try again")
