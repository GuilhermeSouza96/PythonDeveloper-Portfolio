from game_library import app
from flask import render_template, session, redirect, url_for, flash, request
from models import Users
from helpers import UserForm
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    next = request.args.get('next') or url_for('index')
    form = UserForm()
    return render_template('login.html', next = next, form = form)

@app.route('/authenticate', methods=['POST', ])
def authenticate():
    form = UserForm(request.form)

    user = Users.query.filter_by(nickname = form.nickname.data).first()
    password = check_password_hash(user.password, form.password.data)
    if user and password:
        session['user_logged'] = user.nickname
        flash(user.nickname + ' logged successfully!')
        next_page = request.form['next']
        return redirect(next_page)
    else:
        flash('User not logged in')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['user_logged'] = None
    flash('Logout successfully!')
    return redirect(url_for('index'))