from init_extension import db
from flask import Flask
import models

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///expense_tracker.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home();
    return "Flask is running successfully!"

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    pass

if __name__ == '__main__':
    app.run(debug=True) 

