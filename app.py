##Purpose: create Flask app
##Author(s): Layce Smith, Miles Devine, Claudia Vargas
##Last Updated: 10/21/2026
##To activate environment (Windows): .venv\Scripts\activate
##To run the app: flask --app app run
##To run with debugger: flask --app app run --debug
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