from flask import Flask, render_template, request, redirect

from expense_manager import ExpenseManager

app = Flask(__name__)

manager = ExpenseManager()


@app.route("/")
def home():

    expenses = manager.load_expenses()

    total = manager.total_expenses()

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


@app.route("/add", methods=["GET", "POST"])
def add_expense():

    if request.method == "POST":

        category = request.form["category"]

        amount = float(
            request.form["amount"]
        )

        manager.add_expense(
            category,
            amount
        )

        return redirect("/")

    return render_template(
        "add_expense.html"
    )


@app.route("/delete/<int:index>")
def delete(index):

    manager.delete_expense(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)