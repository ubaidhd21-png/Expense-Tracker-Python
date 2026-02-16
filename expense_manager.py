from file_handler import load_expenses, save_expenses


def add_expense(amount, category, description):
    expenses = load_expenses()

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)


def calculate_total():
    expenses = load_expenses()
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"Amount: {expense['amount']} | "
            f"Category: {expense['category']} | "
            f"Description: {expense['description']}"
        )
