from expense_manager import add_expense, calculate_total

def main():
    print("Expense Tracker")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    add_expense(amount, category, description)
    print("Expense added successfully")

    print("Total spent:", calculate_total())

if __name__ == "__main__":
    main()
