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
