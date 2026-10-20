from init_extension import db
from flask import Flask
import models

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///expense_tracker.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    






