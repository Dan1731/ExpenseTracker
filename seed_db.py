from init_extension import db
from flask import Flask
from models import User, ExpenseTrans, ExpenseCat
from sqlalchemy import func

from faker import Faker
fake = Faker()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///expense_tracker.db'

db.init_app(app)

with app.app_context():
    db.drop_all() # Drops all tables
    db.create_all() # Remakes all tables in models file

    for _ in range(50):
        user = User(
           username = fake.unique.user_name(),
           first_name = fake.first_name(),
           last_name = fake.last_name(),
           email = fake.unique.email(),
           password_hash = fake.password()
        )
        db.session.add(user)
    db.session.commit() # Commit users

    user_ids = db.session.execute(db.select(User.id)).scalars().all()
    
    categories = ["Housing", "Transportation", "Food", "Tuition / Books", "Utilities", "Subscriptions", "Insurance", "Phone"]

    for cat in categories:
        cat_entry = ExpenseCat(
            name = cat
        )
        db.session.add(cat_entry)
    db.session.commit() # Commit base categories
    
    categories = db.session.execute(db.select(ExpenseCat.id,
    ExpenseCat.name)).all()

    # Creating fake transactions for each category
    for id in user_ids:
        for category in categories:
            cat_id, cat_name = category
            for i in range(5):
                expense = ExpenseTrans(
                    amount = fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=10, max_value=1000),
                    title = f"Test {cat_name} Transaction # {i}",
                    category_id = cat_id,
                    user_id = id,
                    expense_date = fake.date_this_year(before_today=True, after_today=True)
                )
                db.session.add(expense)
    db.session.commit() # Commit transactions

    # Sample query

    statement = (
        db.select (
        User.id,
        User.username,
        ExpenseCat.name.label("expense_category"),
        func.avg(ExpenseTrans.amount).label("expense_average")
    )
    .join(User.expenses)
    .join(ExpenseTrans.category)
    .group_by(User.id, User.username, ExpenseCat.name)
    .order_by(User.id, ExpenseCat.id)
    )

    results = db.session.execute(statement).mappings().all() # Returns row object. We can access each value using the keys from above

    for result in results:
        print(f"ID {result['id']} | USERNAME {result['username']} | EXPENSE_CATEGORY {result['expense_category']} | AVG_AMOUNT {result['expense_average']}")
