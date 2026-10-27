import json


class ExpenseManager:

    def __init__(self, filename="expenses.json"):
        self.filename = filename

    def load_expenses(self):

        try:
            with open(self.filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

    def save_expenses(self, expenses):

        with open(self.filename, "w") as file:
            json.dump(expenses, file, indent=4)

    def add_expense(self, category, amount):

        expenses = self.load_expenses()

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        self.save_expenses(expenses)

    def delete_expense(self, index):

        expenses = self.load_expenses()

        if 0 <= index < len(expenses):
            expenses.pop(index)

        self.save_expenses(expenses)

    def total_expenses(self):

        expenses = self.load_expenses()

        return sum(expense["amount"] for expense in expenses)