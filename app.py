##Purpose: create Flask app
##Author(s): Layce Smith, Miles Devine, Claudia Vargas
##Last Updated: 11/11/2026
##To activate environment (Windows): .venv\Scripts\activate
##To run the app: flask --app app run
##To run with debugger: flask --app app run --debug
from add_expense_route import add_expenses
from init_extension import db
from flask import Flask, render_template, session
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

    # User goes to expense table for now when sign in successful.
    @app.route("/expenses")
    def expenses():
        expenses = db.session.execute(db.select(ExpenseTrans)).scalars().all()
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
            largest_expense=largest_expense
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