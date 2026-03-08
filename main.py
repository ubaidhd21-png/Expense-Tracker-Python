from expense_manager import add_expense, calculate_total, list_expenses, filter_by_category


def main():
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

            add_expense(amount, category, description)
            print("Expense added!")

        elif choice == "2":
            print("Total spent:", calculate_total())

        elif choice == "3":
            list_expenses()

        elif choice == "4":
            category = input("Enter category to filter: ")
            filter_by_category(category)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
