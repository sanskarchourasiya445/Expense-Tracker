# Expense Tracker Project

expensesList = []  # List to store all expenses
print("Welcome to the Expense Tracker Application")

while True:
    print("\n========= MENU =========")
    print("1. Add a New Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")
    print("========================")

  
    choice = int(input("Enter your choice (1-4): "))
    

    # 1. ADD EXPENSE
    if choice == 1:
        date = input("Enter expense date (DD/MM/YYYY): ")
        category = input("Enter category (Food, Travel, Shopping, Books): ")
        description = input("Enter a short description: ")
        amount = float(input("Enter amount spent: "))
        
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("Expense added successfully.")

    # 2. VIEW ALL EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("No expenses recorded yet.")
        else:
            print("\nExpense History:")
            i = 1
            for expense in expensesList:
                print(
                    f"Expense-{i} -> "
                    f"Date: {expense['date']},"
                    f"Category: {expense['category']}, "
                    f"Description: {expense['description']}, "
                    f"Amount: {expense['amount']}"
                )
                i += 1

    # 3. VIEW TOTAL SPENDING
    elif choice == 3:
        total = 0
        for expense in expensesList:
            total += expense["amount"]

        print("Total Amount Spent:", total)

    # 4. EXIT
    elif choice == 4:
        print("Thank you for using the Expense Tracker.")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")
