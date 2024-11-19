from flask import Blueprint, session, request, redirect, url_for, flash
from src import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    """
    Login route, we use a very simplistic redis key/value for storing the username
    and the date of login. We could implement an evict mechanism based on the time
    of the last message sent by the user
    """
    username = request.form.get("username")

    if not username:
        flash("Can't user empty username!")
        return redirect(url_for('chat.index'))

    if db.get_user(username):
        flash('Username already in use!')
        return redirect(url_for('chat.index'))

    db.set_user(username)
    session["username"] = username
    return redirect(url_for('chat.home'))
