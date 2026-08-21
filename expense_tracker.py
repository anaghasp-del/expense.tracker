import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="daily_expense"
)

cursor = con.cursor()


# Add new expense
def add_expense():

    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    category_id = int(input("Enter category ID: "))
    payment = input("Enter payment method: ")

    query = """
    INSERT INTO expenses
    (amount, expense_date, category_id, payment_method)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (amount, date, category_id, payment))
    con.commit()

    print("Expense added successfully!")


# Add new category
def add_category():

    name = input("Enter category name: ")

    cursor.execute(
        "INSERT INTO categories (name) VALUES (%s)",
        (name,)
    )

    con.commit()

    print("Category added successfully!")


# View all expenses
def view_expenses():

    query = """
    SELECT expenses.id,
           expenses.amount,
           expenses.expense_date,
           categories.name,
           expenses.payment_method
    FROM expenses
    JOIN categories
    ON expenses.category_id = categories.id
    """

    cursor.execute(query)

    records = cursor.fetchall()

    print("\n----- ALL EXPENSES -----")

    for row in records:
        print(
            "ID:", row[0],
            "| Amount:", row[1],
            "| Date:", row[2],
            "| Category:", row[3],
            "| Payment:", row[4]
        )


# View total spending for a month
def monthly_total():

    month = input("Enter month (YYYY-MM): ")

    query = """
    SELECT SUM(amount)
    FROM expenses
    WHERE DATE_FORMAT(expense_date, '%Y-%m') = %s
    """

    cursor.execute(query, (month,))

    result = cursor.fetchone()

    total = result[0]

    if total is None:
        total = 0

    print("Total spending:", total)


# View spending by category
def category_spending():

    month = input("Enter month (YYYY-MM): ")
    category = input("Enter category name: ")

    query = """
    SELECT SUM(expenses.amount)
    FROM expenses
    JOIN categories
    ON expenses.category_id = categories.id
    WHERE DATE_FORMAT(expenses.expense_date, '%Y-%m') = %s
    AND categories.name = %s
    """

    cursor.execute(query, (month, category))

    result = cursor.fetchone()

    total = result[0]

    if total is None:
        total = 0

    print(category, "spending:", total)


# Main menu
while True:

    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add new expense")
    print("2. Add new category")
    print("3. View all expenses")
    print("4. View total spending for a month")
    print("5. View spending by category")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        add_category()

    elif choice == "3":
        view_expenses()

    elif choice == "4":
        monthly_total()

    elif choice == "5":
        category_spending()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

con.close()

# import MySQL.connector
# con=MySQL.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="expenses"
# )
# cursor=con.cursor()

# def add_expense():
#     amount=int(input("Enter amount: "))
#     date=input("Enter date (YYYY-MM-DD): ")
#     category_id=int(input("Enter category ID: "))
#     payment=input("Enter payment method: ")

# query="""INSERT INTO expenses(amount,expense_date,ca)

