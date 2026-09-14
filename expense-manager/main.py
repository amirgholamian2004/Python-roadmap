from storage import save_expenses, load_expenses
from expense import Expense

def show_menu():
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Delete expense")
    print("4. Total expenses")
    print("5. Exit")

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("choose an option: ")

        if choice == "1":
            name = input("Enter the name of your expense: ")
            try:
                cost_input = input("Enter the cost of your expense: ")
                cost_input = cost_input.replace("/", "").replace(",", "").replace(".", "")
                cost = float(cost_input)
                expenses.append(Expense(name, cost))
                print("Expense has been saved successfully.")
            except ValueError:
                print("Invalid input!!! try again...")
                continue

        elif choice == "2":
            if not expenses:
                print("No expenses added yet!")
            for index, value in enumerate(expenses):
                print(f"{index+1}--> name: {value.name}--> cost: {value.cost}")

        elif choice == "3":
            for index, value in enumerate(expenses):
                print(f"expense number--> {index+1}--> name: {value.name}--> cost: {value.cost}")
            try:
                expense_number = int(input("Enter expense number to delete: "))
                deleted_expense = expenses.pop(expense_number-1)
                print("Expense has been removed successfully.")
                print(f"deleted expense: {deleted_expense.name}")
            except ValueError:
                print("Please enter a valid number.")
                continue
            except IndexError:
                print("That expense number doesn't exist.")

        elif choice == "4":
            if not expenses:
                print("No expenses added yet!")
            total = 0
            for expense in expenses:
                total += expense.cost
            print(f"Your total expense is : {total:.1f}")

        elif choice == "5":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()



