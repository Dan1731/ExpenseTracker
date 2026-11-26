from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login_route.login"))
    return render_template("Dashboard/dashboard.html")