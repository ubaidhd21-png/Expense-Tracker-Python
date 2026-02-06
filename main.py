

def main():
    print("Expense Tracker")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    add_expense(amount, category, description)
    print("Expense added successfully")

if __name__ == "__main__":
    main()
