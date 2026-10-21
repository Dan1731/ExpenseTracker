##Purpose: create Flask app
##Author(): Layce Smith
##Last Updated: 10/21/2026
##To activate environment (Windows): .venv\Scripts\activate
##To run the app: flask --app app run
##To run with debugger: flask --app app run --debug
from flask import Flask, render_template, session
from markupsafe import escape
from getUser import get_user_by_id

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is running successfully!"


if __name__ == '__main__':
    app.run(debug=True)