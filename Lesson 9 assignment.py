import locale                 

# Seting locale for currency formatting to US
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def main():
    print("Welcome to Budget Tracker!")
    
    # Get monthly income variable
    income = get_monthly_income()
    
    # Get expenses variable
    expenses = get_expenses()
    
    # Calculate total expenses 
    total_expenses = sum(expenses)

    #getting the remaining buget
    remaining_budget = income - total_expenses
    
    # Display results
    print("\n--- Budget Summary ---")
    print(f"Total Income: {locale.currency(income)}")
    print(f"Total Expenses: {locale.currency(total_expenses)}")
    print(f"Remaining Budget: {locale.currency(remaining_budget)}")
    
    # Displaying each expense
    print("\n--- Expense List ---")
    for num, expense in enumerate(expenses, 1):
        print(f"{num}. {locale.currency(expense)}")
    
    print("\nCompleted by, Armando Gaona")

#list of users expesnses
def get_monthly_income():
    while True:
        income = input("Enter your monthly income: ")
        try:
            income = float(income)
            if income >= 0:
                return income
            print("Income cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


#section obtaining users expenses
def get_expenses():
    expenses = []
    while True:
        expense = input("Enter an expense amount (or '0' to finish): ")
        try:
            expense = float(expense)
            if expense == 0:
                break
            elif expense > 0:
                expenses.append(expense)
            else:
                print("Expense cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")
    return expenses

if __name__ == "__main__":
    main()
