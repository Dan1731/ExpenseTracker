from init_extension import db
from models import User, ExpenseTrans, ExpenseCat

from flask import Blueprint, render_template, request, redirect, url_for, session

add_expenses = Blueprint("add_expense_route", __name__)

@add_expenses.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == "POST":
        # if not 'user_id' in session:
        #     return redirect(url_for("login"))
        exp_title = request.form.get('expense_title')
        exp_desc = request.form.get('expense_desc')
        exp_amount = request.form.get('expense_amount')
        exp_cat_id = request.form.get('expense_cat')

        print(exp_amount)
        print(exp_desc)

    statement = db.select(ExpenseCat.name, ExpenseCat.id)
    categories = db.session.execute(statement).mappings().all()

    return render_template("AddExpense/add_expense.html", categories=categories)