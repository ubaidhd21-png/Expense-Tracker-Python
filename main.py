from expense_manager import add_expense, calculate_total, list_expenses


def main():
    print("Expense Tracker")
    print("1. Add expense")
    print("2. Show total")
    print("3. List expenses")

    choice = input("Choose option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        add_expense(amount, category, description)
        print("Expense added!")

    elif choice == "2":
        print("Total spent:", calculate_total())

    elif choice == "3":
        list_expenses()

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
