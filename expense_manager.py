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
