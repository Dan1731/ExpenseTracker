from init_extension import db
import decimal
from datetime import datetime
from decimal import Decimal
from models import User, ExpenseTrans, ExpenseCat
from sqlalchemy import text
from flask import Blueprint, render_template, request, redirect, url_for, session

add_expenses = Blueprint("add_expense_route", __name__)

@add_expenses.route('/add_category', methods=['GET', 'POST'])
def add_category():
    error_message = None
        
    if 'username' not in session: # Send back to login screen if the username is not present in the session variable
        return redirect(url_for("login_route.home"))
    
    username = session.get('username')
        
    user_id_query = text("""
    SELECT users.id
    FROM users
    WHERE users.username = :username
    """)
        
    user_id = db.session.execute(user_id_query, {"username" : username}).scalar()
    
    if request.method == "POST":
        category_name = request.form.get('category_name')
        print(f"CATEGORY: {category_name}")
        
        category_exists_query = text("""
        SELECT EXISTS (
            SELECT 1
            FROM expense_cats
            WHERE LOWER(expense_cats.name) = LOWER(TRIM(:cat_name)) AND
            expense_cats.user_id = :user_id OR 
            LOWER(expense_cats.name) = LOWER(TRIM(:cat_name)) AND expense_cats.user_id IS NULL
        )
        """)
        
        existing_category = db.session.execute(
            category_exists_query,
            {"cat_name" : category_name, "user_id" : user_id}
        ).scalar()
        
        if existing_category: # Check that the category doesn't already exist in expense_cats
            error_message = "That category already exists. Please try again!"
            return render_template("AddExpense/add_category.html",
                            category_name=category_name,
                            error_message=error_message)
        
        add_category_query = text("""
        INSERT INTO expense_cats (name, user_id) VALUES (:cat_name, :user_id)
        """)
        
        try:
            db.session.execute(add_category_query, {"cat_name" : category_name, "user_id" : user_id})
            db.session.commit()
            print("Added new category name!")
            print(f"Added category {category_name}")
            return render_template("AddExpense/add_category.html", success_message="Category Added!")
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error occurred! {e}")
        
        
    else:
        return render_template("AddExpense/add_category.html")

@add_expenses.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    error_message = None
    
    if 'username' not in session: # Send back to login screen if the username is not present in the session variable
        return redirect(url_for("login_route.home"))
    
    username = session.get('username')
    
    user_id_query = text("""
    SELECT users.id
    FROM users
    WHERE users.username = :username
    """)
    
    user_id = db.session.execute(user_id_query, {"username" : username}).scalar()
    
    categories_query = text("""
    SELECT expense_cats.name, expense_cats.id
    FROM expense_cats
    WHERE expense_cats.user_id = :user_id OR
    expense_cats.user_id IS NULL
    """) # Categories that only the logged in user should have access to

    categories = db.session.execute(categories_query, {"user_id" : user_id}).mappings().all()
    
    if request.method == "POST":

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
        
        expense = ExpenseTrans(
            amount=amount,
            title=exp_title,
            description=exp_desc,
            category_id=exp_cat_id,
            expense_date=expense_date_obj,
            user_id=user_id # user_id 
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
        return render_template("AddExpense/add_expense.html", categories=categories)
