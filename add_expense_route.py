from init_extension import db
import decimal
from datetime import datetime
from decimal import Decimal
from models import User, ExpenseTrans, ExpenseCat
from sqlalchemy import or_
from flask import Blueprint, render_template, request, redirect, url_for, session

add_expenses = Blueprint("add_expense_route", __name__)

@add_expenses.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    error_message = None

    statement = db.select(ExpenseCat.name, ExpenseCat.id)
    categories = db.session.execute(statement).mappings().all()
    if request.method == "POST":
        # if not 'user_id' in session: // Send back to login screen if the user ID is not present in the session variable
        #     return redirect(url_for("login"))

        # user_id = session.get("user_id")

        # get information from our form

        exp_title = request.form.get('expense_title')
        exp_desc = request.form.get('expense_desc')
        exp_amount = request.form.get('expense_amount')
        exp_cat_id = request.form.get('expense_category')
        exp_date = request.form.get('expense_date')

        # title validation
        if not error_message:
            if not exp_title:
                error_message = "No title provided! Please provide one (max 50 chars)"
            elif len(exp_title) > 50:
                error_message = "Title is too long! Please try again (max 50 chars)"

        # description validation
        if not error_message:
            if exp_desc and len(exp_desc) > 100:
                error_message = "Invalid description provided. Please try again (max 100 chars)"

        # amount validation
        if not error_message:
            if not exp_amount:
                error_message = "Expense amount is required. Please try again"
        
            else:
                try:
                    amount = Decimal(exp_amount)
                    if amount <= 0 or amount.as_tuple().exponent < -2:
                        error_message = "Your last amount input had an invalid format. Please try again (must be be greater than $0.00 and use standard currency notation)"
                except (decimal.InvalidOperation, ValueError, TypeError):
                    error_message = "Your last amount input had an invalid format. Please try again (must be be greater than $0.00 and use standard currency notation)"

        # category validation. Need to make sure that the category that's entered is one of the user's categories ??
        if not error_message:
            if not exp_cat_id:
                error_message = "An expense category is required! Please select one from the list"
        
        # date validation
        if not error_message:
            if not exp_date:
                error_message = "A date is required! Please enter one"
            else:
                try:
                    expense_date_obj = datetime.fromisoformat(exp_date)
                    print(type(expense_date_obj))
                except ValueError:
                    error_message = "You have entered an invalid date. Please try again (mm/dd/yyyy)"

        if error_message:
            return render_template("AddExpense/add_expense.html",
            categories=categories,
            error_message=error_message,
            expense_title=exp_title,
            expense_desc=exp_desc,
            expense_amount=exp_amount,
            expense_cat=exp_cat_id,
            expense_date=exp_date)
        # else process for adding expense to the db here

        print(exp_title)
        print(exp_desc)
        print(exp_amount)
        print(exp_cat_id)
        print(exp_date)

        expense = ExpenseTrans(
            amount=amount,
            title=exp_title,
            description=exp_desc,
            category_id=exp_cat_id,
            expense_date=expense_date_obj,
            user_id="1" # user_id from session using 1 as placeholder here
        )

        try:
            db.session.add(expense)
            db.session.commit()
            print("Added expense!")
            print(f"Added expense {expense.id}")
            return render_template("AddExpense/add_expense.html", categories=categories, success_message="Expense Saved!")
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error occurred! {e}")

        


    if request.method == "GET":
        statement = db.select(ExpenseCat.name, ExpenseCat.id) # select statement for now that we don't have user's

        # when we have users

        # statement = db.select(ExpenseCat.name, ExpenseCat.id).where(
        #     or_(
        #         (ExpenseCat.user_id == user_id),
        #         (ExpenseCat.user_id == None)
        #         )
        #     )
        categories = db.session.execute(statement).mappings().all()

        return render_template("AddExpense/add_expense.html", categories=categories)
