
from db import connect


def add_expense(user_id, amount, category, description):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (user_id, amount, category, description) VALUES (?, ?, ?, ?)",
        (user_id, amount, category, description)
    )

    conn.commit()
    conn.close()


def calculate_total(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id=?", (user_id,))
    result = cursor.fetchone()[0]

    conn.close()
    return result if result else 0


def list_expenses(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT amount, category, description FROM expenses WHERE user_id=?", (user_id,))
    expenses = cursor.fetchall()

    conn.close()

    if not expenses:
        print("No expenses found.")
        return

    for exp in expenses:
        print(f"Amount: {exp[0]} | Category: {exp[1]} | Description: {exp[2]}")


def filter_by_category(user_id, category):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT amount, category, description FROM expenses WHERE user_id=? AND category=?",
        (user_id, category)
    )

    expenses = cursor.fetchall()
    conn.close()

    if not expenses:
        print("No expenses found.")
        return

    for exp in expenses:
        print(f"Amount: {exp[0]} | Category: {exp[1]} | Description: {exp[2]}")
