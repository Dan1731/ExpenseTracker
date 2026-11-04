##Purpose: Blueprint for the user profile page (view and update account details)
##Author(s): Layce Smith
##Last Updated: 11/04/2026

from flask import Blueprint, render_template, request, redirect, url_for
from init_extension import db
from models import User

# Blueprint for profile routes; registered in app.py with app.register_blueprint(profile_bp)
profile_bp = Blueprint("profile", __name__)

# GET shows the profile page; POST saves changes submitted from the form
@profile_bp.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Look up the user by the username in the URL; return a 404 page if they don't exist
    user = User.query.filter_by(username=username).first_or_404()
    error = None # Stays None unless validation fails; shown in profile.html

    if request.method == "POST":
        # Read the submitted form fields (matched by each input's name attribute)
        # .strip() removes extra spaces at the start and end
        new_username = request.form.get("username", "").strip()
        first_name = request.form.get("first_name", "").strip()
        last_name = request.form.get("last_name", "").strip()
        email = request.form.get("email", "").strip()

        # Validate input before saving anything to the database
        if not new_username:
            error = "Username can't be empty."
        elif "@" not in email:
            error = "Please enter a valid email address."
        # Only check for duplicates if the username actually changed, otherwise the user would conflict with themselves
        elif new_username != user.username and User.query.filter_by(username=new_username).first():
            error = "That username is already taken."
        else:
            # All checks passed: update the user's record and save it
            user.username = new_username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            db.session.commit()
            # Redirect so a page refresh doesn't resubmit the form,
            # and so the URL matches the username if it changed
            return redirect(url_for("profile.profile", username=user.username))
    # Runs on a GET request, or on a POST that failed validation (shows the error)
    return render_template("profile.html", user=user, error=error)