from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models.user import User
from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_required
def dashboard():
    return render_template('auth/dashboard.html', user=current_user)


def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.find_by_username(username)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('auth/login.html')


def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if User.find_by_username(username):
            flash('Username already exists. Please choose a different username.')
        elif password != confirm_password:
            flash('Passwords do not match.')
        else:
            User.create(full_name, email, username, password)
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
    return render_template('auth/register.html')


@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
