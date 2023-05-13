from flask import (
    Blueprint, flash, g, render_template, redirect, request, url_for,
    current_app, session
)

bp = Blueprint('dashboard', __name__)

@bp.route("/dashboard/dashboard")
def HomePage():

    subjects = [
        {
            "nombre":"AC",
            "creditos":"6"
        },
        {
            "nombre":"SO",
            "creditos":"6"
        }
    ]
    return render_template("dashboard/dashboard.html", subjects = subjects)
