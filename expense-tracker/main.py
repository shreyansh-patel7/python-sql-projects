import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
create table if not exists expense_info(
  expense_id integer primary key autoincrement,
  title text,
  amount integer,
  category text , 
  date text)
""")
connection.commit()


#MENU OPTION
while True:
    print("==> Expense Tracker System")
    print("1.Add a new expense")
    print("2.View all expenses")
    print("3.Delete an expense by ID")
    print("4.Exit the program")
    
    choice = input("Enter the option you want to select: ")

    if choice == "1":
        title = input("1.Enter the title of the expense: ")
        amount = int(input("2.Enter the amount you spend on that expense: "))
        category = input("3.Enter the category of intrest you spend money on: ")
        date = input("4.Enter the date when you spend the money : ")

        cursor.execute(
        "insert into expense_info(title,amount,category,date)values(?,?,?,?)",
        (title,amount,category,date))
        connection.commit()

        print("===>EXPENSE ADDED SUCCESSFULLY \n-->NEXT TIME KEEP THE EXPENSES LOW\n->AND SAVE MORE ")

    elif choice == "2":
        cursor.execute(
            "select * from expense_info"
        )
        rows = cursor.fetchall()
        print("\nexpense_id|Title|Amount|Category|Date")
        for row in rows:
            print(row[0],row[1],row[2],row[3],row[4])

    elif choice == "3":
        del_id = input("Enter the id of the expense to delete: ")
        cursor.execute(
            "delete from expense_info where expense_id == ? ",
            (del_id,)
        )
        connection.commit()

        if cursor.rowcount>0:
            print("✅ Expense deleted successfully!")
        else:
            print("❌ Expense ID not found.")
        
    elif choice == "4":
        print("EXITING THE COMMAND NOW..........")
        break
    else:
        print("❌ Invalid choice. Please try again.")
connection.close()
print("Database connection closed.")