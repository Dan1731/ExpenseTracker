from init_extension import db
from models import User

from flask import Blueprint, render_template, request, redirect, url_for

from email_validator import validate_email, EmailNotValidError
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash

login_pages = Blueprint("login_route", __name__)

@login_pages.route("/")
def home():
    return render_template("Logins/login.html")

@login_pages.route("/login", methods=["POST"])
def login():
    login_input = (request.form.get("login") or "").strip().lower()
    password_input = request.form.get("password") or ""

    # If login is empty:
    if not login_input:
        return render_template(
            "Logins/login.html",
            login_error="Username or email can't be empty."
        )

    # If password is empty:
    if not password_input:
        return render_template(
            "Logins/login.html",
            password_error="Password can't be empty."
        )

    user = db.session.execute(
        db.select(User).where(
            or_(
                User.username == login_input,
                User.email == login_input
            )
        )
    ).scalar_one_or_none()

    if user is None or not check_password_hash(
    user.password_hash, password_input
    ):
            return render_template(
            "Logins/login.html",
            login_error="Invalid username/email or password."
        )

    # Redirect to expense table if credentials are verified.
    return redirect(url_for("expenses"))

@login_pages.route("/forgot-password")
def forgot_password():
    return render_template("ForgotPassword.html")

@login_pages.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = (request.form.get("first_name") or "").strip()
        last_name = (request.form.get("last_name") or "").strip()

        username = (request.form.get("username") or "").strip().lower()
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # User's name validation:
        if not first_name:
            return render_template(
                "Logins/login.html",
                first_name_error="Please enter your first name.",
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                show_signup=True
            )

        if not last_name:
            return render_template(
                "Logins/login.html",
                last_name_error="Please enter your last name.",
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                show_signup=True
            )

        # Useremail validation:
        if not username:
            return render_template(
                "Logins/login.html",
                username_error="Please enter a unique username.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        if len(username) < 4 or len(username) > 15:
            return render_template(
                "Logins/login.html",
                username_error="Username must be between 4 and 15 characters.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        # Check if username exists in database:
        existing_user = db.session.execute(
            db.select(User).filter_by(username=username)
        ).scalar_one_or_none()
        
        if existing_user:
            return render_template(
                "Logins/login.html",
                username_error="Username is already taken.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        # Email validation:
        if not email:
            return render_template(
                "Logins/login.html",
                email_error="Please enter a valid email.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )
        
        else:
            try:
                email_info = validate_email(email, check_deliverability=True)
                email = email_info.normalized

            except EmailNotValidError:
                return render_template(
                    "Logins/login.html",
                    email_error="Please enter a valid email address.",
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    show_signup=True
                )

        # Check if email already exists:
        existing_email = db.session.execute(
            db.select(User).filter_by(email=email)
        ).scalar_one_or_none()

        if existing_email:
            return render_template(
                "Logins/login.html",
                email_error="Seems like you already have an account! Please sign in.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        # Password validation:
        if not password:
            return render_template(
                "Logins/login.html",
                password_error="Password must be 8 to 20 characters long including an uppercase letter, lowercase letter, and number.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        ## Future: Decide whether we want to stay with hashing and make strong password suggestion
        ## Or if we wanna try encryptions.

        if not confirm_password:
            return render_template(
                "Logins/login.html",
                confirm_password_error="Please confirm your password.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        if len(password) < 8 or len(password) > 20:
            return render_template(
                "Logins/login.html",
                password_error="Password must be 8 to 20 characters long.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        if not any(char.isupper() for char in password):
            return render_template(
                "Logins/login.html",
                password_error="Password must have an uppercase letter.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        if not any(char.islower() for char in password):
            return render_template(
                "Logins/login.html",
                password_error="Password must have a lowercase letter.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        if not any(char.isdigit() for char in password):
            return render_template(
                "Logins/login.html",
                password_error="Password must contain a number.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        if confirm_password != password:
            return render_template(
                "Logins/login.html",
                confirm_password_error="Passwords do not match.",
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                show_signup=True
            )

        password_hash = generate_password_hash(password)

        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,            
            email=email,
            password_hash=password_hash
        )

        db.session.add(new_user)
        db.session.commit()

        return render_template(
            "Logins/login.html",
            success_message="Account created successfully! You can now sign in."
        )

    return render_template("Logins/login.html", show_signup=True)