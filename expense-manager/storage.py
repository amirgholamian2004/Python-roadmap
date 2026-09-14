from expense import Expense
import json
def save_expenses(expenses, file_name = "expenses.json"):
    data = [expense.to_dict() for expense in expenses]
    with open(file_name, "w") as file:
        json.dump(data, file)
def load_expenses(file_name = "expenses.json"):
    try:
        with open(file_name, "r") as file:
           data = json.load(file)
    except FileNotFoundError:
        return []
    return [Expense.from_dict(expense) for expense in data]
