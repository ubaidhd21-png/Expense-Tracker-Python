from expense_manager import add_expense, calculate_total, list_expenses, filter_by_category
from db import create_tables, connect


def register():
    conn = connect()
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    print("User registered!")


def login():
    conn = connect()
    cursor = conn.cursor()

    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT id FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Invalid credentials")
        return None


def main():
    create_tables()

    print("1. Register")
    print("2. Login")
    choice = input("Choose: ")

    if choice == "1":
        register()

    user_id = login()
    if not user_id:
        return

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. Show total")
        print("3. List expenses")
        print("4. Filter by category")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(user_id, amount, category, description)

        elif choice == "2":
            print("Total:", calculate_total(user_id))

        elif choice == "3":
            list_expenses(user_id)

        elif choice == "4":
            category = input("Enter category: ")
            filter_by_category(user_id, category)

        elif choice == "5":
            break


if __name__ == "__main__":
    main()
