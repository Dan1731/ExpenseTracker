##Purpose: create Flask app
##Author(s): Layce Smith, Miles Devine, Claudia Vargas
##Last Updated: 11/11/2026
##To activate environment (Windows): .venv\Scripts\activate
##To run the app: flask --app app run
##To run with debugger: flask --app app run --debug
from add_expense_route import add_expenses
from datetime import datetime, timedelta
from init_extension import db
from flask import Flask, render_template, session, request, redirect, url_for
from sqlalchemy import or_, text
from models import User, ExpenseTrans, ExpenseCat
from login_route import login_pages
from profile_route import profile_bp

def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///expense_tracker.db'

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    app.register_blueprint(login_pages)
    app.register_blueprint(profile_bp)
    app.register_blueprint(add_expenses)

    app.config["SECRET_KEY"] = "dev"  # Change this to a random value in production

    # Save the logged-in user to the session without changing login_route.py.
    # login() redirects only when the password check passes, so a redirect
    # from that endpoint means the login succeeded.
    @app.after_request
    def remember_login(response):
        if request.endpoint == "login_route.login" and response.status_code == 302:
            login_input = (request.form.get("login") or "").strip().lower()
            user = db.session.execute(
                db.select(User).where(
                    or_(User.username == login_input, User.email == login_input)
                )
            ).scalar_one_or_none()
            if user:
                session["username"] = user.username
                session["user_id"] = user.id
        return response

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login_route.home"))
    
    @app.route("/dashboard")
    def dashboard():
        
        if 'username' not in session: # Send back to login screen if the username is not present in the session variable
                return redirect(url_for("login_route.home"))
            
        username = session.get('username')
            
        user_id_query = text("""
        SELECT users.id
        FROM users
        WHERE users.username = :username
        """)
        
        user_id = db.session.execute(user_id_query, {"username" : username}).scalar()
        
        conditions = [] # list of conditions
        parameters = {"user_id" : user_id} # dict of parameters, we will always need the user_id

        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        category = request.form.get('category')
        upper_amount = request.form.get('upper_amount')
        lower_amount = request.form.get('lower_amount')

        if start_date:
            conditions.append("expense_trans.expense_date >= :start_date")
            parameters["start_date"] = start_date

        if end_date:
            conditions.append("expense_trans.expense_date <= :end_date")
            parameters["end_date"] = end_date
            
        if category:
            conditions.append("expense_cats.name = :category")
            parameters["category"] = category
            
        if upper_amount:
            conditions.append("expense_trans.amount <= :upper_amount")
            parameters["upper_amount"] = upper_amount

        if lower_amount:
            conditions.append("expense_trans.amount >= :lower_amount")
            parameters["lower_amount"] = lower_amount

        clause = " AND ".join(conditions)

        query = text(f"""
            SELECT
            expense_trans.title, expense_trans.amount, expense_trans.expense_date,
            expense_cats.name AS cat_name
            FROM expense_trans
            JOIN expense_cats on expense_cats.id = expense_trans.category_id
            WHERE {clause}
            """
        )
        
        print(query)
            
        result = db.session.execute(query, params=parameters).mappings().all()

    # User goes to expense table for now when sign in successful.
    @app.route("/expenses")
    def expenses():
        # Default fiilters:
        filtered_category = request.args.get("category", "all")
        start_date = request.args.get("start_date", "")
        end_date = request.args.get("end_date", "")
        search_title = request.args.get("search", "").strip()

        expense = db.select(ExpenseTrans)

        # Category filters.
        if filtered_category.isdigit():
            expense = expense.where(ExpenseTrans.category_id == int(filtered_category))

        # Date filters:
        if start_date:
            expense = expense.where(ExpenseTrans.expense_date >= datetime.fromisoformat(start_date))
        if end_date:
            expense = expense.where(ExpenseTrans.expense_date < datetime.fromisoformat(end_date) + timedelta(days=1))

        # Search expenses by title.
        if search_title:
            expense = expense.where(ExpenseTrans.title.ilike(f"%{search_title}%"))

        expenses = db.session.execute(expense).scalars().all()
        categories = db.session.execute(db.select(ExpenseCat.name, ExpenseCat.id)).mappings().all()

        # Overview amounts:
        total_expenses = sum(expense.amount for expense in expenses)
        total_transactions = len(expenses)
        largest_expense = max((expense.amount for expense in expenses), default=0) # Default if no expenses exist.

        return render_template(
            "ExpenseTable/table.html",
            expenses=expenses,
            categories=categories,
            total_expenses=total_expenses,
            total_transactions=total_transactions,
            largest_expense=largest_expense,
            filtered_category=filtered_category,
            start_date= start_date,
            end_date=end_date,
            search_title=search_title
        )

    with app.app_context():
        db.create_all()
        
        categories = [
        "Housing", "Transportation",
        "Food", "Tuition / Books",
        "Utilities", "Subscriptions",
        "Insurance", "Phone"]

        for name in categories:
            existing = db.session.execute(db.select(ExpenseCat).where(ExpenseCat.name == name)).scalar_one_or_none()

            if existing is None:
                db.session.add(ExpenseCat(name=name))

            db.session.commit()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 